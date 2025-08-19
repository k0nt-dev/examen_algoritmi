# Problema 3 – Căutare într-o matrice sortată (15p)

from typing import List

def search_sorted_matrix(mat: List[List[int]], x: int) -> bool:
    if not mat or not mat[0]:
        return False

    n, m = len(mat), len(mat[0])
    i, j = 0, m - 1  # incepe din primul numar (dreapta sus)

    while i < n and j >= 0:
        val = mat[i][j]
        if val == x:
            return True
        elif val > x:
            # daca "val" este mai mare se muta la stanga
            j -= 1
        else:
            # daca "val" este mai mic se muta la dreapta
            i += 1

    return False

if __name__ == "__main__":
    mat = [
        [1, 4, 7],
        [2, 5, 9],
        [3, 6, 10]
    ]
    print(search_sorted_matrix(mat, 5))  # True
