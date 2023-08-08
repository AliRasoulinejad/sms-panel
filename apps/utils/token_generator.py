import random

from config.env import env

token_length = env.int('LOGIN_TOKEN_LENGTH', default=5)

def token_generator():
    return random.randrange(10**token_length, 10**(token_length+1)-1)
