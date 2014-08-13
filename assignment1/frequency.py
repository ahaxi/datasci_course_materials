import sys, json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
	tweets = open(sys.argv[1])
	tf = {}
	for tweet in tweets:
		tweetDict = json.loads(tweet)
		if tweetDict.has_key(u'text'):
			contents = tweetDict['text'].strip().split()
			for content in contents:
				if tf.has_key(content):
					tf[content] += 1
				else:
					tf.update({content: 1})
	total = 0
	for tfs in tf:
		total += tf[tfs]
	for tfs in tf:
		print tfs, float(tf[tfs])/total

if __name__ == '__main__':
    main()
