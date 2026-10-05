def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    big_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    small_letters = "abcdefghijklmnopqrstuvwxyz"
    keyword = keyword.lower()
    i = 0
    for letter in plaintext:
        key_letter = keyword[i % len(keyword)]
        shift = small_letters.index(key_letter)
        if letter in big_letters:
            number = big_letters.index(letter)
            new_number = (number + shift) % 26
            ciphertext = ciphertext + big_letters[new_number]
        elif letter in small_letters:
            number = small_letters.index(letter)
            new_number = (number + shift) % 26
            ciphertext = ciphertext + small_letters[new_number]
        else:
            ciphertext = ciphertext + letter
        i = i + 1
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    big_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    small_letters = "abcdefghijklmnopqrstuvwxyz"
    keyword = keyword.lower()
    i = 0
    for letter in ciphertext:
        key_letter = keyword[i % len(keyword)]
        shift = small_letters.index(key_letter)
        if letter in big_letters:
            number = big_letters.index(letter)
            new_number = (number - shift) % 26
            plaintext = plaintext + big_letters[new_number]
        elif letter in small_letters:
            number = small_letters.index(letter)
            new_number = (number - shift) % 26
            plaintext = plaintext + small_letters[new_number]
        else:
            plaintext = plaintext + letter
        i = i + 1
    return plaintext
