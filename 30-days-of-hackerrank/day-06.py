def odd_index_or_even_index(s: str) -> str:
    result = ""
    odd_indexed = ""
    even_indexed = ""
    for i in range(0, len(s)):
        if i % 2 == 0:
            even_indexed = even_indexed+s[i]
        else:
            odd_indexed = odd_indexed+s[i]
    result = even_indexed+" "+odd_indexed
    return result


k = int(input())
for i in range(0, k):
    s = input()
    print(odd_index_or_even_index(s))
