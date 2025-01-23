
class HashTableChaining:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        for item in self.table[index]:
            if item[0] == key:
                item[1] = value  # Update value if key exists
                return
        self.table[index].append([key, value])

    def search(self, key):
        index = self.hash_function(key)
        for item in self.table[index]:
            if item[0] == key:
                return item[1]
        return None

    def delete(self, key):
        index = self.hash_function(key)
        for i, item in enumerate(self.table[index]):
            if item[0] == key:
                del self.table[index][i]
                return True
        return False

    def display(self):
        for i, items in enumerate(self.table):
            print(f"Index {i}: {items}")


# Example usage
if __name__ == "__main__":
    hash_table = HashTableChaining(10)
    hash_table.insert(1, "Value 1")
    hash_table.insert(11, "Value 11")
    hash_table.insert(21, "Value 21")
    print("Hash Table after insertions:")
    hash_table.display()

    print("Search for key 11:", hash_table.search(11))
    hash_table.delete(11)
    print("Hash Table after deletion of key 11:")
    hash_table.display()
