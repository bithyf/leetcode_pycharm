def containsDuplicate(self, nums: List[int]) -> bool:
    nums_set = set(nums)
    if len(nums_set) != len(nums) and len(nums) != 0:
        return True
    else:
        return False