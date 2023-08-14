#!/usr/bin/python3

'''
queries the Reddit API and returns a list containing the
title of hot articles listed for a given subreddit
'''

import json
import requests


def recurse(subreddit, hot_list=None, after=None, count=0):
    '''
    queries REDDDIT API returns list of titles
    of hot for subreddit
    '''
    if hot_list is None:
        hot_list = []

    try:
        if after is None:
            subreddit_URL = 'https://www.reddit.com/r/{}/hot.json'.format(
                subreddit
            )
        else:
            subreddit_URL = 'https://www.reddit.com/r/{}/hot.json?after={}'\
                .format(subreddit, after)
        subreddit_info = requests.get(
            subreddit_URL,
            headers={'user-agent': 'user'},
            allow_redirects=False
        ).json()

        if 'data' not in subreddit_info and hot_list == []:
            return None
        children = subreddit_info.get('data').get('children')
        for child in children:
            hot_list.append(child.get('data').get('title'))
            count += 1
        after = subreddit_info.get('data').get('after')
        if after is None:
            return hot_list
        return (recurse(subreddit, hot_list, after, count))
    except Exception:
        return
