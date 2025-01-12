import art

print(art.logo)
should_continue = True
while should_continue != 'no':
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']

    direction = input("Type 'encode' to encrypt, type 'decode to decrypt: \n").lower()

    text = input("Type your message: \n").lower()

    shift = int(input("Type the shift number \n"))


    # TODO 1: Create a function called 'encrypt()' that takes 'original_text' and shift amount and print the
    #  encrypted text. encrypted_text = '' def decrypt(original_text, shift_number): decipher_text = '' for letter in
    #  original_text: shifted_position = alphabet.index(letter) - shift_number shifted_position %= len(alphabet)
    #  decipher_text = decipher_text + alphabet[shifted_position] print(f'Here is the decoded result: {decipher_text}')
    #
    #
    # decrypt(text, shift)
    #
    # # Decrypt function
    # def encrypt(original_text, shift_number):
    #     cipher_text = ''
    #     for letter in original_text:
    #         shifted_position = alphabet.index(letter) + shift_number
    #         shifted_position %= len(alphabet)
    #         cipher_text = cipher_text +alphabet[shifted_position]
    #     print(f'Here is the encoded result: {cipher_text}')
    #
    #
    # encrypt(text, shift)

    def caeser(original_text, shift_number, encode_or_decode):
        output_text = ""
        if encode_or_decode == 'decode':
            shift_number *= -1
        for letter in original_text:
            if letter not in alphabet:
                output_text += letter
            else:
                shifted_position = alphabet.index(letter) + shift_number
                shifted_position %= len(alphabet)
                output_text = output_text + alphabet[shifted_position]
        print(f'Here is the {encode_or_decode} result: {output_text}')


    caeser(original_text=text, shift_number=shift, encode_or_decode=direction)

    should_continue = input("Type 'Yes' if you want to continue, else 'No'\n").lower()
