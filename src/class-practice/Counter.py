class Counter:
    def __init__(self):
        self.count = 0

    def increment(self) -> None:
        self.count += 1

    def get_value(self) -> int:
        return self.count
    
    def reset(self) -> None:
        self.count = 0

    def __str__(self):
        return f"Counter: {self.count}"
    
counter = Counter()
counter.increment()
counter.increment()
print(counter.get_value())  # 2
print(counter)  # Output: Counter: 2
counter.reset()
print(counter.get_value())  # 0
# Output: Current count: 2
# Output: Current count: 0
print(counter)  # Output: Counter: 0