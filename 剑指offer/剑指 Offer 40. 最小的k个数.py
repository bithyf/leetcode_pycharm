class Solution(object):
    def getLeastNumbers(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """

        def quickSort(nums, front, back):
            mid_num = nums[front]
            f = front
            b = back
            while f < b:
                while f < b and nums[b] > mid_num:
                    b -= 1
                nums[f] = nums[b]
                while f < b and nums[f] <= mid_num:
                    f += 1
                nums[f] = nums[b]
            nums[f] = mid_num
            return f

        f = 0
        b = len(arr)
        while True:
            mid = quickSort(arr, f, b)
            if mid == k - 1:
                return arr[:k]
            elif mid > k - 1:
                b = mid - 1
            else:
                f = mid + 1
