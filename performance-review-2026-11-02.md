# Performance review — 2026-11-02

## Scope and method

This is a static, targeted review, not an exhaustive audit or a runtime profile of
all 146,000+ tracked files (most are third-party libraries). I surveyed the
first-party application, networking, rendering and base code for repeated linear
searches, front erases, copies, and documented performance concerns. Findings
were prioritized by scaling behavior and confidence that semantics can be kept.
No changes were made to vendored libraries.

## Changes

- **Streaming GC:** `RegionRemovalItem` now uses a hash lookup in addition to its
  ordered ID vector. Duplicate detection is expected O(n) total rather than
  O(n²), while first-seen serialization order is unchanged. The lookup is
  released after collecting the region to limit memory retained in pending
  packets. The hash table does add transient memory during collection.
- **Streaming GC joint cleanup:** take one snapshot of pending parts and pass it
  by reference through the synchronous descendant visitor instead of copying a
  vector of shared pointers for every visited instance. The actual per-joint
  scan remains linear and preserves duplicate handling and callback order.
- **Cached initial terrain replication:** consume the FIFO chunk queue with a
  deque instead of repeatedly shifting a vector. Chunk order and send budgets
  are unchanged; draining the queue changes from O(n²) to O(n).
- **Studio manual joint detection:** build a membership set once instead of
  rescanning all selected primitives for each touching candidate. The original
  vector still determines traversal and result ordering.

## Validation and follow-up

The standalone `tests/ordered_set_test.cpp` compares the actual ordered set
against the old linear algorithm with 100,000 insertions including duplicates.
Engine unit tests were added for GUID order/deduplication and chunk FIFO state,
but were not run here: this environment lacks the documented Windows toolchain
and CMake. The checked-in Boost tree also omits some headers due to ignore rules;
the standalone test was run with Boost 1.74 preprocessor and predef headers
fetched separately. For example, add their `include` directories to the compiler
command in that test before `-ILibrary/boost`.

These are algorithmic improvements, not measured end-to-end frame-time or network
throughput gains. Profile representative large streaming worlds, initial terrain
loads, and large Studio selections on supported builds; verify packet-level
compatibility, GC memory peaks, and joint/terrain behavior with the full suite.
Other candidates (including the remaining per-joint scan and renderer cluster
updates) require profiling and behavioral tests before changing them. This review
does not establish that all hot paths or performance issues have been found.
