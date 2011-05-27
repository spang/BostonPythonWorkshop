import twitter

import optparse
import sys
import os

def encode(tweet):
    """
    Encode a tweet so it can be safely printed to the
    terminal, depending on operating system type.
    """
    if os.name == 'nt':     # Windows
        encoding = 'cp437'
    else:
        encoding = 'utf8'   # Mac / Linux
    return tweet.GetText().encode(encoding, 'xmlcharrefreplace')

def search(search_term):
    """
    Print recent tweets containing `search_term`.
    """
    api = twitter.Api()
    tweets = api.GetSearch(search_term)
    for tweet in tweets:
        print encode(tweet)

def trending_topics():
    """
    Print the currently trending topics.
    """
    api = twitter.Api()
    trending_topics = api.GetTrendsCurrent()
    for topic in trending_topics:
        print topic.name

def user_tweets(username):
    """
    Print recent tweets by `username`.
    """
    pass

def main(args):
    parser = optparse.OptionParser("""Usage: %prog [-s <search term> | -t | -u <username>]""")

    parser.add_option("-s", "--search",
                      type="string",
                      action="store",
                      dest="search_term",
                      default=None,
                      help="Display tweets containing a particular string.")
    parser.add_option("-t", "--trending-topics",
                      action="store_true",
                      dest="trending_topics",
                      default=False,
                      help="Display the trending topics.")

    (opts, args) = parser.parse_args(args)

    if opts.search_term:
        search(opts.search_term)
    elif opts.trending_topics:
        trending_topics()

if __name__ == "__main__":
    main(sys.argv[1:])
