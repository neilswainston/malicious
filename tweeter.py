'''
Daily Mailicious (c) Neil Swainston 2020

Daily Mailicious is licensed under the MIT License.

To view a copy of this license, visit <http://opensource.org/licenses/MIT/>.

@author:  neilswainston
'''
import twython

from auth import APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET


def tweet(tweets):
    '''Tweet.'''
    response = []

    twitter = twython.Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN,
                              OAUTH_TOKEN_SECRET)

    for status in tweets:
        response.append(twitter.update_status(status=status))

    return response


def get_hashtags(woeid=23424975):  #  UK
    '''Get hashtags.'''
    twitter = twython.Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN,
                              OAUTH_TOKEN_SECRET)

    trends = twitter.get_place_trends(id=woeid)[0]

    return [trend['name'] for trend in trends['trends']
            if trend['name'][0] == '#']
