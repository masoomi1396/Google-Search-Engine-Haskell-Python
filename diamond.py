def mergeSort(data):
    # Doing merge sort from the psuedo code 
    if len(data) <= 1 :
        return data[:]
    else:
        m = len(data) // 2
        fst = mergeSort(data[:m])
        snd = mergeSort(data[m:])
        res = []
        fi = 0
        si = 0
        while  0 <= fi < len(fst) and 0 <= si < len(snd):
            if fst[fi] < snd[si]:
                res.append(fst[fi])
                fi += 1
            else :
                res.append(snd[si])
                si += 1
        while 0 <= fi < len(fst):
            res.append(fst[fi])
            fi += 1
        while 0 <= si < len(snd):
            res.append(snd[si])
            si += 1
    return res


def mergeDict (datas):
    # Using hashTable, and using the word (the one searching) as the key and the files as items
    dictionary = {}
    for counter in range(len(datas)):
        if datas[counter][0] in dictionary : # removing duplicated 
            if datas[counter][1] not in dictionary[datas[counter][0]]:
                dictionary[datas[counter][0]].append(datas[counter][1])
        else: # Add new items to hashTable
            dictionary[datas[counter][0]] = [datas[counter][1]]
    return(dictionary)

def make_table(pairs):
    data = mergeSort(pairs)
    data = mergeDict(data)
    return list(data.items()) # Transfering dictionary (HashTable) to list