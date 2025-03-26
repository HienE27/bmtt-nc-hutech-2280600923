import os
import ecdsa

class ECCCipher:
    def __init__(self):
        if not os.path.exists('cipher/ecc/keys'):
            os.makedirs('cipher/ecc/keys')

    def generate_keys(self):
        sk = ecdsa.SigningKey.generate()
        vk = sk.get_verifying_key()

        with open('cipher/ecc/keys/private_key.pem', 'wb') as p:
            p.write(sk.to_pem())

        with open('cipher/ecc/keys/public_key.pem', 'wb') as p:
            p.write(vk.to_pem())

    def load_keys(self):
        with open('cipher/ecc/keys/private_key.pem', 'rb') as p:
            sk = ecdsa.SigningKey.from_pem(p.read())
        with open('cipher/ecc/keys/public_key.pem', 'rb') as p:
            vk = ecdsa.VerifyingKey.from_pem(p.read())
        return sk, vk

    def sign(self, message, key):
        return key.sign(message.encode('ascii'))

    def verify(self, message, signature, key):
        _, vk = self.load_keys()
        try:
            return vk.verify(signature, message.encode('ascii'))
        except ecdsa.BadSignatureError:
            return False