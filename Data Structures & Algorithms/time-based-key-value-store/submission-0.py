class TimeMap:

    def __init__(self):
        self.m = {} # key : [(time, val)]

    def set(self, key: str, value: str, timestamp: int) -> None:
        val = self.m.get(key, [])
        val.append((timestamp, value))
        self.m[key] = val

    def get(self, key: str, timestamp: int) -> str:
        val_list = self.m.get(key, [])
        if val_list == []: return ""
        low, high = 0, len(val_list) - 1
        while low <= high:
            mid = (low + high) // 2
            if val_list[mid][0] == timestamp:
                return val_list[mid][1]
            elif val_list[mid][0] < timestamp:
                low = mid + 1
            else:
                high = mid - 1
        if high >= 0:
            return val_list[high][1]
        else:
            return ""
        
        

