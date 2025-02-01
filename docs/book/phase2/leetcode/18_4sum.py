from typing import List

from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        results = []
        if len(nums)<4:
            return results
        if sum(nums[:4])> target:
            return results
        if sum(nums[-4:])< target:
            return results
        for i, num in enumerate(nums[:-3]):
            current_result = self.three_sum(nums[i+1:], target-nums[i])
            current_result = [xi + [num] for xi in current_result]
            results += current_result
        results = [tuple(sorted(x)) for x in results]
        results = list(set(results))
        results = [list(xi) for xi in results]
        return results

    def three_sum(self, nums, target):
        results = []
        if sum(nums[:3])> target:
            return results
        if sum(nums[-3:])< target:
            return results
        for i, num in enumerate(nums[:-2]):
            current_results = self.two_sum(nums[i+1:], target-nums[i])
            current_results = [xi + [num] for xi in current_results]
            results += current_results
        return results



    def two_sum(self, nums, target):
        # assume nums is sorted
        n = len(nums)
        i = 0
        j = n-1
        current_sum = nums[i]+nums[j]
        results = []
        if sum(nums[:2]) > target:
            return results
        if sum(nums[-2:]) < target:
            return results
        while i<j:
            current_sum = nums[i]+nums[j]

            if current_sum==target:
                results.append([nums[i], nums[j]])
                i +=1
            elif current_sum < target:
                i += 1
            else:
                j -= 1
        return results


class Solution2(Solution):
    def two_sum(self, nums, target):
        l = dict()
        for k,v in enumerate(nums):
            if target-v in l:
                l[target-v].append(k)
            else:
                l[target-v]  = [k]
        results =[]
        for k,v in enumerate(nums):
            if v in l and (not [k]==l[v]):
                results.append([v, target-v])
        return results

class Solution3(Solution):
    def two_sum(self, nums, target):
        # assume nums is sorted
        n = len(nums)
        i = 0
        j = n-1
        current_sum = nums[i]+nums[j]
        results = []
        if sum(nums[:2]) > target:
            return results
        if sum(nums[-2:]) < target:
            return results
        while i<j:
            current_sum = nums[i]+nums[j]

            if current_sum==target:
                results.append([nums[i], nums[j]])
                i +=1
                j -=1 # Since we dont need to care the duplicatesd, speed up 689 ms
            elif current_sum < target:
                i += 1
            else:
                j -= 1
        return results

class Solution4(Solution):

    def two_sum(self, nums, target):
        # assume nums is sorted
        n = len(nums)
        i = 0
        j = n-1
        results = []
        if sum(nums[:2]) > target:
            return results
        if sum(nums[-2:]) < target:
            return results
        while i<j:
            current_sum = nums[i]+nums[j]
            print('current_sum', current_sum,nums[i], nums[j], i,j)

            if current_sum==target:
                results.append([nums[i], nums[j]])
                i +=1
                while i < j and nums[i] == nums[i-1]:
                    i += 1
                j -=1
                while i<j and nums[j]==nums[j+1]:
                    j -= 1
            elif current_sum < target:
                i += 1

            else:
                j -= 1

        return results


class Solution5:
    def fourSum(self, nums, target):
        def findNsum(l, r, target, N, result, results):
            if r-l+1 < N or N < 2 or target < nums[l]*N or target > nums[r]*N:  # early termination
                return
            if N == 2: # two pointers solve sorted 2-sum problem
                results += [result+x for x in self.two_sum(l,r,nums, target)]
            else: # recursively reduce N
                for i in range(l, r+1):
                    if i == l or (i > l and nums[i-1] != nums[i]):
                        findNsum(i+1, r, target-nums[i], N-1, result+[nums[i]], results)

        nums.sort()
        results = []
        findNsum(0, len(nums)-1, target, 4, [], results)
        return results

    def two_sum(self,l,r, nums, target):
        results =[]
        while l < r:
            s = nums[l] + nums[r]
            if s == target:
                results.append([nums[l], nums[r]])
                l += 1
                while l < r and nums[l] == nums[l-1]:
                    l += 1
                r -=1
                while l<r and nums[r] ==nums[r+1]:
                    r -= 1
            elif s < target:
                l += 1
            else:
                r -= 1
        return results

class Solution6(Solution5):
    def two_sum(self,l,r, nums, target):
        is_even = target %2==0
    def two_sum_even(self, nums, target):

        results =[]
        while l < r:
            s = nums[l] + nums[r]
            if s == target:
                results.append([nums[l], nums[r]])
                l += 1
                while l < r and nums[l] == nums[l-1]:
                    l += 1
                r -=1
                while l<r and nums[r] ==nums[r+1]:
                    r -= 1
            elif s < target:
                l += 1
            else:
                r -= 1
        return results

if __name__ == '__main__':
    nums = [1,0,-1,0,-2,2]
    nums = [-1,0,-5,-2,-2,-4,0,1,-2]
    nums = [-2,-1,-1,1,1,2,2]
    target  = 0
    target = -9
    target = 0
    s = Solution5()
    y = s.fourSum(nums=nums,target=target)
    print(y)