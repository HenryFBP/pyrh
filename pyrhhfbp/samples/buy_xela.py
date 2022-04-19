import os

from pyrhhfbp import dump_session
from pyrhhfbp.samples.somesettings import RH_LOGIN_CRED_PATH, RH_SESSION_JSON_PATH
from someutils import get_robinhood_from_disk_or_prompt, get_robinhood_login_json, user_prompt_yn

if __name__ == '__main__':

    rh = get_robinhood_from_disk_or_prompt(RH_SESSION_JSON_PATH, creds=get_robinhood_login_json())

    if rh.oauth.is_valid:
        print("Saving our valid login session to {} so we don't have to login a bunch".format(
            RH_SESSION_JSON_PATH))
        dump_session(rh, RH_SESSION_JSON_PATH)

    # check if user already has a quote for XELA...
    # raise NotImplementedError("lol u r lazy")

    # ask user if they want to buy XELA
    stock_symbol = 'XELA'
    stock_quote_data = rh.quote_data(stock_symbol)

    # TODO: What is the lower price? idk lol. We need to make a POJO to store this stuff...I am sick of handling raw JSON... We also should validate against a schema...the lack of JSON schema validation is the whole reason I had to modify the `place_buy_order` method.
    stock_price = stock_quote_data['last_extended_hours_trade_price']
    if not stock_price:
        stock_price = stock_quote_data['last_trade_price']

    stock_quantity = 3
    print("{}: costs ${}".format(stock_symbol, stock_price))

    yesmsg = "Yes, submit BUY order for {} {}.".format(stock_quantity, stock_symbol)
    nomsg = "No, do not submit BUY order for {} {}.".format(stock_quantity, stock_symbol)
    promptmsg = "Submit BUY order of {} {} for ${:.4f} total?".format(
        stock_quantity,
        stock_symbol,
        (stock_quantity * float(stock_price))
    )

    if user_prompt_yn(
            promptmsg,
            {
                'yes': yesmsg,
                'no': nomsg
            },
            successval=yesmsg):

        print("im BUYIIING {} {} OOOOUGHHHHH @w@ $_$ :DDDDD".format(stock_quantity, stock_symbol))

        result = rh.place_buy_order(
            instrument=stock_quote_data,
            quantity=stock_quantity,
            ask_price=stock_price)
        print("result:")
        print(result)

    else:
        print("k, not buying any XELA... stocks broke. understandable, have a great day")

    # rh.buy('youre mom')
