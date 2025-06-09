class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        str1 = self.get_dict_chr(s)
        str2 = self.get_dict_chr(t)
        if str1 == str2:
            return True
        return False

    def get_dict_chr(self, s : str):
        char_count = {}
        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        return char_count
