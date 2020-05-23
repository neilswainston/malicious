
'''dailymalicious.'''
import feedparser as f
import markovify as m

_URL = 'feed://www.dailymail.co.uk/articles.rss'
_ENTS = [[e.title, e.summary] for e in f.parse(_URL).entries]

for _ in range(100):
    print(m.Text([x for ent in _ENTS for x in ent]).make_short_sentence(140))
