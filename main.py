import string
alphabet = list(string.ascii_lowercase) * 2 # Doubles the size of the alphabet so the iteration doesnt go beyond the range of a normal alphabet

#Makes sure what's entered is either 'encode' or 'decode'
while True:       
    while True:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        if direction in ['encode', 'decode']:
            break  # Exit the loop if input is valid
        else:
            print("Invalid input. Please type 'encode' or 'decode'.")
            
    text = input("Type your message:\n").lower()
    
    # Makes sure what's entered is an integer
    while True:
        try:
            shift = int(input("Type the shift number:\n"))
            break
        except (ValueError, IndexError):
            print("Please enter a valid integer for the shift number.")
    shift = shift % 26
    # SHORTER VERSION
    
    def encrypt(plain_text, shift_amount):
        cipher = ''
        # Converts shift_amount to a negative number so it iterates backwards rather than forwards and decrypts the text
        if direction == 'decode':
            shift_amount *= -1
        for char in plain_text:
            if char in alphabet:
                cipher_index = alphabet.index(char)+shift_amount
                cipher += alphabet[cipher_index]
            else:
                cipher += char
        return(cipher)
    caesar_cipher = encrypt(text, shift)
    print(f"Caesar says {caesar_cipher}!\n")
    
    user_input = input("Do you want to restart the Caesar Cipher Program:  ").lower()
    if user_input == 'yes':
        pass
    else:
        break
    
print("Please enter a shift number 25 and below")