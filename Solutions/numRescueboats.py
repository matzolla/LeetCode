class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        time complexity O(n+nlogn)
        space complexity O(1)
        """

        left=0
        right=len(people)-1
        num_boats=0
        people.sort()

        while left<=right:

            if people[left]+people[right]<=limit:
                num_boats+=1

                left+=1
                right-=1
            elif people[left]+people[right]>limit:
                right-=1

                num_boats+=1
        
        return num_boats
