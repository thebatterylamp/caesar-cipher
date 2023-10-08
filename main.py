alphabet = list(map(chr, range(ord('a'), ord('z') + 1)))
alphabets = alphabet + alphabet


def encode(message, shift):
    encoded_message = ""
    for ch in message:
        if ch in alphabets:
            position = alphabets.index(ch)
            new_position = position + shift
            new_ch = alphabets[new_position]
            encoded_message += new_ch
        else:
            encoded_message += ch
    return encoded_message


def decode(message, shift):
    decoded_message = ""
    for ch in message:
        if ch in alphabets:
            position = alphabets.index(ch)
            new_position = position - shift
            new_ch = alphabets[new_position]
            decoded_message += new_ch
        else:
            decoded_message += ch
    return decoded_message


print("Welcome to Caesar Cipher!")
options = input("Please type 'encode' to encrypt or 'decode' to decrypt: ").lower()
user_input = input("Please type your message: ").lower()
code = int(input("Please type the shift number: "))

if options == 'encode':
    result = encode(user_input, code)
    print(f"The encoded message is '{result}'")
elif options == 'decode':
    result = decode(user_input, code)
    print(f"The decoded message is '{result}'")
else:
    print("Invalid Input!")
