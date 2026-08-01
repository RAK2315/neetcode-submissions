class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

    def get(self, key: int) -> int:
        if key in self.cache:
            # delete and add the key again so that it becomes them most recent key
            value = self.cache[key]
            del self.cache[key]
            self.cache[key] =  value

            return self.cache[key]
        return -1

        

    def put(self, key: int, value: int) -> None:
        # 1. if key exist, update value, delete and add again to make it most recent used
        if key in self.cache:
            del self.cache[key]

            self.cache[key] = value


        else:
            # 2. if key does not exist, remove least recently used key, ie
            # the key not used for longest time, which would be the first key
            if len(self.cache) == self.capacity:
                first_key = list(self.cache)[0]
                del self.cache[first_key]
            
            # add the key value pair
            self.cache[key] = value
        
        
