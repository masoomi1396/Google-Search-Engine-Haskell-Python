def linear_pairs(word_table, key): # Using Linear Search From the Assignment to search through our list (Slower than Binary one) For example : "spank" took 7ms to search while in binary it was 0ms
    for counter in range(len(word_table)):
         if word_table[counter][0] == key:
             return len(word_table[counter][1])
    return -1

def binary_pairs(datas, target): # Using Binary Search From the Assignment to search through our list 
    start = 0
    end = len(datas) - 1
    while start <= end:
        middle = (start+end) // 2
        if datas[middle][0] == target:
            return middle
        elif datas[middle][0] < target:
            start = middle + 1
        else:
            end = middle - 1
    return -1