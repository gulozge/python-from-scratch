class Solution:

    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        """mors_alphabet=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        seen=set()
        for x in words:
            mors_code=""
            for i in x:
                k=letters.index(i.upper())
                mors_code=mors_code+mors_alphabet[k]
            if mors_code not in seen or len(words)!=1:
                seen.add(mors_code)

        return len(seen)
        """

        # 'a' ile 'z' arasındaki harflerin Morse kodu karşılıkları
        mors_alphabet = {
            'a': ".-", 'b': "-...", 'c': "-.-.", 'd': "-..", 'e': ".", 'f': "..-.", 'g': "--.", 'h': "....", 'i': "..",
            'j': ".---", 'k': "-.-", 'l': ".-..", 'm': "--", 'n': "-.", 'o': "---", 'p': ".--.", 'q': "--.-", 'r': ".-.",
            's': "...", 't': "-", 'u': "..-", 'v': "...-", 'w': ".--", 'x': "-..-", 'y': "-.--", 'z': "--.."
        }

        # Benzersiz Morse kodlarını saklamak için bir set kullanıyoruz
        seen = set()

        # Her kelimeyi inceleyip Morse kodunu set'e ekliyoruz
        for word in words:
            # Her harfin Morse kodunu alıyoruz
            mors_code = ''.join(mors_alphabet[char] for char in word.lower())
            seen.add(mors_code)  # Morse kodunu set'e ekliyoruz

        # Set'in boyutu, benzersiz Morse kodlarının sayısını verir
        return len(seen)


solution = Solution()
liste = ["gin", "zen", "gig", "msg"]
print(solution.uniqueMorseRepresentations(liste))
