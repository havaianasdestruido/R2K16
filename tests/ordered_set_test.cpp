// Standalone: g++ -std=c++11 -I. -ILibrary/boost tests/ordered_set_test.cpp -o /tmp/ordered_set_test && /tmp/ordered_set_test
#include "Network/OrderedSet.h"
#include <algorithm>
#include <cassert>
#include <vector>

int main()
{
    RBX::Network::OrderedSet<int> actual;
    std::vector<int> expected;
    // Repeated and non-monotonic values exercise duplicate detection and ordering.
    for (int i = 0; i < 100000; ++i)
    {
        int value = (i * 97) % 5000;
        bool isNew = std::find(expected.begin(), expected.end(), value) == expected.end();
        assert(actual.insert(value) == isNew);
        if (isNew)
            expected.push_back(value);
    }
    actual.finish();
    assert(actual.size() == expected.size());
    for (size_t i = 0; i < expected.size(); ++i)
        assert(actual[i] == expected[i]);
}
