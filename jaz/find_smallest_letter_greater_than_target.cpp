class Solution {
public:
    char nextGreatestLetter(vector<char> &letters, char target) {
        int low = 0;
        int hi  = letters.size() - 1;
        int mid = hi / 2;

        while (low < hi) {
            if (letters[mid] > target)
                hi  = mid - 1;
            else if (letters[mid] < target)
                low = mid + 1;
            else
                break;

            mid = low + (hi - low) / 2;
        }

        while (mid < letters.size() && letters[mid] <= target)
            ++mid;

        return letters[mid >= letters.size() ? 0 : mid];
    }
};