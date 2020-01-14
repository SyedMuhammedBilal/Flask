import bcrypt

bcrypt_password = bcrypt.hashpw('password'.encode('utf8'), bcrypt.gensalt(12))

bcrypt_password1 = bcrypt.hashpw('password'.encode('utf8'), bcrypt.gensalt(12))

check = bcrypt.checkpw('password'.encode('utf8'), bcrypt_password)

check1 = bcrypt.checkpw('password'.encode('utf8'), bcrypt_password1)
print(bcrypt_password)
print(check)
print(bcrypt_password1)
print(check1)