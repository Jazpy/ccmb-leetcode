class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        s = pref[0]
        ret = [pref[0]]

        for i in range(1, len(pref)):
            missing = pref[i] ^ s
            ret.append(missing)
            s ^= missing

        return ret