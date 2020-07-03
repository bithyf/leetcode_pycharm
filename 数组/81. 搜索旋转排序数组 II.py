def search(nums, target):
    begin = 0
    end = len(nums) - 1
    while begin <= end:
        mid = (begin + end) // 2
        if target == nums[mid]:
            return True
        elif nums[begin] >= nums[end]:
            if nums[begin] == nums[end] == nums[mid]:
                begin += 1
                while begin <= end and nums[begin] != nums[begin]:
                    begin += 1
                end -= 1
                while begin <= end and nums[end] != nums[end]:
                    end -= 1
                continue
            if nums[mid] >= nums[begin]:
                if target > nums[mid]:
                    begin = mid + 1
                else:
                    if target >= nums[begin]:
                        end = mid - 1
                    else:
                        begin = mid + 1
            else:
                if target < nums[mid]:
                    end = mid - 1
                else:
                    if target > nums[end]:
                        end = mid - 1
                    else:
                        begin = mid + 1
        else:
            if target > nums[mid]:
                begin = mid + 1
            else:
                end = mid - 1
    return False
