def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    big_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    small_letters = "abcdefghijklmnopqrstuvwxyz"
    for letter in plaintext:
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
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    big_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    small_letters = "abcdefghijklmnopqrstuvwxyz"
    for letter in ciphertext:
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
    return plaintext
