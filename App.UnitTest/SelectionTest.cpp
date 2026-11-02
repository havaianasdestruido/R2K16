#include <boost/test/unit_test.hpp>

#include "rbx/test/DataModelFixture.h"
#include "rbx/test/ScopedFastFlagSetting.h"
#include "V8DataModel/BasicPartInstance.h"
#include "V8DataModel/Selection.h"
#include "V8DataModel/ScreenGui.h"
#include "V8DataModel/PlayerGui.h"
#include "network/Player.h"
#include "network/Players.h"

using namespace RBX;

BOOST_AUTO_TEST_SUITE( SelectionTest )

BOOST_AUTO_TEST_CASE(RemovingFromDataModelRemovesFromSelection)
{
	DataModelFixture dm;
	DataModel::LegacyLock lock(&dm, DataModelJob::Write);

	shared_ptr<BasicPartInstance> part = Creatable<Instance>::create<BasicPartInstance>();
	part->setParent(dm->getWorkspace());

	Selection* selection = dm->create<Selection>();
	selection->setSelection(part.get());

	BOOST_CHECK_EQUAL(1, selection->size());
	BOOST_CHECK_EQUAL(part.get(), selection->front().get());

	part->setParent(NULL);

	BOOST_CHECK_EQUAL(0, selection->size());
}

BOOST_AUTO_TEST_CASE(NotInDataModelBlockedFromSelection)
{
	DataModelFixture dm;
	DataModel::LegacyLock lock(&dm, DataModelJob::Write);

	shared_ptr<BasicPartInstance> part = Creatable<Instance>::create<BasicPartInstance>();

	Selection* selection = dm->create<Selection>();

	const size_t expectedSize = 0;

	selection->clearSelection();
	selection->setSelection(part.get());
	BOOST_CHECK_EQUAL(expectedSize, selection->size());

	selection->clearSelection();
	selection->addToSelection(part.get());
	BOOST_CHECK_EQUAL(expectedSize, selection->size());

	selection->clearSelection();
	selection->toggleSelection(part.get());
	BOOST_CHECK_EQUAL(expectedSize, selection->size());

	selection->clearSelection();
	part.reset();
}

BOOST_AUTO_TEST_SUITE_END()

BOOST_AUTO_TEST_CASE(LayerCollectorResetOnSpawn)
{
	DataModelFixture dm;
	DataModel::LegacyLock lock(&dm, DataModelJob::Write);
	StarterGuiService* starter = dm->create<StarterGuiService>();
	Network::Players* players = dm->create<Network::Players>();
	shared_ptr<Network::Player> player = Creatable<Instance>::create<Network::Player>();
	player->setParent(players);
	player->createPlayerGui();
	PlayerGui* gui = player->findFirstChildOfType<PlayerGui>();
	BOOST_REQUIRE(gui);

	shared_ptr<ScreenGui> persistent = Creatable<Instance>::create<ScreenGui>();
	persistent->setName("Persistent");
	BOOST_CHECK(persistent->getResetOnSpawn());
	persistent->setResetOnSpawn(false);
	persistent->setParent(starter);
	shared_ptr<ScreenGui> resetting = Creatable<Instance>::create<ScreenGui>();
	resetting->setName("Resetting");
	resetting->setParent(starter);

	player->rebuildGui();
	shared_ptr<Instance> oldPersistent = shared_from(gui->findFirstChildByName("Persistent"));
	shared_ptr<Instance> oldResetting = shared_from(gui->findFirstChildByName("Resetting"));
	BOOST_REQUIRE(oldPersistent);
	BOOST_REQUIRE(oldResetting);
	BOOST_CHECK(!Instance::fastDynamicCast<ScreenGui>(oldPersistent.get())->getResetOnSpawn());
	player->rebuildGui();
	BOOST_CHECK_EQUAL(gui->findFirstChildByName("Persistent"), oldPersistent.get());
	BOOST_CHECK(gui->findFirstChildByName("Resetting") != oldResetting.get());
	BOOST_CHECK_EQUAL(gui->numChildren(), 2u);

	starter->setResetPlayerGui(false);
	shared_ptr<Instance> currentResetting = shared_from(gui->findFirstChildByName("Resetting"));
	player->rebuildGui();
	BOOST_CHECK_EQUAL(gui->findFirstChildByName("Resetting"), currentResetting.get());
}
