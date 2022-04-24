class Solution:
    def reorderLogFiles(self, logs):
        lets = []
        digs = []
        
        for log in logs:
            s = log.split(' ')
            identifier = s[0]
            content = ' '.join(s[1:])
            
            if content[0][0].isalpha():
                lets.append((log, identifier, content))
            else:
                digs.append((log, identifier, content))
            
        lets = sorted(lets, key=lambda x: (x[2], x[1]))
        
        return [let[0] for let in lets] + [dig[0] for dig in digs]
