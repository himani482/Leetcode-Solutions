# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.
# class Solution:
#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#         d1 ={}
#         for i in magazine:
#             d1[i] =  d1.get(i,0) + 1
        
#         for i in ransomNote:
#             if d1.get(i,0) == 0:
#                 return False
#             d1[i] -=1
        
#         return True


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for char in ransomNote:
            if char not in magazine:
                return False
            
            magazine = magazine.replace(char, "", 1)
        
        return True
