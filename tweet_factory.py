'''
Daily Mailicious (c) Neil Swainston 2020

Daily Mailicious is licensed under the MIT License.

To view a copy of this license, visit <http://opensource.org/licenses/MIT/>.

@author:  neilswainston
'''
import feedparser
import markovify


def get_tweets(num, hashtags, url='feed://www.dailymail.co.uk/articles.rss'):
    '''Get Tweets.'''
    ents = [[ent.title, ent.summary] for ent in feedparser.parse(url).entries]

    return [_get_tweet(ents, hashtags) for _ in range(num)]


def _get_tweet(ents, hashtags):
    '''Get Tweet.'''
    while True:
        tweet = markovify.Text([val for ent in ents
                                for val in ent]).make_short_sentence(140)

        tweet = _add_hashtags(tweet, hashtags)

        if len(tweet) < 140:
            return tweet


def _add_hashtags(tweet, hashtags):
    '''Add hashtags.'''
    tags = tweet.split()
    new_tags = []
    idx = 0

    while idx < len(tags):
        increment, new_tag = _get_hashtag(tags[idx:], hashtags)
        new_tags.append(new_tag)
        idx += increment

    return ' '.join(new_tags)


def _get_hashtag(tags, hashtags):
    '''Get hashtag.'''
    potential_hashtag = '#'

    for idx, tag in enumerate(tags):
        potential_hashtag += tag.lower()

        for hashtag in hashtags:
            if potential_hashtag == hashtag.lower():
                return idx + 1, hashtag

    return 1, tags[0]
