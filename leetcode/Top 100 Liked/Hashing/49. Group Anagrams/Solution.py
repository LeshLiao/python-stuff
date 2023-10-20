import os
import sys
import unittest
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashmap = {}
        ret_list = []

        for str in strs:
            sorted_str = ''.join(sorted(str))
            if sorted_str in hashmap:
                # ret_list[hashmap[sorted_str]].append(str)
                ret_list[hashmap.get(sorted_str)].append(str)
            else:
                index = len(ret_list)
                hashmap[sorted_str] = index
                ret_list.append([str])

        return ret_list

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_ex_1(self):
        strs = ["eat","tea","tan","ate","nat","bat"]

        expected = [["bat"],["nat","tan"],["ate","eat","tea"]]
        my_expected = [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
        self.assertEqual(self.s.groupAnagrams(strs), my_expected)

    def test_ex_2(self):
        strs = [""]
        expected = [[""]]
        self.assertEqual(self.s.groupAnagrams(strs), expected)

    def test_ex_3(self):
        strs = ["a"]
        expected = [["a"]]
        self.assertEqual(self.s.groupAnagrams(strs), expected)

if __name__ == '__main__':
    unittest.main()