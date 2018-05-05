def combsort(input):
    gap = len(input)
    swaps = True
    while gap > 1 or swaps:
        gap = max(1, int(gap / 1.25))  # minimum gap is 1
        swaps = False
        for i in range(len(input) - gap):
            j = i+gap
            if input[i] > input[j]:
                input[i], input[j] = input[j], input[i]
                swaps = True

alist = [54,26,93,17,77,31,44,55,20]
combsort(alist)
print(alist)