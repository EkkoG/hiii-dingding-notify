#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 ciel <ciel@cieldeMBP>
#

"""
"""

import requests

def send_message(message, tokens):
    para = {"msgtype": "text", "text": {"content": message},"at": {"atMobiles":[]}}

    for token in tokens:
        url = "https://oapi.dingtalk.com/robot/send?access_token={}".format(token)
        r = requests.post(url, json=para)