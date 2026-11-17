import collections

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0
        self.key_to_freq = {} 
        self.freq_to_keys = collections.defaultdict(collections.OrderedDict) 

    def _update(self, key: int, new_value: int = None) -> int:
        freq = self.key_to_freq[key]
        val = self.freq_to_keys[freq].pop(key)
        if new_value is not None:
            val = new_value
        if not self.freq_to_keys[freq] and self.min_freq == freq:
            self.min_freq += 1
        self.key_to_freq[key] = freq + 1
        self.freq_to_keys[freq + 1][key] = val
        return val

    def get(self, key: int) -> int:
        if key not in self.key_to_freq:
            return -1
        return self._update(key)

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.key_to_freq:
            self._update(key, value)
        else:
            if len(self.key_to_freq) == self.capacity:
                evict_key, _ = self.freq_to_keys[self.min_freq].popitem(last=False)
                del self.key_to_freq[evict_key]
            self.key_to_freq[key] = 1
            self.freq_to_keys[1][key] = value
            self.min_freq = 1