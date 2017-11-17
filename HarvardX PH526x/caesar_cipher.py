"""
Caesar Cipher

Author: Gareth Mawer
"""
import string

alphabet = string.ascii_lowercase + " "
letters = dict(enumerate(alphabet))

encryption_key = 3

message = "hi my name is caesar"

def create_encoding_dictionary(encryption_key):
    """
    Assumes that encryption_key is an integer.
    
    Returns a dictionary which encodes a letter of the alphabet to a number
    """
    encoding = {}
    index = 0
    for letter in alphabet:
        if (index + encryption_key) < 0 or (index + encryption_key) > 26:
            code = (index + encryption_key) % 27
        else:
            code = (index + encryption_key)
        encoding[letter] = code
        index += 1
    return encoding

def caesar(message, encryption_key):
    """
    Assumes that message is a string and encryption_key is an integer
    
    The Caesar Cipher involves using an encryption key to change the value of the number 
    associated with each letter of the alphabet, the dictionary encoding implements this.
    We then use the number associated with encoding each letter in the message as a key,
    called the encoding_key, to find the associated letter with that key in the letters
    dictionary. We then add the associated letters with the encoding key to a new string
    encrypting the original message.
    
    Returns a string of the message encrypted using a Caesar Cipher
    """
    encrypted_message = ""
    encoding = create_encoding_dictionary(encryption_key)
    for letter in message:
        encoding_key = encoding[letter]
        encrypted_letter = letters[encoding_key]
        encrypted_message += encrypted_letter
    return encrypted_message

def decode_encrypted_message(encrypted_message, encryption_key):
    """
    Assumes that encrypted_message is a string produced by the caesar function
    to encrypt a message. Also assumes that the encryption_key is the initial 
    encryption key used to encrypt the message. 
    
    Returns a string of the encrypted message deciphered, i.e. the original 
    message
    """
    decryption_key = -encryption_key
    encoding = create_encoding_dictionary(decryption_key)
    original_message = caesar(encrypted_message, decryption_key)
    return original_message

def test_caesar_cipher():
    encryption_keys = [i for i in range(27)]
    for encryption_key in encryption_keys:
        print("Original Message: ", message)
        
        encrypted_message = caesar(message, encryption_key)
        print("Encrypted message using encyrption key ", encryption_key, ": ", encrypted_message)
        
        decrypted_message = decode_encrypted_message(encrypted_message, encryption_key)
        print("Decrypted message: ", decrypted_message)
        
        print("Is original message the same as decrypted message? ", message == decrypted_message)
    
test_caesar_cipher()
