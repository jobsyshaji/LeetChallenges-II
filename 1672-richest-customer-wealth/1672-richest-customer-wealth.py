class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
     
        maxw = []
        for i in accounts:
            total = 0
            for digits in i:
                total = total + digits
                maxw.append(total)
            wealth = max(maxw)
        
        return wealth  
        
            
        
