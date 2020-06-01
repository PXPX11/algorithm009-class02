class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str1 = ''
        for i in digits:
            str1 = str1 + str(i)
        number = int(str1) + 1
        ls = []
        for j in str(number):
            ls.append(int(j))
        return ls