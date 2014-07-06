import sys
import json

def main():
    tweet_file = open(sys.argv[1])

    terms = {}  

    for line in tweet_file:
        tweet = json.loads(line)
        tweet_text = tweet.get('text', None)
        if tweet_text:
            for word in tweet_text.split(" "):
                word = word.strip()
                if word:
                    try:
                        terms[word] += 1
                    except:
                        terms[word] = 1

    for term in terms:
        term_frequency = terms[term] / float(len(terms))
        print "%s %f" % (term, term_frequency)

if __name__ == '__main__':
    main()
