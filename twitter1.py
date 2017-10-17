from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

ckey = 'UR1lpFR9HwtMTS5q1bDDvOfOM'
csecret = 'xOquUCjBrvlRGk16vgcFIhW7DGCehGoPUeC4DFhsFEMSzXM4hg'
atoken = '384070998-iNJFYX0hWuojspEcwHocfc2DduiXreOsjNnzaXfT'
asecret = 'kLgRsJhpokLu1WnjoSI2G3egKDYqQcp76JWLevqZyVYQA'

class listener(StreamListener):

	def on_data(self, data):
		print(data)
		return True
		
	def on_error(self, status):
		print(status)
		
auth = OAuthHandler(ckey, csecret)	
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["aapl"])

