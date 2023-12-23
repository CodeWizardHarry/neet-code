class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """

   # [a,bb,cccc]
   # 1!a2!bb4!cccc
    def encode(self, strs):
        res = ''
        for s in strs:
            res = res + str(len(s)) + "!" + s
        return res

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str):
        # write your code here
        print(str)
        i = 0
        res = []
        print(len(str))
        while i < len(str):
            word = str[i+2:i+2+int(str[i])]
            print(word)
            i = i+2+int(str[i])  
            print(i)  
            res.append(word)

        return res


###########################################################################



#solution 2

class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
   # [a,bb,cccc]
   # 1!a2!bb4!cccc
    def encode(self, strs):
        res = ''
        for s in strs:
            res = res + str(len(s)) + "!" + s
        return res


    def decode(self, str):
        i = 0
        res = []
        while i < len(str):
            j = i 
            while str[j] != '!':
                j += 1
            
            length = int(str[i:j])
            word = str[j+1:j+length+1] 
            print(word)
            res.append(word)
            i = j+1+length
        return res

 