from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        s[:] = s[::-1]
        # s.reverse()


a = Solution()
message = "ABCDE"
message_to_list = list(message)
a.reverseString(message_to_list)
print(message_to_list)
