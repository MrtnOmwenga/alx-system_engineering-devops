#!/usr/bin/python3
""" Get number of Subscribers of a subreddit """

import requests


def number_of_subscribers(subreddit):
    """ Get number of subscribers """

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    data = requests.get(url, headers={'User-Agent':
                                      '0x16-api_advanced:project:\
v1.0.0 (by /u/firdaus_cartoon_jr)'}).json()
    subs = data.get("data", {}).get("subscribers", 0)
    return (subs)
