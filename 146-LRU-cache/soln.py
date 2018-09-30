class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.data = collections.OrderedDict()
        self.capacity = capacity


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.data:
            val = self.data.pop(key)
            self.data[key] = val
            return val
        else:
            return -1


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.data:
            val = self.data.pop(key)
            self.data[key] = value
            return val
        else:
            if len(self.data) >= self.capacity:
                to_be_removed = next(iter(self.data))
                self.data.pop(to_be_removed)
            self.data[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
