import sys, json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
	# sent_file = open(sys.argv[1])
	# tweet_file = open(sys.argv[2])
	# hw()
	# lines(sent_file)
	# lines(tweet_file)
	afinnfile = open(sys.argv[1])
	scores = {}	# initialize an empty dictionary
	for line in afinnfile:
 		term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
  		scores[term] = int(score)  # Convert the score to an integer.

	# print scores.items() # Print every (term, score) pair in the dictionary
	# tweets = open("problem_1_submission.txt")
	tweets = open(sys.argv[2])
	for tweet in tweets:
		tweetDict = json.loads(tweet)
		if tweetDict.has_key(u'text'):
			tscore = 0
			contents = tweetDict['text'].strip().split()
			for content in contents:
				if scores.has_key(content):
					tscore += scores[content]
			print tscore				
		else:
			print str(0)

if __name__ == '__main__':
    main()
