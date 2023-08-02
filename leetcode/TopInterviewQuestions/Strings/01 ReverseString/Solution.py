from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        half_length = int(len(s)/2)
        for i in range(0, half_length):
            temp = s[i]
            tail_index = i*(-1)-1
            s[i] = s[tail_index]
            s[tail_index] = temp
            pass


a = Solution()
message = "WhatIsThis"
message_to_list = list(message)
a.reverseString(message_to_list)
print(message_to_list)

""" What did we learn
str and List is different.
What does in-place mean?
"""
