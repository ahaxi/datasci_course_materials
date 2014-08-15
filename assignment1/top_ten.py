import sys, json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
	tweets = open(sys.argv[1])
	hashtags = {}
	for tweet in tweets:
		tweetDict = json.loads(tweet)
		if tweetDict.has_key(u'entities'):
			entities = tweetDict['entities']
			if entities.has_key(u'hashtags'):
				for entity in entities['hashtags']:
					hashtag = entity['text']
					if hashtags.has_key(hashtag):
						hashtags[hashtag] += 1
					else:
						hashtags.update({hashtag:1})
	hashtagss = sorted(hashtags.items(), key = lambda x:x[1], reverse = True)
	count = 0
	for i in range(0,10):
		print hashtagss[i][0], hashtagss[i][1]

if __name__ == '__main__':
    main()
