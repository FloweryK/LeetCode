class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # scan digit-logs and store them separately
        ## how to scan: split and examine .isalpha()
        letters, digits = [], []
        
        for log in logs:
            log = log.split(' ')
            identifier, words = log[0], ' '.join(log[1:])
            
            if words[0].isalpha():
                letters.append((identifier, words))
            else:
                digits.append((identifier, words))
            
        # sort letters with two conditions
        letters = sorted(letters, key=lambda x: (x[1], x[0]))
        
        # join all contents
        digits = [' '.join(t) for t in digits]
        letters = [' '.join(t) for t in letters]
        
        return letters + digits
        