from json.encoder import INFINITY
import os
from typing import List, Union
import logging

from pyrhhfbp import dump_session
from pyrhhfbp.samples.somesettings import RH_LOGIN_CRED_PATH, RH_SESSION_JSON_PATH
from someutils import choose_lowest, get_robinhood_from_disk_or_prompt, get_robinhood_login_json, user_prompt_yn

if __name__ == '__main__':

    logging.basicConfig(filename='buy_xela.log', encoding='utf-8', level=logging.DEBUG)

    rh = get_robinhood_from_disk_or_prompt(
        RH_SESSION_JSON_PATH, creds=get_robinhood_login_json())

    if rh.oauth.is_valid:
        print("Saving our valid login session to {} so we don't have to login a bunch".format(
            RH_SESSION_JSON_PATH))
        dump_session(rh, RH_SESSION_JSON_PATH)

    # ask user if they want to buy XELA
    stock_symbol = 'XELA'
    stock_quantity_desired = 3.0
    stock_quantity_in_pending_orders = 0.0

    stock_quote_data = rh.quote_data(stock_symbol)

    # check how many quotes user already has for XELA...
    my_orders = rh.get_open_orders()
    for order in my_orders:

        stock_data = (rh.get(order['instrument']))
        position_data = (rh.get(order['position']))
        # print("daStockData:")
        # print(daStockData)
        # if it matches our symbol,
        if stock_data['symbol'] == stock_symbol:
            # record how many stocks are in a pending order
            stock_quantity_in_pending_orders += float(position_data['quantity'])
            # print("position data:")
            # print(position_data)

    # check if user already owns XELA
    stock_quantity_owned = 0.0
    my_owned_stocks = rh.get_account()

    # if we would buy too much...
    stocks_in_orders_or_owned = stock_quantity_in_pending_orders + stock_quantity_owned

    if(stocks_in_orders_or_owned >= stock_quantity_desired):
        msg = "You already own {} stocks and already have orders for {} stocks.\n".format(
            stock_quantity_in_pending_orders,
            stock_quantity_owned
        )
        msg += ("Because of this, we are not going to BUY {d} {s} because it would exceed our target of {d} {s}.\n".format(
            d=stock_quantity_desired,
            s=stock_symbol
        ))
        raise ValueError(msg)
    else:
        # we need to buy less to target our goal...
        stock_quantity_desired -= stocks_in_orders_or_owned

    # We need to make a POJO to store this stuff...I am sick of handling raw JSON... We also should validate against a schema...the lack of JSON schema validation is the whole reason I had to modify the `place_buy_order` method.
    last_extended_hours_trade_price = stock_quote_data['last_extended_hours_trade_price']
    last_trade_price = stock_quote_data['last_trade_price']

    stock_price = choose_lowest(last_extended_hours_trade_price, last_trade_price)

    print("{}: costs ${}".format(stock_symbol, stock_price))

    # display this to the user if we are doing some math to reduce how many stocks we are buying
    extranote = (
        "\nNote: We already have {} stocks of {} bought or in pending orders.".format(
            stocks_in_orders_or_owned, stock_symbol)
        if (stocks_in_orders_or_owned > 0)
        else ""
    )

    yesmsg = "Yes, submit BUY order for {} {}.".format(
        stock_quantity_desired, stock_symbol)
    nomsg = "No, do not submit BUY order for {} {}.".format(
        stock_quantity_desired, stock_symbol)
    promptmsg = "Submit BUY order of {} {} for ${:.4f} total? {}".format(
        stock_quantity_desired,
        stock_symbol,
        (stock_quantity_desired * float(stock_price)),
        extranote
    )

    if user_prompt_yn(
            promptmsg,
            {
                'yes': yesmsg,
                'no': nomsg
            },
            successval=yesmsg):

        print("im BUYIIING {} {} OOOOUGHHHHH @w@ $_$ :DDDDD".format(stock_quantity_desired, stock_symbol))

        result = rh.place_buy_order(
            instrument=stock_quote_data,
            quantity=stock_quantity_desired,
            ask_price=stock_price)
        print("result:")
        print(result)

    else:
        print("k, not buying any XELA... stocks broke. understandable, have a great day")

    # rh.buy('youre mom')
