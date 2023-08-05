class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True

        # turn into lowercase
        new_str = self.letters(s).lower()
        # print("new_str:"+new_str)
        half_length = int(len(s)/2)
        # print("half_length:" + str(half_length))
        # print("Front str:"+new_str[0:half_length])
        temp = new_str[-half_length:]
        # print("Tail str:"+temp[::-1])

        # cut half and compare string
        if new_str[0:half_length] == temp[::-1]:
            return True
        return False

    def letters(self, input):
        return ''.join(filter(str.isalnum, input))


s = Solution()

ans = s.isPalindrome("0P")
print("ans:"+str(ans))
print("expect: False")

ans = s.isPalindrome("A man, a plan, a canal: Panama")
print("ans:"+str(ans))
print("expect: True")

ans = s.isPalindrome("race a car")
print("ans:"+str(ans))
print("expect: False")

ans = s.isPalindrome(" ")
print("ans:"+str(ans))
print("expect: True")
