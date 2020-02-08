'''
	There are two sorted arrays nums1 and nums2 of size m and n respectively.

	Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

	Example 1:
	nums1 = [1, 3]
	nums2 = [2]

	The median is 2.0
	Example 2:
	nums1 = [1, 2]
	nums2 = [3, 4]

	The median is (2 + 3)/2 = 2.5
'''
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m
        if n == 0:
            raise ValueError
        imin, imax, half_len = 0, m, int((m + n + 1) / 2)
        print("m: ", m)
        print("n: ", n)
        print("init imin: ", imin)
        print("init imax: ", imax)
        print("half_len: ", half_len)
        print('------------------------------')
        while imin <= imax:
            print("loop imin: ", imin)
            print("loop imax: ", imax)
            i = int((imin + imax) / 2)
            j = half_len - i
            print("i: ", i)
            print("j: ", j)
            if (i < m) and (nums2[j-1] > nums1[i]):
                # i is too small, must increase it
                imin = i + 1
            elif (i > 0) and (nums1[i-1] > nums2[j]):
                # i is too big, must decrease it
                imax = i - 1
            else:
                # i is perfect
    
                if i == 0: max_of_left = nums2[j-1]
                elif j == 0: max_of_left = nums1[i-1]
                else: max_of_left = max(nums1[i-1], nums2[j-1])
    
                if (m + n) % 2 == 1:
                    return max_of_left
    
                if i == m: min_of_right = nums2[j]
                elif j == n: min_of_right = nums1[i]
                else: min_of_right = min(nums1[i], nums2[j])
    
                return (max_of_left + min_of_right) / 2.0
            
        


print(Solution().findMedianSortedArrays([1,2], [3, 4]))