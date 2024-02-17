class Solution:
    def isHappy(self, n: int) -> bool:
        """
        steps:
        1. write code that runs the process as outlined in the explanation
        2. use a set to track the numbers we have seen
        3. break the loop when a number has appeared twice
        """

        def recursive_call(n, seen_numbers):
            res = 0 
            for num in str(n):
                res += int(num)**2
            if res == 1:
                return True
            if res in seen_numbers:
                return False
            seen_numbers.add(res)
            
            return recursive_call(res,seen_numbers)
            
        return recursive_call(n, set())