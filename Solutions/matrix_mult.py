class matmultiply:
    """
    time complexity O(n^3)
    """
    def __init__(self,A,B):
        self.A=A
        self.B=B

    def multiply(self):
        C= [[0 for row in len(self.A)]for col in len(self.A[0])]


        for idx in range(len(self.A)):
            for idy in range(len(self.A[0])):

                C[idx][idy]=0

                for idz in range(len(self.A)):

                    C[idx][idy]+=self.A[idx][idz]*self.B[idz][idy]

        

        return C