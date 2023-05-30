#include <vector>
#include <list>
#include <memory>
#include <algorithm>

using std::vector;
using std::list;
using std::unique_ptr;

class MyHashSet {
private:
    size_t hash_range, used, load;
    double load_factor;
    vector<unique_ptr<list<int>>> arr;

    // https://stackoverflow.com/a/12996028
    size_t hash(unsigned int key) {
        key  = ((key >> 16) ^ key) * 0x45d9f3b;
        key  = ((key >> 16) ^ key) * 0x45d9f3b;
        return ((key >> 16) ^ key) % hash_range;
    }

    void fast_add(int key) {
        size_t hashed = hash(key);

        // First time adding to bucket
        if (arr[hashed] == nullptr)
            arr[hashed] = make_unique<list<int>>(1, key);
        else
            arr[hashed]->push_back(key);
    }

    void rehash() {
        vector<unique_ptr<list<int>>> old_arr(hash_range * 2);
        old_arr.swap(arr);

        hash_range *= 2;
        load        = hash_range * load_factor;

        for (auto &p : old_arr) {
            if (p == nullptr)
                continue;

            for (auto &k : *p)
                fast_add(k);
        }
    }

public:
    MyHashSet() : hash_range(100), used(0), load_factor(0.75),
        load(hash_range * load_factor), arr(hash_range) {}

    void add(int key) {
        size_t hashed = hash(key);

        // First time adding to bucket
        if (arr[hashed] == nullptr) {
            arr[hashed] = make_unique<list<int>>(1, key);
        // Collision
        } else {
            arr[hashed]->push_back(key);
        }

        ++used;

        // Check if we need to rehash
        if (used > load)
            rehash();
    }

    void remove(int key) {
        size_t hashed = hash(key);

        if (arr[hashed] == nullptr)
            return;

        arr[hashed]->remove(key);
    }

    bool contains(int key) {
        size_t hashed = hash(key);

        if (arr[hashed] == nullptr)
            return false;

        return (std::find(arr[hashed]->begin(),
            arr[hashed]->end(), key) != arr[hashed]->end());
    }
};
