from cryptography.fernet import Fernet

# Program Generates a random key for Encryption and Decryption of logs collected
key = Fernet.generate_key()
file = open("encryption_key.txt", 'wb')
file.write(key)
file.close()
