class add_find:

    def __init__(self):
        self.array={}
        self.hashset=set()

    def add(self,value):

        ### we add values using a dictionary
        ##  time complexity O(1)
        if value not in self.hashset:
            
            self.array[value]=1
            
            self.hashset.add(value)
        
        self.array[value]+=1

    def find(self,target):
        ## time O(n)
        for values in self.array:

            self.array[values]-=1

            if self.array[values]<1: self.hashset.remove(values)

            if target - values in self.hashset: return True

            self.array[values]+=1
            self.hashset.add(values)

        return False




#### testing example

arr=add_find()

arr.add(3)
arr.add(1)
arr.add(2)

print(arr.find(3))
            







    