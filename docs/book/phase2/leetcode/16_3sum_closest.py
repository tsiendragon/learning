from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        assert len(nums)>=3
        min_value = abs(sum(nums[:3])-target)
        min_index = [0,1,2]
        if len(nums)==3:
            return sum(nums)
        for i in range(len(nums)-2):
            min_index_current, min_value_current = self.two_sum_closest(nums[i+1:], target-nums[i])
            if min_value_current< min_value:
                min_index = [i, min_index_current[0]+i+1, min_index_current[1]+i+1]
                min_value = min_value_current

        return sum([nums[j] for j in min_index])


    def two_sum_closest(self, nums: List[int], target:int) -> int:
        min_value = abs(sum(nums[:2])-target)
        min_index = [0,1]
        for i in range(len(nums)-1):
            min_index_current, min_value_current = self.one_closest(nums[i+1:], target-nums[i])
            if min_value_current< min_value:
                min_value = min_value_current
                min_index =[i,min_index_current+i+1 ]
        return min_index, min_value



    def one_closest(self, nums: List[int], target:int)-> int:
        nums_a = [abs(x - target) for x in nums]
        min_v = min(nums_a)
        min_index = nums_a.index(min_v)
        return min_index, min_v


class Solution1M:
    """without y==0, 4279 ms, with y==0, 47ms"""
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        if len(nums)==3:
            return sum(nums)
        min_value = sum(nums[:3])
        largest_value = sum(nums[-3:])
        if min_value >= target:
            return min_value
        if largest_value <= target:
            return largest_value
        current_min  = abs(min_value-target)
        result = min_value
        for i, x in enumerate(nums[:-2]):

            current_sum  = self.two_sum_closest(nums[i+1:], target-x) + x
            y =abs(current_sum - target)
            if y==0:
                return current_sum
            if y  < current_min:
                current_min = y
                result = current_sum
        return result

    def two_sum_closest(self, nums: List[int], target:int) -> int:
        if len(nums)==2:
            return sum(nums)
        min_value = sum(nums[:2])
        largest_value = sum(nums[-2:])
        if min_value >= target:
            return min_value
        if largest_value <= target:
            return largest_value
        current_min  = abs(min_value-target)
        result = min_value
        for i, x in enumerate(nums[:-1]):
            current_sum  = self.one_closest(nums[i+1:], target-x) + x
            y = abs(current_sum - target)
            if y==0:
                return current_sum
            if y  < current_min:

                current_min = y
                result = current_sum
        return result



    def one_closest(self, nums: List[int], target:int)-> int:
        return min([(x, abs(target - x)) for x in nums], key = lambda x: x[1])[0]

class Solution2:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        assert len(nums)>=3
        nums.sort()
        result = sum(nums[:3])
        min_value = abs(result-target)
        if len(nums)==3:
            return sum(nums)
        for i in range(len(nums)-2):
            current_sum = self.two_sum_closest(nums[i+1:], target-nums[i])
            if abs(current_sum+nums[i]-target) < min_value:
                result  = current_sum + nums[i]
                min_value = abs(result-target)

        return result


    def two_sum_closest(self, nums: List[int], target:int) -> int:
        # use  pointers
        result = sum(nums[:2])
        left, right = 0, len(nums)-1
        while left < right:
            sum_2 = nums[left]+nums[right]
            if abs(sum_2-target) < abs(result-target):
                result = sum_2
            if sum_2<target:
                left+=1
            elif sum_2>target:
                right-=1
            else:
                return result
        return result

class Solution3:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        return self.KSumClosest(nums, 3, target)

    def KSumClosest(self, nums: List[int], k: int, target: int) -> int:
        N = len(nums)
        if N == k:
            return sum(nums[:k])

        # target too small
        current = sum(nums[:k])
        if current >= target:
            return current

        # target too big
        current = sum(nums[-k:])
        if current <= target:
            return current

        if k == 1:
            return min([(x, abs(target - x)) for x in nums], key = lambda x: x[1])[0]

        closest = sum(nums[:k])
        for i, x in enumerate(nums[:-k+1]):
            if i>0 and x == nums[i-1]:
                continue
            current = self.KSumClosest(nums[i+1:], k-1, target - x) + x
            if abs(target - current) < abs(target - closest):
                if current == target:
                    return target
                else:
                    closest = current

        return closest

if __name__ == '__main__':
    sol = Solution1M()
    # sol = Solution3()
    nums = [[1,1,1,0], [-1,2,1,-4], list(range(999))]
    target = [-100,1, 748]
    answer = [2,2,748]
    for i in range(len(nums)):
        y = sol.threeSumClosest(nums[i], target[i])
        print('y',y)
        assert y ==answer[i], f'expected {answer[i]}, got {y}'
