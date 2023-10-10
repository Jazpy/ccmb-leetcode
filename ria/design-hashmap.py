# https://leetcode.com/problems/design-hashmap/
# 2247ms
# 16.54MB


class MyHashMap(object):

    def __init__(self):
        self.map = []
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        key_present = False
        for pair in self.map:
            if key == pair[0]:
                pair[1] = value
                key_present = True
        if key_present is False:
            self.map.append([key, value])
        
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """

        key_present = False
        for pair in self.map:
            if key == pair[0]:
                return pair[1]
        return -1

        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        i = 0
        for pair in self.map:
            if key == pair[0]:
                self.map.pop(i)
            i+=1
        
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

