class Solution {
public:
    int minFlips(int a, int b, int c) {
        int o = a | b;
        int d = o ^ c;

        // Get number of 0s that should've been 1s
        int ret = __builtin_popcount((~o) & d);

        // Places where we have a 1 and need a 0
        int m = o & d;
        ret += __builtin_popcount(a & m);
        ret += __builtin_popcount(b & m);

        return ret;
    }
};