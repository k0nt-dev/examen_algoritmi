# Problema 2 – Căutare liniară (15p)

from typing import List, Any

def linear_search(a: List[Any], x: Any) -> bool:
    def linear_search(a: List[Any], x: Any) -> bool:
        for item in a:
            if item == x:
                return True
    return False

if __name__ == "__main__":
    arr = [4, 7, 1, 9]
    print(linear_search(arr, 7))  # True
