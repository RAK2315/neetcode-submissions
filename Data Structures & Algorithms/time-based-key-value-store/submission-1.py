class TimeMap:

    def __init__(self):
        self.di = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        k = (key,timestamp)
        self.di[k] = value


    def get(self, key: str, timestamp: int) -> str:
        timestamp_prev = timestamp
        while timestamp_prev > -1:
            k = (key,timestamp_prev)
            if k in self.di:
                return self.di[k]
            else:
                timestamp_prev-=1
        return ""



        
