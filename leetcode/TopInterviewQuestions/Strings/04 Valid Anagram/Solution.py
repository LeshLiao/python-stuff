class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_dictionary = self.calculate_letter(s)
        t_dictionary = self.calculate_letter(t)

        for key in s_dictionary:
            # print(key, '->', s_dictionary.get(key))
            # print(key, '->', t_dictionary.get(key))
            if s_dictionary.get(key) != t_dictionary.get(key):
                return False

        for key in t_dictionary:
            # print(key, '->', s_dictionary.get(key))
            # print(key, '->', t_dictionary.get(key))
            if s_dictionary.get(key) != t_dictionary.get(key):
                return False

        return True

    def calculate_letter(self, temp: str) -> dict:

        my_dictionary = {}
        for element in temp:
            val = my_dictionary.get(element)
            if val != None:
                sum = int(val) + 1
                my_dictionary.update({element: str(sum)})
            else:
                my_dictionary.update({element: "1"})

        return my_dictionary


s = Solution()
ans = s.isAnagram("anagram", "nagaram")
print("ans:"+str(ans))
print("expect: True")

ans = s.isAnagram("rat", "car")
print("ans:"+str(ans))
print("expect: False")

'''
Reference youtube:
https://www.youtube.com/watch?v=9UtInBqnCgA&list=PLot-Xpze53lfQmTEztbgdp8ALEoydvnRQ&ab_channel=NeetCode
'''
