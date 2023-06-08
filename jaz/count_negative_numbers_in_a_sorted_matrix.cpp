class Solution {
public:
    int countNegatives(vector<vector<int>> &grid) {
        int col = 0;
        int ret = 0;

        for (int row = grid.size() - 1; row >= 0; --row) {
            while (col < grid[0].size() && grid[row][col] >= 0 && ++col);

            ret += grid[0].size() - col;
        }

        return ret;
    }
};