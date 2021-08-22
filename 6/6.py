class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 팰린드롬 판별 및 투포인트 확장처리
        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -=1
                right += 1
            return s[left + 1:right]
        # 해당사항이 없으면 빠르게 종료
        if len(s) < 2 or s == s[::-1]:
            return s
        
        result = ''
        # 슬라이딩 윈도우를 우측으로 이동시키기.
        for i in range(len(s) - 1):
            # 문자열 길이가 제일 긴 친구를 골라내기.
            result = max(result, expand(i, i + 1), expand(i, i + 2), key=len)
            
        return result
