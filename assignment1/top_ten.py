import sys
import json
import operator

def main():
    tweet_file = open(sys.argv[1])

    hashs = {}  

    for line in tweet_file:
        tweet = json.loads(line)
        tweet_entities = tweet.get('entities', None)
        if tweet_entities:
            tweet_hashtags = tweet_entities.get('hashtags', None)
            if tweet_hashtags:
                for h in tweet_hashtags:
                    try:
                        hashs[h['text']] += 1 
                    except:
                        hashs[h['text']] = 1


    sorteds = sorted(hashs.iteritems(), key=operator.itemgetter(1), reverse=True)

    i = 0
    for h, f in sorteds:
        if i < 10:
            print "%s %f" % (h, f)
        i += 1 

if __name__ == '__main__':
    main()
