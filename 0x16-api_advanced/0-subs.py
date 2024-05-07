#!/usr/bin/python3
"""
Script that queries subscribers on a given Reddit subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://oauth.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
            "User-Agent": "linux:api.request.red:v1.0.0 (by /u/ouarrar23)",
            'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IlNIQTI1NjpzS3dsMnlsV0VtMjVmcXhwTU40cWY4MXE2OWFFdWFyMnpLMUdhVGxjdWNZIiwidHlwIjoiSldUIn0.eyJzdWIiOiJ1c2VyIiwiZXhwIjoxNzE1MjA1ODA4Ljk4MjU5OSwiaWF0IjoxNzE1MTE5NDA4Ljk4MjU5OSwianRpIjoiOXZXeVJVUmlJWXNRU2J1M3V3Q1EzcWt4WWJSczlnIiwiY2lkIjoiS1hsRFRzMEo0QTlhS3p0bHdhLXBXUSIsImxpZCI6InQyX3p3NGZscXRkcyIsImFpZCI6InQyX3p3NGZscXRkcyIsImxjYSI6MTcxNTExNzg3MjcxMiwic2NwIjoiZUp5S1Z0SlNpZ1VFQUFEX193TnpBU2MiLCJmbG8iOjl9.rzSD8ZWpqEvALrN9yHKuDDVS6tCP9b8poUj_7wKKS5Tp0wmRKp8Sa-bP61KmWAgnxhEwjJ294U-qEcQ-0MCQHlD2KN1TG2wUqNzZWN6zQNZmaVnI67RK0G54O8_9Ra4OoBIzxLSMVmSzhAVuIi1GtwlSqt0YZBW_mhWbMsYxj4iVh_LJfEYcJ_XkpUKvX_Z2Eeqt-BtsNVsUiboAjzyjlGoQnkdMN9HPRGKSVkAMzEowA-bWlyX6d_yCFBLUE4KzaYqq4VeHwrMSxS80ktkWAbHmSTUrF-Tpd_Rmk6bTpTQMgb4IY2356KNdXsYjPZ-rjnL44t9lw09uTuRg3JzmjA'
            }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0

