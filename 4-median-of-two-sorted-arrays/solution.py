class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        # Binary search the shorter array to keep the search logarithmic.
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        left_size = (m + n + 1) // 2
        low, high = 0, m

        while low <= high:
            cut1 = (low + high) // 2
            cut2 = left_size - cut1

            left1 = float("-inf") if cut1 == 0 else nums1[cut1 - 1]
            right1 = float("inf") if cut1 == m else nums1[cut1]
            left2 = float("-inf") if cut2 == 0 else nums2[cut2 - 1]
            right2 = float("inf") if cut2 == n else nums2[cut2]

            if left1 > right2:
                high = cut1 - 1
            elif left2 > right1:
                low = cut1 + 1
            else:
                if (m + n) % 2:
                    return float(max(left1, left2))

                return (max(left1, left2) + min(right1, right2)) / 2.0
