# Problema 1 – Merge Sort (20p)
# TODO: Implementați algoritmul Merge Sort și explicați complexitatea.

from typing import List

def merge_sort(a: List[int]) -> List[int]:
    def sort(l: int, r: int) -> None:
        if r - l <= 1:
            return
        m = (l + r) // 2
        sort(l, m)
        sort(m, r)
        i, j = l, m
        merged: List[int] = []
        while i < m and j < r:
            if a[i] <= a[j]:
                merged.append(a[i])
                i += 1
            else:
                merged.append(a[j])
                j += 1

        while i < m:
            merged.append(a[i])
            i += 1
        while j < r:
            merged.append(a[j])
            j += 1

        a[l:r] = merged

    sort(0, len(a))
    return a


if __name__ == "__main__":
    data = [5, 2, 8, 1, 3]
    print("input :", data)
    print("sorted:", merge_sort(data))
####################################################################################################
# Complexitatea algoritmului Merge Sort este O(n log n) in orice caz. Acest lucru inseamna ca
# algoritmul este eficient cu orice marime de date. (Am citit ca este utilizat cel mai mult la baze de date mari)

