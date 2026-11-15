class Solution:
    def countConsistent(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0

        for i in range(n):
            min_value = nums[i]
            and_value = nums[i]

            for j in range(i, n):
                and_value &= nums[j]
                min_value = min(min_value, nums[j])

                if and_value == min_value:
                    count += 1

        return count