'''
Daily Mailicious (c) Neil Swainston 2020

CodonGenie is licensed under the MIT License.

To view a copy of this license, visit <http://opensource.org/licenses/MIT/>.

@author:  neilswainston
'''
# pylint: disable=invalid-name
import sys
import traceback
import uuid

from flask import Flask, jsonify

from tweet_factory import get_tweets
from tweeter import tweet


# Configuration:
DEBUG = False
SECRET_KEY = str(uuid.uuid4())

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/test/<num>')
def test(num):
    '''Test.'''
    return jsonify(get_tweets(int(num)))


@app.route('/publish/<num>')
def publish(num):
    '''Publish.'''
    tweets = get_tweets(int(num))
    return tweet(tweets)


@app.errorhandler(Exception)
def handle_exception(err):
    '''Exception handling method.'''
    exc_type, exc_value, exc_traceback = sys.exc_info()
    traceback.print_exception(exc_type, exc_value, exc_traceback)
    response = jsonify({'message': err.__class__.__name__ + ': ' + str(err)})
    response.status_code = 500
    return response


def main(argv):
    '''main method.'''
    if argv:
        app.run(host='0.0.0.0', threaded=True, port=int(argv[0]))
    else:
        app.run(host='0.0.0.0', threaded=True)


if __name__ == '__main__':
    main(sys.argv[1:])
