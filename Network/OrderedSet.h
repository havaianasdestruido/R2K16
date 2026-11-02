#pragma once

#include <boost/unordered_set.hpp>
#include <vector>

namespace RBX { namespace Network {

// Stream-out messages must retain first-seen order on the wire, while avoiding
// a linear scan of all previously collected IDs for every descendant.
template <typename T>
class OrderedSet
{
    std::vector<T> ordered;
    boost::unordered_set<T> seen;

public:
    bool insert(const T& id)
    {
        if (!seen.insert(id).second)
            return false;
        ordered.push_back(id);
        return true;
    }

    // Call only after the last insertion; queued messages no longer need the lookup table.
    void finish() { boost::unordered_set<T>().swap(seen); }

    size_t size() const { return ordered.size(); }
    const T& operator[](size_t index) const { return ordered[index]; }
};

} } // namespace RBX::Network
