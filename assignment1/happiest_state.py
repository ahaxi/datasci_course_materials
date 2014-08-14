import sys, json

states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
	afinnfile = open(sys.argv[1])
	scores = {}	# initialize an empty dictionary
	for line in afinnfile:
 		term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
  		scores[term] = int(score)  # Convert the score to an integer.

	# print scores.items() # Print every (term, score) pair in the dictionary
	# tweets = open("problem_1_submission.txt")
	happy = {}
	tweets = open(sys.argv[2])
	for tweet in tweets:
		tweetDict = json.loads(tweet)
		if tweetDict.has_key(u'user'):
			if tweetDict['user'].has_key(u'location'):
				address = tweetDict['user']['location']
				if len(address.split(",")) == 2:
					state = address.split(",")[1].strip().upper()
					if states.has_key(state):
						if tweetDict.has_key(u'text'):
							tscore = 0
							contents = tweetDict['text'].strip().split()
							for content in contents:
								if scores.has_key(content):
									tscore += scores[content]
						if happy.has_key(state):
							happy[state][0] += tscore
							happy[state][1] += 1
						else:
							happy.update({state:[tscore, 1]})
	happiest = ""
	maxAverage = 0
	for h in happy:
		if happy[h][0]/float(happy[h][1]) > maxAverage:
			maxAverage = happy[h][0]/float(happy[h][1])
			happiest = h
	print happiest



if __name__ == '__main__':
    main()
