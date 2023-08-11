'''
Given a string s, find the first non-repeating character in it and return its index.
If it does not exist, return -1.

Example 1:
Input: s = "arlo"
Output: 0

Example 2:
Input: s = "testautomation"
Output: 1

Example 3:
Input: s = "aabb"
Output: -1

'''


def test(s):
    temp = list(s)
    temp[0] = ''
    print(temp)


def get_non_repeating_character(s):
    ans = -1
    for index, item in enumerate(s):
        temp = list(s)
        target = temp[index]
        temp[index] = ''
        same = False
        for i in temp:
            if i == target:
                same = True

        if same == False:
            ans = index
            break

    return ans


def firstNonRepeatingChar(s):
    freq = {}
    for char in s:
        if char not in freq:
            freq[char] = 1
        else:
            freq[char] += 1

    for i in range(len(s)):
        if freq[s[i]] == 1:
            return i

    return -1


str = 'aabb'

print(get_non_repeating_character(str))
print(firstNonRepeatingChar(str))

# test('aabb')
