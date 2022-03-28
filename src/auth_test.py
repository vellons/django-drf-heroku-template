import requests
import os

# https://firebase.google.com/docs/reference/rest/auth#section-sign-in-email-password
FIREBASE_USER_VERIFY_SERVICE = 'https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword'
FIREBASE_API_KEY = os.getenv('FIREBASE_API_KEY', None)  # Project settings > General > API web key


def user_login(email, passwd):
    url = '{}?key={}'.format(FIREBASE_USER_VERIFY_SERVICE, FIREBASE_API_KEY)
    data = {
        'email': email,
        'password': passwd,
        'returnSecureToken': True
    }
    result = requests.post(url, json=data)
    json_result = result.json()
    return json_result


if __name__ == '__main__':
    email = os.getenv('FIREBASE_LOGIN_EMAIL', None)
    password = os.getenv('FIREBASE_LOGIN_PWD', None)
    if not email:
        email = input('Email> ')
    if not password:
        password = input('Password> ')

    r = user_login(email, password)
    print(r)

    print('localId: {}'.format(r['localId']))
    print('idToken: {}'.format(r['idToken']))
    print('refreshToken: {}'.format(r['refreshToken']))

    """
    Now you cat make http request with 'Authorization' header that contains idToken
    
    curl --location --request GET 'http://localhost:8000/api/users/' \
        --header 'Authorization: eyJhbGZ......'
    """
