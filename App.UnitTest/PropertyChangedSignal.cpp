#include <boost/test/unit_test.hpp>

#include "rbx/test/DataModelFixture.h"

#include "script/Script.h"
#include "script/ScriptContext.h"
#include "util/ProtectedString.h"
#include "util/RunStateOwner.h"
#include "v8datamodel/BasicPartInstance.h"
#include "v8datamodel/PartInstance.h"
#include "v8datamodel/Value.h"
#include "v8tree/Instance.h"

#include "G3D/System.h"

using namespace RBX;

// Instance:GetPropertyChangedSignal(name) returns a signal that:
//   * only fires when the given property changes
//   * calls its handlers with no arguments
//   * still supports connect / wait / disconnect like any other RBXScriptSignal
BOOST_AUTO_TEST_SUITE(PropertyChangedSignal)

// Evaluates a Lua expression in the fixture's script context, returns it as an int
static int scriptInt(DataModelFixture& fixture, const char* expression)
{
	std::auto_ptr<Reflection::Tuple> result = fixture.execute(expression);

	BOOST_REQUIRE(result.get());
	BOOST_REQUIRE_EQUAL(result->values.size(), 1);

	return result->values.at(0).convert<int>();
}

// Creates a part named TestPart in the workspace
static shared_ptr<PartInstance> createTestPart(DataModelFixture& fixture)
{
	shared_ptr<PartInstance> part = Creatable<Instance>::create<BasicPartInstance>();
	part->setName("TestPart");
	part->setParent(fixture.dataModel->getWorkspace());
	return part;
}

BOOST_FIXTURE_TEST_CASE(OnlyFiresForRequestedProperty, DataModelFixture)
{
	DataModel::LegacyLock lock(dataModel, DataModelJob::Write);

	shared_ptr<PartInstance> part = createTestPart(*this);

	execute(
		"local part = workspace.TestPart\n"
		"nameChanges = 0\n"
		"part:GetPropertyChangedSignal('Name'):connect(function()\n"
		"   nameChanges = nameChanges + 1\n"
		"end)\n"
		"return 0\n");

	// A change to a different property must be ignored
	part->setAnchored(!part->getAnchored());
	BOOST_CHECK_EQUAL(scriptInt(*this, "return nameChanges"), 0);

	// A change to the requested property fires exactly once
	part->setName("RenamedPart");
	BOOST_CHECK_EQUAL(scriptInt(*this, "return nameChanges"), 1);

	// Assigning the same value again does not raise a change
	part->setName("RenamedPart");
	BOOST_CHECK_EQUAL(scriptInt(*this, "return nameChanges"), 1);

	// ... and other changes keep firing it, one per change
	part->setAnchored(!part->getAnchored());
	part->setName("RenamedAgain");
	BOOST_CHECK_EQUAL(scriptInt(*this, "return nameChanges"), 2);
}

BOOST_FIXTURE_TEST_CASE(HandlerIsCalledWithoutArguments, DataModelFixture)
{
	DataModel::LegacyLock lock(dataModel, DataModelJob::Write);

	shared_ptr<PartInstance> part = createTestPart(*this);

	execute(
		"local part = workspace.TestPart\n"
		"argumentCount = -1\n"
		"part:GetPropertyChangedSignal('Name'):connect(function(...)\n"
		"   argumentCount = select('#', ...)\n"
		"end)\n"
		"return 0\n");

	BOOST_CHECK_EQUAL(scriptInt(*this, "return argumentCount"), -1);

	part->setName("RenamedPart");
	BOOST_CHECK_EQUAL(scriptInt(*this, "return argumentCount"), 0);
}

BOOST_FIXTURE_TEST_CASE(DisconnectStopsNotifications, DataModelFixture)
{
	DataModel::LegacyLock lock(dataModel, DataModelJob::Write);

	shared_ptr<PartInstance> part = createTestPart(*this);

	execute(
		"local part = workspace.TestPart\n"
		"nameChanges = 0\n"
		"connection = part:GetPropertyChangedSignal('Name'):connect(function()\n"
		"   nameChanges = nameChanges + 1\n"
		"end)\n"
		"return 0\n");

	part->setName("First");
	BOOST_CHECK_EQUAL(scriptInt(*this, "return nameChanges"), 1);

	execute("connection:disconnect()\nreturn 0\n");

	part->setName("Second");
	BOOST_CHECK_EQUAL(scriptInt(*this, "return nameChanges"), 1);
}

BOOST_FIXTURE_TEST_CASE(MultipleConnectionsAllFire, DataModelFixture)
{
	DataModel::LegacyLock lock(dataModel, DataModelJob::Write);

	shared_ptr<PartInstance> part = createTestPart(*this);

	execute(
		"local part = workspace.TestPart\n"
		"nameChanges = 0\n"
		"part:GetPropertyChangedSignal('Name'):connect(function()\n"
		"   nameChanges = nameChanges + 1\n"
		"end)\n"
		"return 0\n");

	part->setName("First");
	BOOST_CHECK_EQUAL(scriptInt(*this, "return nameChanges"), 1);

	// Signals from GetPropertyChangedSignal are still first-class signals
	execute(
		"local part = workspace.TestPart\n"
		"otherChanges = 0\n"
		"part:GetPropertyChangedSignal('Name'):connect(function()\n"
		"   otherChanges = otherChanges + 1\n"
		"end)\n"
		"return 0\n");

	part->setName("Second");
	BOOST_CHECK_EQUAL(scriptInt(*this, "return nameChanges"), 2);
	BOOST_CHECK_EQUAL(scriptInt(*this, "return otherChanges"), 1);
}

BOOST_FIXTURE_TEST_CASE(ConnectionObjectIsUsable, DataModelFixture)
{
	DataModel::LegacyLock lock(dataModel, DataModelJob::Write);

	createTestPart(*this);

	std::auto_ptr<Reflection::Tuple> result = execute(
		"local part = workspace.TestPart\n"
		"connection = part:GetPropertyChangedSignal('Name'):connect(function() end)\n"
		"return connection.connected, tostring(part:GetPropertyChangedSignal('Name'))\n");

	BOOST_REQUIRE_EQUAL(result->values.size(), 2);
	BOOST_CHECK(result->values.at(0).convert<bool>());
	BOOST_CHECK(result->values.at(1).convert<std::string>().find("Name") != std::string::npos);
}

BOOST_FIXTURE_TEST_CASE(InvalidPropertyThrows, DataModelFixture)
{
	DataModel::LegacyLock lock(dataModel, DataModelJob::Write);

	createTestPart(*this);

	bool threw = false;

	try
	{
		execute(
			"local part = workspace.TestPart\n"
			"part:GetPropertyChangedSignal('NotARealProperty')\n"
			"return 0\n");
	}
	catch (std::exception& e)
	{
		threw = true;
		BOOST_CHECK(std::string(e.what()).find("NotARealProperty") != std::string::npos);
	}

	BOOST_CHECK(threw);
}

BOOST_FIXTURE_TEST_CASE(WaitResumesOnRequestedProperty, DataModelFixture)
{
	shared_ptr<PartInstance> part = Creatable<Instance>::create<BasicPartInstance>();
	part->setName("TestPart");

	shared_ptr<StringValue> marker = Creatable<Instance>::create<StringValue>();
	marker->setName("Marker");

	{
		DataModel::LegacyLock lock(dataModel, DataModelJob::Write);

		marker->setParent(dataModel->getWorkspace());
		part->setParent(dataModel->getWorkspace());

		shared_ptr<Script> script = Creatable<Instance>::create<Script>();
		script->setEmbeddedCode(ProtectedString::fromTestSource(
			"local part = workspace.TestPart\n"
			"local marker = workspace.Marker\n"
			"part:GetPropertyChangedSignal('Name'):wait()\n"
			"marker.Value = 'woke up'\n"));
		script->setParent(dataModel->getWorkspace());

		ServiceProvider::create<RunService>(dataModel.get())->run();
	}

	// Changing an unrelated property must not resume the waiting script
	{
		DataModel::LegacyLock lock(dataModel, DataModelJob::Write);
		part->setAnchored(true);
	}

	{
		DataModel::LegacyLock lock(dataModel, DataModelJob::Write);
		BOOST_CHECK_EQUAL(marker->getValue(), "");
		part->setName("Triggered");
	}

	G3D::System::sleep(.3f);

	DataModel::LegacyLock lock(dataModel, DataModelJob::Write);
	BOOST_CHECK_EQUAL(marker->getValue(), "woke up");
}

BOOST_FIXTURE_TEST_CASE(UnfilteredChangedSignalStillFiresForEverything, DataModelFixture)
{
	DataModel::LegacyLock lock(dataModel, DataModelJob::Write);

	shared_ptr<PartInstance> part = createTestPart(*this);

	execute(
		"local part = workspace.TestPart\n"
		"changes = 0\n"
		"part.Changed:connect(function()\n"
		"   changes = changes + 1\n"
		"end)\n"
		"return 0\n");

	const int before = scriptInt(*this, "return changes");

	part->setAnchored(true);
	BOOST_CHECK(scriptInt(*this, "return changes") > before);

	const int afterAnchored = scriptInt(*this, "return changes");

	part->setName("Renamed");
	BOOST_CHECK(scriptInt(*this, "return changes") > afterAnchored);
}

BOOST_FIXTURE_TEST_CASE(WorksOnNonPartInstances, DataModelFixture)
{
	DataModel::LegacyLock lock(dataModel, DataModelJob::Write);

	shared_ptr<StringValue> value = Creatable<Instance>::create<StringValue>();
	value->setName("TestValue");
	value->setParent(dataModel->getWorkspace());

	execute(
		"local value = workspace.TestValue\n"
		"valueChanges = 0\n"
		"value:GetPropertyChangedSignal('Value'):connect(function()\n"
		"   valueChanges = valueChanges + 1\n"
		"end)\n"
		"return 0\n");

	// The default value means the first assignment changes it
	value->setValue("hello");
	BOOST_CHECK_EQUAL(scriptInt(*this, "return valueChanges"), 1);

	value->setValue("hello");
	BOOST_CHECK_EQUAL(scriptInt(*this, "return valueChanges"), 1);

	value->setValue("world");
	BOOST_CHECK_EQUAL(scriptInt(*this, "return valueChanges"), 2);
}

BOOST_AUTO_TEST_SUITE_END()
