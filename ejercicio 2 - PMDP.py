from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os

key = b"12345678901234567890123456789012"
texto = b"Expecto Patronum"
fixed_iv = b"\x00" * 16 

def pad(data):
    padder = padding.PKCS7(128).padder()
    return padder.update(data) + padder.finalize()

def encrypt(mode_obj, data, needs_padding=True):
    if needs_padding:
        data = pad(data)
    cipher = Cipher(algorithms.AES(key), mode_obj, backend=default_backend())
    enc = cipher.encryptor()
    return enc.update(data) + enc.finalize()

print("=== Con IV aleatorio ===")
iv_cbc = os.urandom(16)
iv_ofb = os.urandom(16)
iv_cfb = os.urandom(16)
ct_cbc = encrypt(modes.CBC(iv_cbc), texto)
ct_ofb = encrypt(modes.OFB(iv_ofb), texto, False)
ct_cfb = encrypt(modes.CFB(iv_cfb), texto, False)
ct_ecb = encrypt(modes.ECB(), texto)

print(f"CBC (IV={iv_cbc.hex()[:8]}...): {ct_cbc.hex()}")
print(f"OFB (IV={iv_ofb.hex()[:8]}...): {ct_ofb.hex()}")
print(f"CFB (IV={iv_cfb.hex()[:8]}...): {ct_cfb.hex()}")
print(f"ECB (sin IV)            : {ct_ecb.hex()}")

print("\n=== Con IV fijo ===")
ct_cbc_f = encrypt(modes.CBC(fixed_iv), texto)
ct_ofb_f = encrypt(modes.OFB(fixed_iv), texto, False)
ct_cfb_f = encrypt(modes.CFB(fixed_iv), texto, False)

print(f"CBC IV fijo: {ct_cbc_f.hex()}")
print(f"OFB IV fijo: {ct_ofb_f.hex()}")
print(f"CFB IV fijo: {ct_cfb_f.hex()}")
print("\n=== Texto repetido con IV fijo (ECB pattern) ===")
texto2 = b"Expecto Patronum Expecto Patronum"
padder = padding.PKCS7(128).padder()
p2_padded = padder.update(texto2) + padder.finalize()
ct2_ecb = encrypt(modes.ECB(), texto2)
ct2_cbc = encrypt(modes.CBC(fixed_iv), texto2)
print(f"ECB doble: {ct2_ecb.hex()}")
print(f"CBC doble: {ct2_cbc.hex()}")
print(f"ECB bloque1: {ct2_ecb[:16].hex()}")
print(f"ECB bloque2: {ct2_ecb[16:32].hex()}")
print(f"Son iguales: {ct2_ecb[:16] == ct2_ecb[16:32]}")