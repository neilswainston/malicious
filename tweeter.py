'''
Daily Mailicious (c) Neil Swainston 2020

CodonGenie is licensed under the MIT License.

To view a copy of this license, visit <http://opensource.org/licenses/MIT/>.

@author:  neilswainston
'''
from twython import Twython

from auth import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, \
    ACCESS_TOKEN_SECRET


def tweet(tweets):
    '''Tweet.'''
    response = []

    twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN,
                      ACCESS_TOKEN_SECRET)

    for status in tweets:
        response.append(twitter.update_status(status=status))

    return response
