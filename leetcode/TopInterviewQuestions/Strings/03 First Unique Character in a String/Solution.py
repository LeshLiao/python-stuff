class Solution:
    def firstUniqChar(self, s: str) -> int:
        myDictionary = {}
        for element in s:
            val = myDictionary.get(element)
            if val != None:
                sum = int(val) + 1
                myDictionary.update({element: str(sum)})
            else:
                myDictionary.update({element: "1"})

        # print(myDictionary.items())

        singleKey = ""
        for key in myDictionary:
            # print(key, '->', myDictionary[key])
            if myDictionary[key] == '1':
                singleKey = key
                break

        ret = 0
        for element in s:
            # print(singleChar)
            # print(element)
            if element == singleKey:
                return ret
            ret = ret + 1
        return -1


s = Solution()
ans = s.firstUniqChar("leetcode")
print("ans:"+str(ans))
print("expect: 0")


ans = s.firstUniqChar("loveleetcode")
print("ans:"+str(ans))
print("expect: 2")


ans = s.firstUniqChar("aabb")
print("ans:"+str(ans))
print("expect: -1")
