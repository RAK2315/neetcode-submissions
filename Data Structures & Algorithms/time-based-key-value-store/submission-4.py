class TimeMap:

    def __init__(self):
        self.di = {} # form: {key:[(timestamp,value), (timestamp2,value2)]}

        # also given timestampt 1 will be less then t2 always and so on t1<t2<t3...
        # so hint binary search
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.di:
            self.di[key]=[ (timestamp,value) ]
        else:
            self.di[key].append((timestamp,value))


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.di: return ""

        arr = self.di[key] # [ (t1,v1), (t2,v2) ]
        target = timestamp
        
        left ,right = 0, len(arr) - 1


        while left <= right:
            mid = (left+right)//2

            if arr[mid][0] == target:
                return arr[mid][1]
            
            elif arr[mid][0] < target:
                left = mid + 1
            else: right = mid - 1
        

        # ex: [(3,a),(4,b),(5,c)], target tstamp = 2
        # so right would keep decreasing till final loop makes it -1
        if right == -1: return "" 

        # otherwise
        # ex: [(3,a),(4,b),(6,c)], target tstamp = 5 
        # output: b
        return arr[right][1]
        




        