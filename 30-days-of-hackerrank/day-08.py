phone_book = {}


def phone_book_add(s: str):
    s = s.split()
    phone_book[s[0]] = s[1]


n = int(input())

for i in range(0, n):
    s = input()
    phone_book_add(s)

try:
    while True:
        query = input()
        if phone_book.get(query):
            print(str(query)+"="+str(phone_book.get(query)))

        else:
            print("Not found")

except EOFError:
    pass
