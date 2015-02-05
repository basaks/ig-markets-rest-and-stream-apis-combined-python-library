#!/usr/bin/env python
# -*- coding: utf-8 -*-

from trading_ig import IGService

from utils_igmarkets.trading_ig_config import Config as config


ig_service = IGService(config.username, config.password, config.api_key, config.acc_type)
ig_service.create_session()

open_positions = ig_service.fetch_open_positions()
print("open_positions:\n%s" % open_positions)

print("")

epic = 'CS.D.USDJPY.MINI.IP'
# telstra: AA.D.TLS.CASH.IP
# "epic": "CS.D.USDJPY.MINI.IP",
resolution = 'min'
num_points = 10
response = ig_service.fetch_historical_prices_by_epic_and_num_points(epic, resolution, num_points)
df_ask = response['prices']['ask']
print("ask prices:\n%s" % df_ask)