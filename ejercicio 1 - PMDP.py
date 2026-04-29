from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os

key = b"12345678901234567890123456789012"
texto = b"Expecto Patronum"
iv = os.urandom(16)

padder = padding.PKCS7(128).padder()
padded = padder.update(texto) + padder.finalize()

cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
encryptor = cipher.encryptor()
ciphertext = encryptor.update(padded) + encryptor.finalize()

decryptor = cipher.decryptor()
padded_plain = decryptor.update(ciphertext) + decryptor.finalize()
unpadder = padding.PKCS7(128).unpadder()
decrypted = unpadder.update(padded_plain) + unpadder.finalize()

print(f"Texto plano original : {texto.decode()}")
print(f"Clave utilizada      : {key.decode()}")
print(f"IV utilizado         : {iv.hex()}")
print(f"Texto cifrado (hex)  : {ciphertext.hex()}")
print(f"Texto descifrado     : {decrypted.decode()}")