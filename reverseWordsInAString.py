#https://leetcode.com/problems/reverse-words-in-a-string/
def reverseWords(self, s):
    s = s.strip().split()
    return ' '.join(s[::-1])
