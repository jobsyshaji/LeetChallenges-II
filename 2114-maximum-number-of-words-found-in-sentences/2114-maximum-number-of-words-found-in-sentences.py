class Solution(object):
    def mostWordsFound(self, sentences):
        total_words = []

        for i in sentences:
          
            for j in i:
                words = i.split()
                x = len(words)
               
                total_words.append(x)
            max_word = max(total_words)

        return max_word      
       
        
            
        

      
    
    
        