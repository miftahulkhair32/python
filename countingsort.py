def counting_sort(array1, max_val):
    m = max_val + 1
    count = [0] * m                
    
    for a in array1:
    # count occurences
        count[a] += 1             
    i = 0
    for a in range(m):            
        for c in range(count[a]):  
            array1[i] = a
            i += 1
    return array1

print(counting_sort( [8, 10, 7, 11, 9, 1, 4, 6, 3, 5, 2], 11 ))
# ini sorting yang terbatas jumlah max
