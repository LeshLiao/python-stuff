class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        my_str_list = list(str(x))

        if my_str_list[0] == '-':
            del my_str_list[0]
            sign = -1

        # my_str_list[:] = my_str_list[::-1]
        my_str_list.reverse()
        s = ''.join(my_str_list)

        ret = int(s) * sign

        if ret > (pow(2, 31)-1) or ret < (pow(2, 31) * -1):
            return 0

        return ret


s = Solution()
ans = s.reverse(123)
print(ans)
print("expect: 321")

ans = s.reverse(1534236469)
print(ans)
print("expect: 0")

ans = s.reverse(-2147483412)
print(ans)
print("expect: -2143847412")

""" What did we learn
pow()
Go over question clearly
    limitation on output x not input x.
"""
