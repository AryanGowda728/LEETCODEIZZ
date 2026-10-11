# 4. Median of Two Sorted Arrays

[LeetCode problem](https://leetcode.com/problems/median-of-two-sorted-arrays/)

## Approach

The arrays are already sorted, so there is no need to merge them. Instead, choose a cut in each array so the combined left half contains half of the elements (or one extra element when the total length is odd).

Binary search for the cut in the shorter array. The second cut is determined by the desired left-half size. A valid partition has every value on the left less than or equal to every value on the right. Checking the four values next to the cuts tells us whether the partition is valid or which direction to continue searching.

Once the partition is valid, the median is the largest value on the left for an odd total length. For an even total length, it is the average of the largest left value and the smallest right value. Infinite sentinels handle cuts at either end of an array.

## Core Pattern

**Binary search on a partition:** search for the split point in the shorter sorted array, while deriving the matching split in the other array.

## Complexity

- **Time:** `O(log(min(m, n)))`, where `m` and `n` are the input lengths. Each binary-search step does constant work.
- **Space:** `O(1)`, using a fixed number of variables.
