class Solution:
    # 先来一个二分搜索
    def binary_search(self,nums,target):
        left,right = 0,len(nums)-1    # [left,right]
        while left <= right:
            mid = (left + right) // 2 
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1 
            else:
                left = mid + 1 
        return -1

    # Leetcode 283  move zeros
    # [1,0,4,0,13] ==> [1,4,13,0,0]
    # 第一种方法 ： 额外新建了一个列表，空间复杂度+1
    def moveZeros(self,nums:list):
        new_num = []
        for i in range(len(nums)):
            if nums[i] != 0:
                new_num.append(nums[i])
        for i in range(len(nums) - len(new_num)):
            new_num.append(0)
        return new_num

    def moveZeros1(self,nums:list):
        # 第二种方法，不新建列表。使用一个指针k来记载非0元素
        k = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                if k != i:   # 特殊判断，如果遇到数组中全都是非元素，避免自己和自己交换
                    nums[k],nums[i] = nums[i],nums[k]
                    k += 1
                else:
                    k += 1
        return nums
    
    # leetcode 27 remove element
    def remove_element_1(self,nums,val):
        # 暴力while循环
        while val in nums:
            nums.remove(val)
        return len(nums)

    def remove_element_2(self,nums,val):
        # for倒着循环
        for i in range(len(nums)-1,-1,-1):   # [len(nums)-1,0]
            if nums[i] == val:
                nums.pop(i)
        return len(nums)

    def removeelement_3(self, nums, val: int) -> int:
        # 双指针
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return len(nums[:k])

    # leetcode 26 删除排序数组中的重复项（排好序的列表原地去重）
    def removeDuplicates_1(self, nums) -> int:
        k = 0
        for i in range(1,len(nums)):
            if nums[i] != nums[k]:
                nums[k] = nums[i]
                k += 1
        return k + 1

    def removeDuplicates_2(self,nums):
        for i in range(len(nums)-2,-1,-1):
            if nums[i] == nums[i+1]:
                nums.pop(i)
        return len(nums)

    # leetcode 80 删除数组中的重复元素


    # 三路快排
    # 85
    def sortColurs(self,nums):
        zeros = -1                # nums[0,zeros....] == 0
        two = len(nums)           # nums[two.....n-1] == 2
        i = 0
        while i < two:
            if nums[i] == 2:
                two -= 1
                nums[i],nums[two] = nums[two],nums[i]
            elif nums[i] == 1:
                i += 1
            else:
                zeros += 1
                nums[i],nums[zeros] = nums[zeros],nums[i]
                i += 1
        return nums

    # 88  合并两个有序数组

    # 215 medium 数组中第K个最大元素

    # 对撞指针 （两个指针，索引，一首一尾，分别向中间对撞）
    # lc 167 TwoSum — 输入有序数组
    def twoSum(self,nums,target):
        l,r = 0,len(nums) - 1
        while l < r:
            if nums[l] + nums[r] == target:
                return [l+1,r+1]
            elif nums[l] + nums[r] < target:
                l = l+1
            else:
                r = r - 1
        return -1

    # 125 valid palinedrome
    def valid_palinedrome(self,s:str):
        s = filter(str.isalnum,s)
        s = ''.join(s).lower()
        l,r = 0,len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False
        return True
    # 344 reverse str

    # 345 reverse str google

    # 双索引技术 Two Point --> 滑动窗口
    # 209 min size subarray sum
    def minSubArrayLen(self, s: int, nums: list[int]) -> int:
        l = 0
        r = -1
        res = len(nums) + 1
        sum = 0
        while l < len(nums):
            if (r+1<len(nums)) & (sum < s):
                r += 1
                sum += nums[r]
            else:
                sum -= nums[l]
                l += 1
            if sum >= s:
                res = min(res,r-l+1)
        if res == len(nums) + 1:
            return 0
        return res

s = Solution()
# res = s.binary_search([1,3,5,7,9],3)
# print(res)
# res = s.removeDuplicates_2([1,1,4,99,1,4,6,7,7,8,10])
res = s.sortColurs([1,2,2,0,1,0,2])
print(res)