def caesar_decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted_char = chr((ord(char) - shift - ord('а')) % 32 + ord('а'))
            decrypted_text += shifted_char
        else:
            decrypted_text += char
    return decrypted_text

def decrypt_with_key(ciphertext, key):
    key_shifts = [ord(char) - ord('а') for char in key]

    decrypted_text = ""
    for i, char in enumerate(ciphertext):
        shift = key_shifts[i % len(key)]
        decrypted_char = caesar_decrypt(char, shift)
        decrypted_text += decrypted_char

    return decrypted_text

ciphertext = "мао з юйчжлкнауша"
key = "юфу"

# Операция 1: Многократный шифр Цезаря
decrypted_text_1 ="олы й йцщтшмщмхдм"
# Операция 2: Однократный шифр Цезаря
print(decrypted_text_1)
print()
for i in range(1,33):
    decrypted_text_2 = caesar_decrypt(decrypted_text_1, i)

    print("Расшифрованный текст:", decrypted_text_2)
