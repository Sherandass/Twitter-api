try:
	import json
except:
	import simplejson as json
import csv


headers = ['INDEX', 'ID', 'TIMESTAMP', 'TWEET', 'LOCATION', 'RETWEET COUNT', 'LIKE COUNT', 'FOLLOWER COUNT', 'VERIFIED STATUS', 'TWEETID']
x =1
with open('dataset3.csv', 'a') as csvfile:
    csv.DictWriter(csvfile, fieldnames=headers).writeheader()
tweets_filename = 'iranfloods.json'
tweets_file = open(tweets_filename, "r")
for line in tweets_file:
	try:
		tweet = json.loads(line.strip())
		if 'text' in tweet:
			print(tweet['user']['screen_name'])
			print(tweet['created_at'])
			print(tweet['text'])
	
			print(tweet['retweet_count'])
			print(tweet['favorite_count'])
			print(tweet['user']['followers_count'])
			print(tweet['user']['verified'])
			print(tweet['id'])
			with open('dataset3.csv',"a") as csvfile:
				writer = csv.DictWriter(csvfile,fieldnames = headers)
				row = {'INDEX':x, 'ID':tweet['user']['screen_name'], 'TIMESTAMP':tweet['created_at'], 'TWEET':tweet['text'], 'RETWEET COUNT':tweet['retweet_count'], 'LIKE COUNT':tweet['favorite_count'], 'FOLLOWER COUNT':tweet['user']['followers_count'], 'VERIFIED STATUS':tweet['user']['verified'], 'TWEETID':tweet['id']}
				writer.writerow(row)
				x = x+1
			hashtags=[]
			for hashtag in tweet['entities']['hashtags']:
				hashtags.append(hashtag['text'])
				print(hashtags)
	except:
		continue