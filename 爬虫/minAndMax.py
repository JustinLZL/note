# -*- coding: utf-8 -*-
from __future__ import unicode_literals


def startAndEnd(L, start, end):
    if end - start <= 1:
        return (max(L[start], L[end]),
                min(L[start], L[end]))
    else:
        max1, min1 = startAndEnd(L, start, (start + end) // 2)
        max2, min2 = startAndEnd(L, (start + end) // 2 + 1, end)
        print(max(max1, max2), min(min1, min2))
        return max(max1, max2), min(min1, min2)


def minAndMax(L):
    assert(type(L) == type([]) and len(L) > 0)
    maxV, minV = startAndEnd(L, 0, len(L) - 1)
    return maxV, minV

L = [5, 8, 7, 4,12,3,5,4,8,5,-20,1,7,3, 1, -9]
assert(minAndMax(L) == (8, -9))
