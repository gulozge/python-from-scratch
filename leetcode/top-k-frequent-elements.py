from collections import Counter


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        tmp = Counter(nums)
        sorted_dict_desc = dict(
            # key=lambda item: item[1] değere göre sıralayacak
            sorted(tmp.items(), key=lambda item: item[1], reverse=True))
        count = 0
        result = list()
        for key in sorted_dict_desc.keys():
            if count < k:
                result.append(key)
                count += 1
            else:
                break
        return result


solution = Solution()
print(solution.topKFrequent([1, 1, 1, 2, 2, 3], 2))
