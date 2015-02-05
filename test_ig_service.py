#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Run unit tests using
nosetests -s -v
"""

import pandas as pd
from utils_igmarkets.ig_service import IGService
from utils_igmarkets.trading_ig_config import Config  # defines username, password, api_key, acc_type, acc_number

def test_ig_service():
    '''Connect using the rest api to access account information'''
    c = Config()
    ig_service = IGService(c.username, c.password, c.api_key, c.acc_type)
    ig_service.create_session()

    print("fetch_accounts")
    response = ig_service.fetch_accounts()
    print(response)
    assert(response['balance'][0]['available'] > 0)

    raw_input('\n\n***************press any key******************\n\n')

    print("fetch_account_activity_by_period")
    response = ig_service.fetch_account_activity_by_period(1000000)
    print(response[:10])
    assert(isinstance(response, pd.DataFrame))

    # raw_input('\n\n***************press any key******************\n\n')
    # #
    # print("fetch_transaction_history_by_type_and_period")
    # response = ig_service.fetch_transaction_history_by_type_and_period(100000000, "ALL")
    # print(response)
    # assert(isinstance(response, pd.DataFrame))

    raw_input('\n\n***************press any key******************\n\n')
    #
    print("fetch_open_positions")
    response = ig_service.fetch_open_positions()
    print(response)
    assert(isinstance(response, pd.DataFrame))

    raw_input('\n\n***************press any key******************\n\n')

    print("fetch_working_orders")
    response = ig_service.fetch_working_orders()
    print response
    #print response['marketData']
    #print response['workingOrderData']
    assert(isinstance(response, pd.DataFrame))

    raw_input('\n\n***************press any key******************\n\n')

    print("fetch_top_level_navigation_nodes")
    response = ig_service.fetch_top_level_navigation_nodes()
    print(response) # dict with nodes and markets
    assert(isinstance(response, dict))
    market_id = response['nodes']['id'].iloc[0]

    print("fetch_client_sentiment_by_instrument")
    response = ig_service.fetch_client_sentiment_by_instrument(market_id)
    print(response)
    assert(isinstance(response, dict))

    print("fetch_related_client_sentiment_by_instrument")
    response = ig_service.fetch_related_client_sentiment_by_instrument(market_id)
    print(response)
    assert(isinstance(response, pd.DataFrame))

    print("fetch_sub_nodes_by_node")
    node = market_id #?
    response = ig_service.fetch_sub_nodes_by_node(node)
    print(response)
    #

    raw_input('***************press any key******************\n\n')

    print("fetch_all_watchlists")
    response = ig_service.fetch_all_watchlists()
    print(response)
    watchlist_id = response['id'].iloc[0]
    #
    #
    raw_input('\n\n***************press any key******************\n\n')
    print("fetch_watchlist_markets")
    response = ig_service.fetch_watchlist_markets(watchlist_id)
    print(response)
    epic = response['epic'].iloc[5]

    raw_input('\n\n***************press any key******************\n\n')
    print("fetch_market_by_epic")
    response = ig_service.fetch_market_by_epic(epic)
    print(response)


    raw_input('\n\n***************press any key******************\n\n')
    print("search_markets based on text or symbol. \n To list epics on CBA type 'cba' with quotes. \n")
    #search_term = input('Input symbol or text: ')
    search_term = 'tls'
    response = ig_service.search_markets(search_term)
    print(response)

    print 'Epic ------------------> ', epic
    #epic = "CS.D.USDJPY.MINI.IP"
    print epic

    raw_input('\n\n***************press any key******************\n\n')

    print 'Market detail for Epic: ', epic
    response = ig_service.fetch_market_by_epic(epic)
    print response

    raw_input('\n\n***************press any key to send a market order on %s mini contract******************\n\n' % 'CS.D.AUDUSD.MINI.IP')
    print 'Create a market order via the api'
    raw_input('\n\n***************press any key******************\n\n')

    response = ig_service.create_open_position(currency_code='USD', direction='BUY', epic='CS.D.AUDUSD.MINI.IP', expiry='-', force_open='false',
        guaranteed_stop='false', level='', limit_distance='', limit_level='', order_type='MARKET', size=3,
        stop_distance='', stop_level='')

    print response
    print '\n\n---------------->>>>>order accepted/rejected? ', response['dealStatus'], '\n\n'

    raw_input('\n\n***************press any key******************\n\n')
    print 'Create an working order via the api'
    raw_input('\n\n***************press any key******************\n\n')

    response = ig_service.create_working_order(currency_code='USD', direction='SELL', epic='CS.D.AUDUSD.MINI.IP', expiry='-', good_till_date="2015/02/06 20:00:44",
                            guaranteed_stop='true', level=0.7850, limit_distance=200.0, limit_level='', size=1, stop_distance=45.0, stop_level='',
                            time_in_force='GOOD_TILL_CANCELLED', order_type='LIMIT')

    print response
    try:
        if response['dealStatus'] == 'CANCELLED':
            print 'Check current prices and adjust \'lavel\''
    except Exception, e:
        print 'Order submission error. Check current prices and adjust \'lavel\''

if __name__ == '__main__':
    test_ig_service()