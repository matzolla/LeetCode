def pow(x,n):
    """ calculate x pow n
    Arguments:
    x -- number
    n -- integer pow
    """

    if n<0:
        x=1/x

    n=abs(n)
    pow=1
    while n:
        if (n & 1)!=0:
            pow*=x
        
        x*=x
        n>>=1
       
    
    return pow

# pow=1,x=4 n=5
# pow=4, x=16,n=2
# pow=4, x=256, n=1
print(pow(2,300))
