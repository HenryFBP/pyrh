import os

RH_CONFIG_PATH = os.path.abspath(os.path.expanduser('~/.robinhood/'))

if not os.path.exists(RH_CONFIG_PATH):
    os.mkdir(RH_CONFIG_PATH)

RH_LOGIN_CRED_PATH = os.path.join(RH_CONFIG_PATH, 'login.json')
RH_SESSION_JSON_PATH = os.path.join(RH_CONFIG_PATH, 'session.json')

