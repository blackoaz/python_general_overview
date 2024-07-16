class HashMap:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        # Check if the key already exists and update the value
        for kv in self.table[index]:
            if kv[0] == key:
                kv[1] = value
                return
        # Otherwise, add the new key-value pair
        self.table[index].append([key, value])

    def get(self, key):
        index = self.hash_function(key)
        for kv in self.table[index]:
            if kv[0] == key:
                return kv[1]
        return None

    def __str__(self):
        return str(self.table)

# Example usage:
hash_map = HashMap()

hash_map.insert("key1", "value1")
hash_map.insert("key2", "value2")
hash_map.insert("key3", "value3")

print(hash_map.get("key1"))  # Output: value1
print(hash_map.get("key4"))  # Output: None

print(hash_map)
