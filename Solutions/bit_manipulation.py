class reverse_bit:
    """
    reversing a binary bit 
    time complexity O(1)
    """
    def __init__(self,n):
        self.n=n

    def reverse(self):

        res=0

        for i in range(32):

            bit=(self.n>>i)&1

            res=res|(bit<<(32-i))

        return  res


rev=reverse_bit(32)







