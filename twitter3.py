from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

ckey = 'UR1lpFR9HwtMTS5q1bDDvOfOM'
csecret = 'xOquUCjBrvlRGk16vgcFIhW7DGCehGoPUeC4DFhsFEMSzXM4hg'
atoken = '384070998-iNJFYX0hWuojspEcwHocfc2DduiXreOsjNnzaXfT'
asecret = 'kLgRsJhpokLu1WnjoSI2G3egKDYqQcp76JWLevqZyVYQA'

class listener(StreamListener):

	def on_data(self, data):
		#print(data)
		tweet = data.split(',"text":"')[1].split('","source')[0]
		#print(tweet)
		time = data.split('"created_at":"')[1].split('","id')[0]
		print(tweet + "::" + time)
		saveMe = time + '::' + tweet + '\n'
		output = open('twitter.csv','a')
		output.write(saveMe)
		output.close()
		return True
		
	def on_error(self, status):
		print(status)
		
auth = OAuthHandler(ckey, csecret)	
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["@ES"])

