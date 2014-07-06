import sys
import json

def main():
    afinnfile = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    scores = {}
    for line in afinnfile:
        term, score  = line.split("\t")
        scores[term] = int(score)

    for line in tweet_file:
        tweet = json.loads(line)
        tweet_text = tweet.get('text', None)
        if tweet_text:
            tweet_score = 0
            not_found = []
            for word in tweet_text.split(" "):
                word_score = scores.get(word, 0)
                tweet_score =+ word_score
                if word_score == 0:
                    not_found.append(word)
            for word in not_found:
                print "%s %d" % (word, tweet_score)

if __name__ == '__main__':
    main()
