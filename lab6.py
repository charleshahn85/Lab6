def vigenere_sq(alphabet):
    print("   " + " ".join(alphabet))
    print("  " + "-" * (len(alphabet) * 2 + 1))
    for i, letter in enumerate(alphabet):
        row = alphabet[i:] + alphabet[:i]
        print(f"{letter} | {' '.join(row)}")

def letter_to_index(letter, alphabet):
    return alphabet.index(letter)


def index_to_letter(index, alphabet):
    return alphabet[index % len(alphabet)]


def vigenere_index(key_letter, plaintext_letter, alphabet):
    key_index = letter_to_index(key_letter, alphabet)
    plaintext_index = letter_to_index(plaintext_letter, alphabet)
    return (plaintext_index + key_index) % len(alphabet)


def undo_vigenere_index(key_letter, cipher_letter, alphabet):
    key_index = letter_to_index(key_letter, alphabet)
    cipher_index = letter_to_index(cipher_letter, alphabet)
    return (cipher_index - key_index) % len(alphabet)


def encrypt_vigenere(key, plaintext, alphabet):
    ciphertext = ""
    key_length = len(key)
    for i, letter in enumerate(plaintext):
        if letter in alphabet:
            key_letter = key[i % key_length]
            cipher_index = vigenere_index(key_letter, letter, alphabet)
            ciphertext += index_to_letter(cipher_index, alphabet)
        else:
            ciphertext += letter
    return ciphertext


def decrypt_vigenere(key, ciphertext, alphabet):
    plaintext = ""
    key_length = len(key)
    for i, letter in enumerate(ciphertext):
        if letter in alphabet:
            key_letter = key[i % key_length]
            plain_index = undo_vigenere_index(key_letter, letter, alphabet)
            plaintext += index_to_letter(plain_index, alphabet)
        else:
            plaintext += letter
    return plaintext


def main():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = "DAVINCI"

    while True:
        print("\nVigenère Cipher Program")
        print(" ")
        print("1. Encrypt plain text")
        print("2. Decrypt plain text")
        print("3. Print Vigenère Square")
        print("4. Exit program")
        print(" ")
        choice = input("Enter your choice (1-4); ")

        if choice == '1':
            plaintext = input("Enter plain text to encrypt: ").upper()
            encrypted = encrypt_vigenere(key, plaintext, alphabet)
            print(f"Encrypted text: {encrypted}")
        elif choice == '2':
            ciphertext = input("Enter cipher text to decrypt: ").upper()
            decrypted = decrypt_vigenere(key, ciphertext, alphabet)
            print(f"Decrypted text: {decrypted}")
        elif choice == '3':
            vigenere_sq(alphabet)
        elif choice == '4':
            print("CYA!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()