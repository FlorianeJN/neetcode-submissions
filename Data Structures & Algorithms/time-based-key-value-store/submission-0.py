class TimeMap:
    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.store[key]
        low = 0
        high = len(values) - 1
        value = ""

        while low <= high:
            mid = low + ((high - low) // 2)
            if values[mid][0] <= timestamp:
                value = values[mid][1]
                low = mid + 1
            else:
                high = mid - 1
        
        return value

