def go_until(seq):
    L = []
    count = 0
    i = 0
    while i < len(seq):
        while seq[i] >= 0:
            count += seq[i]
            i += 1
            if i >= len(seq):
                break
        L.append(count)
        count = 0
        if i >= len(seq):
            break
        while seq[i] < 0:
            count += seq[i]
            i += 1
            if i >= len(seq):
                break
        L.append(count)
        count = 0
    return L

def find_max(seq):
    pass
seq = [2,-1,2,3,4,-5]
seq2 = [2,-3,5,-4,8,-5,7,-1,6]

print(go_until(seq))
print(go_until(seq2))
