import math
from collections import defaultdict

# Meh naive solution
class Solution:
    def __within(self, c, t, r):
        return math.dist(c, t) <= r

    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        bomb_dic = defaultdict(list)

        for i, main_bomb in enumerate(bombs):
            for j, sub_bomb in enumerate(bombs):
                if i == j:
                    continue
                if self.__within(main_bomb[:2], sub_bomb[:2], main_bomb[2]):
                    bomb_dic[i].append(j)

        ret = 0
        for i in range(len(bombs)):
            stk       = [i]
            total_det = set()

            while stk:
                exploding = stk.pop()
                total_det.add(exploding)

                for b in bomb_dic[exploding]:
                    if b not in total_det:
                        stk.append(b)

            ret = max(ret, len(total_det))
        
        return ret