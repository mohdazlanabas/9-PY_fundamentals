import hashlib
from cryptography.fernet import Fernet

# original message
message_Original = (
    "Government Lying To You. They Are Brainwashing Your Mind. There is No COVID"
)

# key generator
key = Fernet.generate_key()
key_Store = Fernet(key)
key_View = str(key, "utf8")

# message encryption
messsage_Encrypt = key_Store.encrypt(
    b"Government Lying To You. They Are Brainwashing Your Mind. There is No COVID"
)
message_Encrypt_View = str(messsage_Encrypt, "utf8")

# message decryption
message_Decrypted = key_Store.decrypt(messsage_Encrypt)


# printing
print(f"Message Original is: {message_Original}")
print(f"Encryption Key is: {key_View}")
print(f"Message Encrypted is: {message_Encrypt_View}")
print(f"Message Decrypted is: {message_Decrypted}")


"""
print(f"Original Message is: {message_Original}")

# 1st Needs To Enccode
message_Encoded = message_Original.encode()

# 2nd is the SHA encryption
message_SHA256 = hashlib.sha256(message_Encoded)
message_Hash = message_SHA256.hexdigest()
print(f"Hash256 is: {message_Hash }")
"""
