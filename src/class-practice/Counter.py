class Counter:
    def __init__(self):
        self.count = 0

    def increment(self) -> None:
        self.count += 1

    def show(self) -> None:
        print(f"Current count: {self.count}")
    
    def reset(self) -> None:
        self.count = 0
    
counter = Counter()
counter.increment()
counter.increment()
counter.show()  # 2
counter.reset()
counter.show()  # 0
# Output: Current count: 2
# Output: Current count: 0