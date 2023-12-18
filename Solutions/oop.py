class metric:

    def __init__(self,x,y):

        self.x=x
        self.y=y

    def subtract(self):

        """perform element wise subtraction bewtween two vectors
        output   -- vector (list)
        Arguments -- vector x (list), vector y (list)
        """

        result=[]

        for idx in range(len(self.x)):

            result.append(self.x[idx]-self.y[idx])


        return result


    def multiply(self,x,y):

        """perform element wise multiplication bewtween two vectors
        output   -- vector (list)
        Arguments -- vector x (list), vector y (list)
        """

        result =[]

        for idx in range(len(x)):

            result.append(x[idx]*y[idx])

        return result

    
    def sum(self,x):

        """perform element wise addition along the axis of a vector
        output   -- scalar
        Arguments -- vector x (list)
        """

        sum_array=0 

        for idx in range(len(x)):

            sum_array+=x[idx]

        return  sum_array

    def square_root(self,x):

       """compute the square root of the value x
        output   -- scalar
        Arguments -- scalar x
        """

       return x**(0.5)


class Euclidean(metric):

    def __init__(self,x,y):
        
        super().__init__(x,y)

    
    def norm(self):

        subtract_vector= self.subtract()

        multiply_vector= self.multiply(subtract_vector,subtract_vector)

        sum_vector= self.sum(multiply_vector)


        return self.square_root(sum_vector)

## Test case
vector1=[2,3,4]
vector2=[1,2,2]

compute= Euclidean(vector1,vector2)


print(compute.norm())

