#!/bin/python
# -*- coding: utf8 -*-
import sys
import os
import re

class Solution:
    def calcSumOfOnlyOne(self, arr):
        s = set()
        result = 0
        for num in arr:
            if num in s:
                result -= num
            else:
                result += num

            s.add(num)

        return result

_arr_cnt = 0
_arr_cnt = input()
_arr = list(map(int, sys.stdin.readline().strip().split()))

  
s = Solution()
res = s.calcSumOfOnlyOne(_arr)

print(str(res) + "\n")