import random

words = [
    "elma", "armut", "kavak", "ağaç", "bahar", "çilek", "dünya", "ev", "yaz", "göl",
    "beyaz", "kara", "sarı", "yeşil", "kırmızı", "deniz", "dağ", "kule", "şehir", "köy",
    "bilgisayar", "telefon", "kitap", "masa", "sandalye", "yol", "yıldız", "güneş", "ay",
    "kış", "yaz", "bahar", "sonbahar", "zeytin", "zambak", "kuruluş", "bütün", "yarım",
    "futbol", "basketbol", "müzik", "şarkı", "film", "kamera", "fotoğraf", "sinema",
    "televizyon", "yemek", "börek", "pide", "pizza", "hamburger", "salata", "balık",
    "et", "tavuk", "kurabiye", "çorba", "müze", "galeri", "resim", "kitaplık", "çalışma"
]


def hangman_game():
    word = random.choice(words).lower()
    alphabet = set("abcçdefgğhıijklmnoöprsştuüvyz")
    used_letters = set()
    hidden_word = "-" * len(word)
    lives = 6

    while lives > 0 and "-" in hidden_word:
        print(f"\nGizli kelime: {hidden_word}")
        print(f"Önceki tahminleriniz: {', '.join(used_letters)}")
        letter = input("Lütfen bir harf giriniz: ").lower()

        if letter in used_letters:
            print("Bu harfi zaten tahmin ettiniz, başka bir harf deneyin.")

        elif letter not in alphabet:
            print("Lütfen geçerli bir harf girin (Türkçe alfabesi).")

        else:
            used_letters.add(letter)

            if letter in word:
                word_list = list(hidden_word)
                for i in range(len(word)):
                    if word[i] == letter:
                        word_list[i] = letter
                hidden_word = "".join(word_list)
            else:
                lives -= 1
                print(f"Yanlış tahmin! Kalan can: {lives}")

        if "-" not in hidden_word:
            print(f"Tebrikler! Kelimeyi doğru tahmin ettiniz: {hidden_word}")
            break

    else:
        print(f"Canınız bitti. Kelime: {word}. Üzgünüz, kaybettiniz!")


hangman_game()
