from jose import jwt


def generate(input: str):
    payload = {'id': input}
    token = jwt.encode(payload, 'CHAVE-SECRETA', algorithm='HS256')
    return token


def decode(token):
    payload = jwt.decode(token, 'CHAVE-SECRETA', algorithms=['HS256'])
    return payload
