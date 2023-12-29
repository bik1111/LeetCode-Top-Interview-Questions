# URL : https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/?envType=featured-list&envId=top-interview-questions?envType=featured-list&envId=top-interview-questions

class Solution(object):
    def strStr(self, haystack, needle):
        # needle이 haystack보다 애초에 긴 문자열이면 "-1" 반환
        # 1을 더해주는 이유는 문자열 크기가 동일한 경우, 인덱스 0은 계산해줘야 하기 때문.
        for i in range(len(haystack) - len(needle) + 1):
            # 인덱스를 돌며 해당 인덱스부터 needle의 길이만큼의 문자열이 haystack에 있는지 확인
            if haystack[i : i+len(needle)] == needle:
                # 만약 hasystack에 needle이 있다면 해당 인덱스 반환
                return i
        # 그렇지 않다면 "-1" 반환
        return -1




myObj = Solution()
result = myObj.strStr("iloveyou", "vey")