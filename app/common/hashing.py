from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class HashCrypt():
    '''Description
    String encryption functions'''

    def EncryptPassword(password):
        '''Description
        :param str: To perform hash encryption
        :return str: hash'''
        return pwd_context.hash(password)

    def DecryptVerifyPassword(plain_password,hashed_password):
        '''Description
        :param str: plain_password from form login
        :return str: hashed_password from saved password
        :return bool: True/False'''
        return pwd_context.verify(plain_password,hashed_password)
