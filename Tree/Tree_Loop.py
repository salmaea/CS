def tree(h):
    T =''
    if (h == 0):
        return T

    elif (h < 0):
        T = T + (abs(h)-1)*' ' + '*' + (abs(h)-1)*' ' + '\n'
        s = 0
        for i in range(abs(h),0,-1):
            T = T + (s)*' ' + (2*i-1)*'*' + s*' ' + '\n'
            s = s + 1
    else:
        s = abs(h)-1
        for i in range(1, h+1):
            T = T + s*' ' + (2*i-1)*'*' + s*' ' + '\n'
            s = s - 1
        T = T + (h-1)*' ' + '*' + (h-1)*' '
    return T
