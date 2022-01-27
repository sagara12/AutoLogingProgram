from cryptography.fernet import Fernet
# key = Fernet.generate_key()
# print(key)
f = Fernet(b'zCJqo_kdutX3uSmz9iso8-4XBABGROF3T2-DRaZ7Re0=')
token = f.encrypt(b"899008877668899")
print(token)
b'...'
decoding = f.decrypt(token)
print(decoding)