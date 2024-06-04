def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        # i = 0
        # j = 0

        # Greedy
        # nums = []
        # i = 0
        # j = 0
        # while i < m and j < n:
        #     if nums1[i] <= nums2[j]:
        #         nums.append(nums1[i])
        #         i += 1
        #     elif nums1[i] > nums2[j]:
        #         nums.append(nums2[j])
        #         j += 1
        # if i != m:
        #     while i < m:
        #         nums.append(nums1[i])
        #         i += 1
        # elif j != n:
        #     while j < n:
        #         nums.append(nums2[j])
        #         j += 1
        
        # for i in range(len(nums1)):
        #     nums1[i] = nums[i]


        # not using extra space
        if len(nums2) <= 0:
            return
        
        while m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]
        return nums1

# Time: O(n)
# Space: O(1)

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
print(merge(nums1, m, nums2, n)) # [1,2,2,3,5,6]