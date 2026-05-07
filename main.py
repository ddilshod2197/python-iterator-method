class Iterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

class MyIterable:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return Iterator(self.data)

my_iterable = MyIterable([1, 2, 3, 4, 5])
for item in my_iterable:
    print(item)
```

```python
class MyIterable:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return iter(self.data)

my_iterable = MyIterable([1, 2, 3, 4, 5])
for item in my_iterable:
    print(item)
