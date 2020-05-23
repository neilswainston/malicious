'''
Daily Mailicious (c) Neil Swainston 2020

CodonGenie is licensed under the MIT License.

To view a copy of this license, visit <http://opensource.org/licenses/MIT/>.

@author:  neilswainston
'''
import feedparser
import markovify


def get_tweets(num, url='feed://www.dailymail.co.uk/articles.rss'):
    '''Get Tweets.'''
    ents = [[ent.title, ent.summary] for ent in feedparser.parse(url).entries]

    return [markovify.Text([val for ent in ents
                            for val in ent]).make_short_sentence(140)
            for _ in range(num)]
