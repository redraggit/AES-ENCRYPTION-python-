from Crypto.Cipher import AES
from Crypto import Random
import base64

padding = '$'

block_size = 16
p = lambda s:s + (block_size - len(s) % block_size)* padding

key = Random.new().read(16)
IV = Random.new().read(16)

E = AES.new(key, AES.MODE_CBC, IV)

encryption_methode = base64.b64encode (IV + E.encrypt(p('sukaa bliaatzz').encode('utf-8')))
print(encryption_methode) 

D = AES.new(key, AES.MODE_CBC, IV)
IV_= base64.b64decode(encryption_methode)[:16]
encryption_methode_ = base64.b64decode(encryption_methode)[16:]
plain_text = D.decrypt(encryption_methode_)

plain_text = plain_text.decode('utf-8')
print(plain_text.rstrip('$'))