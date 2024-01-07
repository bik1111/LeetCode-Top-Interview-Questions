class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        # 배열 dp를 생성하고 dp[i]는 i까지의 계단을 오르는 데의 경우의 수를 저장합니다.
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):

            # 현재 계단에 도달하는 방법은 (i-1)번째 계단에서 1 step을 오르는 방법과 (i-2)번째 계단에서 2 steps를 오르는 방법의 합과 같습니다.⭐️⭐️
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]

# Example usage:
myObj = Solution()
print(myObj.climbStairs(17))
print(myObj.climbStairs(3))


# 1 or 2 step 씩 오를 수 있음 (condition)
# 1step을 오르는 경우 (n-1): 현재 계단에서 1step을 오르면 i번째 계단 바로 "앞"에 도착
# 따라서 n번째 계단에 도달하는 방법의 수는 n-1번째 계단에 도달하는 경우의 수와 동일

# 2step을 오르는 경우 (n-2): 현재 계단에서 2step을 오르면 n-2번째 계단에 도착
# 따라서 n번째 계단에 도착하는 방법의 수는 n-2번째 계단에 도달하는 방법의 수와 동일



