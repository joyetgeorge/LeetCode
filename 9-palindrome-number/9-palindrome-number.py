class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverse = 0
        num = x
        while num > 0 :
            reminder = num % 10
            reverse = (reverse * 10) + reminder
            num = num // 10
        return x == reverse