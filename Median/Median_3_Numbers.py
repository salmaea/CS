#Median of 3
print("hello")
def median3(a,b,c):
    if (a<b and b<c) or (b>c and b<a) or (b==a) or (b==c):
        return b
    elif (b<a and a<c) or (c<a and a<b) or (a==b) or (a==c):
        return a
    else:
        return c
print(median3(100,3,1000)
