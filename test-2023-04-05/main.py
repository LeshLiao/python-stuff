
'''
a_text = "abcdefghijklmnopqrstuvwxyz"

Please define a func(a_text,N) such that:

	print (func(a_text,2))   ->  “aba”
	print (func(a_text,3))   ->  “abcba”
	print (func(a_text,4))   ->  “abcdcba”
'''

a_text = "abcdefghijklmnopqrstuvwxyz"


def func(a_text, num):
    str = a_text[:num]
    reversed = str[::-1]
    reversed1 = reversed[1:]
    str = str + reversed1
    return str


print(func(a_text, 2))
print(func(a_text, 3))
print(func(a_text, 4))
