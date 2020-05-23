'''
Daily Mailicious (c) Neil Swainston 2020

CodonGenie is licensed under the MIT License.

To view a copy of this license, visit <http://opensource.org/licenses/MIT/>.

@author:  neilswainston
'''
from twython import Twython

from auth import consumer_key, consumer_secret, access_token, \
    access_token_secret


def tweet(tweets):
    '''Tweet.'''
    response = []

    twitter = Twython(consumer_key, consumer_secret, access_token,
                      access_token_secret)

    for status in tweets:
        response.append(twitter.update_status(status=status))

    return response
