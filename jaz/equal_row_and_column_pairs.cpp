#include <sstream>
#include <unordered_map>
#include <string>
#include <iostream>

using std::vector;
using std::stringstream;
using std::unordered_map;
using std::string;

class Solution {
public:
    int equalPairs(vector<vector<int>>& grid) {
        // Hash all rows
        unordered_map<string, int> rows;
        for (const auto &v : grid) {
            stringstream ss;

            for (auto e : v)
                ss << e << ",";

            if (rows.find(ss.str()) == rows.end())
                rows[ss.str()] = 1;
            else
                ++rows[ss.str()];
        }

        // Hash columns and compare to rows
        int ret = 0;
        for (size_t i = 0; i != grid[0].size(); ++i) {
            stringstream ss;

            for (size_t j = 0; j != grid.size(); ++j)
                ss << grid[j][i] << ",";

            auto it = rows.find(ss.str());
            if (it != rows.end())
                ret += it->second;
        }

        return ret;
    }
};