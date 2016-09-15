def go_until(seq):
    pos = 0
    for i in range(len(seq)):
        if seq[i] >= 0:
            pos += seq[i]
        else:
            return pos,i
    return pos,-1

seq = [2,-1,2,3,4]

print(go_until(seq))

pos,i = go_until(seq)

print(go_until(seq[i:]))
