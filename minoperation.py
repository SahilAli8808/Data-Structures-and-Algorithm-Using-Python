def minOperation(s): 
        #code here
        """
        abcabca
        a
        a-->next element?a:next
        ab?nextelement is current string?current sting : current element
        
        
        """
        count =0
        current_string = ""
        for i in range(len(s)):
            if s[i] not in current_string:
                current_string += s[i]
                print(current_string ,"-->")
                count += 1
                print(count)
            else:
                current_string = s[i]
        return count
print(minOperation("nnlnnlfd"))