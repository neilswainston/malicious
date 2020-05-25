'''
Daily Mailicious (c) Neil Swainston 2020

CodonGenie is licensed under the MIT License.

To view a copy of this license, visit <http://opensource.org/licenses/MIT/>.

@author:  neilswainston
'''
# pylint: disable=too-few-public-methods
import twython

from auth import APP_KEY, APP_SECRET


class Tweeter():
    '''Class to submit tweets to Twitter.'''

    def __init__(self):
        self.__twython = twython.Twython(APP_KEY, APP_SECRET, oauth_version=2)
        self.__access_token = self.__twython.obtain_access_token()

    def tweet(self, tweets):
        '''Tweet.'''
        response = []

        twitter = twython.Twython(APP_KEY, access_token=self.__access_token)

        for status in tweets:
            response.append(twitter.update_status(status=status))

        return response
