import base64

# https://gist.github.com/dssstr/aedbb5e9f2185f366c6d6b50fad3e4a4?permalink_comment_id=4035082#gistcomment-4035082
# Added more alphabets so that it doesnt error while using base64
def vigenere(
        text: str,
        key: str,
        alphabet='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz=-<>?/\\|!@#$%^&*()_+\', =',
        encrypt=True
):

    result = ''

    for i in range(len(text)):
        letter_n = alphabet.index(text[i])
        key_n = alphabet.index(key[i % len(key)])

        if encrypt:
            value = (letter_n + key_n) % len(alphabet)
        else:
            value = (letter_n - key_n) % len(alphabet)

        result += alphabet[value]

    return result


def vigenere_encrypt(text: str, key: str):
    # base64 encoding so that any unknown character not in alphabet doesnt throw error
    text = base64.urlsafe_b64encode(str.encode(text)).decode('utf-8')
    return vigenere(text=text, key=key, encrypt=True)


def vigenere_decrypt(text, key):
    f = vigenere(text=text, key=key, encrypt=False)
    # Decoding as base64
    return base64.urlsafe_b64decode(str.encode(f))
