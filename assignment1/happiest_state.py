import sys
import operator
import json

states = {
        'Alaska': 'AK',
        'Alabama': 'AL',
        'Arkansas': 'AR',
        'American Samoa': 'AS',
        'Arizona': 'AZ',
        'California': 'CA',
        'Colorado': 'CO',
        'Connecticut': 'CT',
        'District of Columbia': 'DC',
        'Delaware': 'DE',
        'Florida': 'FL',
        'Georgia': 'GA',
        'Guam': 'GU',
        'Hawaii': 'HI',
        'Iowa': 'IA',
        'Idaho': 'ID',
        'Illinois': 'IL',
        'Indiana': 'IN',
        'Kansas': 'KS',
        'Kentucky': 'KY',
        'Louisiana': 'LA',
        'Massachusetts': 'MA',
        'Maryland': 'MD',
        'Maine': 'ME',
        'Michigan': 'MI',
        'Minnesota': 'MN',
        'Missouri': 'MO',
        'Northern Mariana Islands': 'MP',
        'Mississippi': 'MS',
        'Montana': 'MT',
        'National': 'NA',
        'North Carolina': 'NC',
        'North Dakota': 'ND',
        'Nebraska': 'NE',
        'New Hampshire': 'NH',
        'New Jersey': 'NJ',
        'New Mexico': 'NM',
        'Nevada': 'NV',
        'New York': 'NY',
        'Ohio': 'OH',
        'Oklahoma': 'OK',
        'Oregon': 'OR',
        'Pennsylvania': 'PA',
        'Puerto Rico': 'PR',
        'Rhode Island': 'RI',
        'South Carolina': 'SC',
        'South Dakota': 'SD',
        'Tennessee': 'TN',
        'Texas': 'TX',
        'Utah': 'UT',
        'Virginia': 'VA',
        'Virgin Islands': 'VI',
        'Vermont': 'VT',
        'Washington': 'WA',
        'Wisconsin': 'WI',
        'West Virginia': 'WV',
        'Wyoming': 'WY'
    }

def main():
    afinnfile = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    scores = {}
    for line in afinnfile:
        term, score  = line.split("\t")
        scores[term] = int(score)

    found = {}
    for line in tweet_file:
        tweet = json.loads(line)
        tweet_text = tweet.get('text', None)
        
        if tweet_text:
            state_code = None
            places = tweet.get('places', None)
            if places:
                name = places.get('name', None)
                if name:
                    if states.get(name, None):
                        state_code = states[name]
            if not state_code:
                user = tweet.get('user', None)
                if user:
                    location = user.get('location', None)
                    if location:
                        if states.get(location, None):
                            state_code = states[location]

            tweet_score = 0
            not_found = []
            for word in tweet_text.split(" "):
                word_score = scores.get(word, 0)
                tweet_score =+ word_score
                if word_score == 0:
                    not_found.append(word)

            if state_code:
                try:
                    found[state_code] = tweet_score        
                except:
                    found[state_code] += tweet_score        

    sorteds = sorted(found.iteritems(), key=operator.itemgetter(1), reverse=True)
    print sorteds[0][0]

if __name__ == '__main__':
    main()
