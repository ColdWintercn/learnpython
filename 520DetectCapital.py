class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        count = 0
        judge = 0
        if ord(word[0]) in range(65,91):
            for i in word:
                count += 1
                if ord(i) in range (65,91):
                    judge += 1
            if count == judge:
                return True
            else :
                if judge == 1:
                    return True
                else:
                    return False
        else:
            for i in word:
                count += 1
                if ord(i) in range (65,91):
                    judge += 1
            if count == judge:
                return False
            else:
                if judge == 0:
                    return True
                else:
                    return False