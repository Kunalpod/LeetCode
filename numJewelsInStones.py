# https://leetcode.com/problems/jewels-and-stones/
def numJewelsInStones(self, J, S):
    count = 0
    for stone in S:
        if stone in J: count += 1
    return count
