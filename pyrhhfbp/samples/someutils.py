import json
from json.encoder import INFINITY
import os
from typing import Dict, Any, List, Union

from pyrhhfbp import Robinhood, load_session
from pyrhhfbp.samples.somesettings import RH_LOGIN_CRED_PATH


def choose_lowest(*args: List[Union[int, str, float, None]]):
    lowest = INFINITY

    for arg in args:

        if arg:

            if type(arg) is str:
                arg = float(arg)

            if type(arg) is int:
                arg = float(arg)

            if arg < lowest:
                lowest = arg

    if lowest == INFINITY:
        return None

    return lowest


def user_prompt_choose_dict(
        d=None,
        prompt: str = "Please choose:",
        quitkey: str = 'q',
        invalidmsg: str = "Invalid choice.",
        showvalidchoices: bool = True
) -> Union[Any, None]:
    if d is None:
        d = {1: 'apple', '2': 'banana', 3: 'potato'}

    while True:
        for k in d.keys():
            v = d[k]
            print("- [{:^3s}] {}".format(k, repr(v)))
        selection = input(
            prompt +
            (" ({} to quit)".format(quitkey) if quitkey else '') +
            "\n > "
        )
        if quitkey and (selection == quitkey):
            return None

        if selection in d.keys():
            # if they choose a valid choice
            return d[selection]
        else:
            print(invalidmsg)

            if showvalidchoices:
                print("Valid choices: {}".format(repr(list(d.keys()))))


def user_prompt_yn(prompt: str = "Yes or no?", promptdict=None, successval="Yes") -> bool:
    if promptdict is None:
        promptdict = {'y': successval, 'n': "No"}

    daChoice = user_prompt_choose_dict(promptdict, prompt)

    return daChoice == successval


def get_robinhood_login_json(path=RH_LOGIN_CRED_PATH) -> Dict:
    if not os.path.exists(path):
        raise Exception("login file {} does not exist. please create it.".format(path))

    with open(path) as fh:
        obj = json.load(fh)
    return obj


def get_robinhood_from_disk_or_prompt(session_json_path, creds) -> Robinhood:
    if os.path.exists(session_json_path):
        rh = load_session(session_json_path)
        print("Loaded session from '{}'...\n"
              "Testing if it's valid... AAPL price = {}".format(
                  session_json_path,
                  rh.get_quote_list("AAPL", "symbol,last_trade_price")[0][1]
              ))
    else:
        print("We do not have a saved session. Using saved creds. you may be prompted for 2fa")
        rh = Robinhood(username=creds['email'],
                       password=creds['password'], challenge_type='sms')

    print("rh.oauth.is_valid={}".format(rh.oauth.is_valid))
    if not rh.oauth.is_valid:
        print("We need to log in again :P")
        rh.login()

    return rh
