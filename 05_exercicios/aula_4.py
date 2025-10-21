def perms(l, pos=0):
    if pos == len(l)-1:
        print(l)
    else:
        for i in range(pos, len(l)):
            l[i], l[pos] = l[pos], l[i]
            perms(l, pos+1)
            l[i], l[pos] = l[pos], l[i]

def perms_2(l, pos=0):
    if pos == len(l)-1:
        return l[:]
    else:
        result = []
        for i in range(pos, len(l)):
            l[i], l[pos] = l[pos], l[i]
            result += perms(l, pos+1)
            l[i], l[pos] = l[pos], l[i]
        return result

