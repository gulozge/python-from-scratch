from collections import Counter


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        # nums listesindeki her elemanın kaç kez tekrar ettiğini sayar ve bir Counter objesi döner.
        # Counter objesi aslında bir dict gibi çalışır ve öğeleri anahtar olarak, sıklıklarını ise değer olarak saklar.
        count = Counter(nums)

        # Counter objesi, her öğeyi anahtar olarak tutar ve öğelerin sıklıklarını (değerlerini) saklar.
        # key=count.get, her elemanın sıklığını almak için Counter'ın get metodunu kullanır.
        return max(count, key=count.get)


solution = Solution()
print(solution.majorityElement([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
