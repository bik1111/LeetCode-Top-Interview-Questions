from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        # for 루프의 range 함수는 세 개의 인자를 받습니다: 시작(start), 끝(stop), 그리고 스텝(step)
        # -1 (끝 값): 이 부분은 루프의 끝을 나타냅니다. -1은 루프가 0까지 도달할 때까지 계속됨을 의미합니다. 즉, 가장 낮은 자릿수에 도달할 때까지 반복합니다.

        for i in range(len(digits)-1, -1, -1):
            if digits[i] == 9:
                # 올림 처리
                digits[i] = 0
            else:
                digits[i] = digits[i] + 1
                return digits
        return [1] + digits


myObj = Solution()
myObj.plusOne([9, 9, 9])
