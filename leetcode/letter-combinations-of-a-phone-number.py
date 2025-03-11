import itertools


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []

        liste = list()
        result = list()
        dic = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        for i in digits:
            liste.append(dic[i])
        """
        itertools.product(*) fonksiyonu, 
        verilen listelerdeki her elemandan birer tane seçerek, tüm olası kombinasyonları oluşturur.
        Her kombinasyonu bir tuple (demet) olarak döndürür.
        """
        for i in itertools.product(*liste):
            combined_string = ''.join(i)
            result.append(combined_string)

        return result


solution = Solution()
print(solution.letterCombinations("23"))
