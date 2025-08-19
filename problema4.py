# Problema 4 – Stivă (20p)

class Stack:
    def __init__(self):
        self._data = []

    def push(self, x):
        self._data.append(x)
        pass

    def pop(self):
        if not self._data:
            raise IndexError("stiva este goala")
        return self._data.pop()
        pass

    def peek(self):
        if not self._data:
            raise IndexError("peek din stiva goala")
        return self._data[-1]
        pass

    def __repr__(self):
        return f"Stack({self._data})"

if __name__ == "__main__":
    s = Stack()
    s.push(5)
    s.push(7)
    s.pop()
    s.push(9)
    print(s.peek())  # 9
    print(s)
