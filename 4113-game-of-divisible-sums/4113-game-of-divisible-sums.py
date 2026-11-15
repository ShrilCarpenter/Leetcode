class Solution:
    def maxDifference(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [0] * (n + 1)
        dp[n - 1] = nums[n - 1]

        for i in range(n - 2, -1, -1):
            s1 = nums[i]
            s2 = s1 + nums[i + 1]
            dp[i] = max(
                s1 + (dp[i + 1] if s1 % 3 else -dp[i + 1]),
                s2 + (dp[i + 2] if s2 % 3 else -dp[i + 2]),
            )

        return dp[0]