'''Здесь аналогично заданию (Decetror должен порождать FaceDecector или MegaDetector)
   Authenticator порождает FacebookAuthenticator и AmazonAuthenticator
   Credentials - AmazonCredentials и FacebookCredentials
   User - FacebookUser и AmazonUser
   '''
from abc import ABC, abstractmethod
import random
from enum import Enum

class User(ABC):
    "Абстрактный пользователь(продукт)"
    pass

class FacebookUser(User):
    "Пользователь Facebook с номером телефона(конкретная реализация user)"

    def __init__(self,phone):
        print(f'Created FacebookUser: {phone}')


class AmazonUser(User):
    "Пользователь Amazon с почтой(конкретная реализация user)"

    def __init__(self, email):
        print(f'Created AmazonUser: {email}')

class Credentials(ABC):
    "Абстрактные учетные данные"
    pass

class AmazonCredentials(Credentials):
    "Учетные данные для входа в Амазон(Конкретная реализация учетных данных)"
    def __init__(self,email,password):
        self._email = email
        self._password = password

    @property
    def email(self):
        return self._email

    @property
    def password(self):
        return self._password

class FacebookCredentials(Credentials):
    "Учетные данные для входа в Фейсбук(Конкретная реализация учетных данных)"
    def __init__(self,phone,password):
        self._phone = phone
        self._password = password

    @property
    def phone(self):
        return self._phone

    @property
    def password(self):
        return self._password

class Authenticator(ABC):
    "Абстрактный аутентификатор(создатель)"
    @abstractmethod
    def authenticate(self,credentials: Credentials) -> User:
        pass

class FacebookAuthenticator(Authenticator):
    "Аутентификатор Фэйсбука(абстрактная реализация аутентификатора)"
    def authenticate (self, credentials: FacebookCredentials) -> FacebookUser:
        print(f'Authenticated by phone: {credentials.phone}')
        return FacebookUser(credentials.phone)#возвращает продукт

class AmazonAuthenticator(Authenticator):
    "Аутентификатор Амазон(абстрактная реализация аутентификатора)"
    def authenticate (self, credentials: AmazonCredentials) -> AmazonUser:
        print(f'Authenticated by email: {credentials.email}')
        return AmazonUser(credentials.email)#возвращает продукт

def authenticate(authenticator: Authenticator, credentials: Credentials) -> User:
    return authenticator().authenticate(credentials)#

#Форма логина Facebook (телефон + пароль)
phone = '+1 800 99 444'
password = 'joke'
credentials = FacebookCredentials(phone,password)
user: FacebookUser = authenticate(FacebookAuthenticator,credentials)

#Форма логина Амазон (мыло + пароль)
email = '455ghjo@facebook.com'
password = 'joke'
credentials = AmazonCredentials(email,password)
user: AmazonUser = authenticate(AmazonAuthenticator,credentials)
