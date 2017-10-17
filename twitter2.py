from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

ckey = 'UR1lpFR9HwtMTS5q1bDDvOfOM'
csecret = 'xOquUCjBrvlRGk16vgcFIhW7DGCehGoPUeC4DFhsFEMSzXM4hg'
atoken = '384070998-iNJFYX0hWuojspEcwHocfc2DduiXreOsjNnzaXfT'
asecret = 'kLgRsJhpokLu1WnjoSI2G3egKDYqQcp76JWLevqZyVYQA'

class listener(StreamListener):

	def on_data(self, data):
		try:
                  print(data)
                  tweet = data.split(',"text":"')[1].split('","source')[0]
                  #print(tweet)
                  time = data.split('"created_at":"')[1].split('","id')[0]
                  #print(time + "::" + tweet)
                  location = data.split('"location":"')[1].split('","url')[0]
                  saveMe = time + '::' + tweet + '::' + location + '\n'
                  #saveMe = data + '\n'
                  output = open('twitter_googl_test.txt','a')
                  output.write(saveMe)
                  output.close()
                  return True
			
		except Exception as e:
			print(e)
	
	
		
	def on_error(self, status):
		print(status)
try:
        auth = OAuthHandler(ckey, csecret)	
        auth.set_access_token(atoken, asecret)
        twitterStream = Stream(auth, listener())
        twitterStream.filter(track=["googl", "google", "goog"])
        #twitterStream.filter(track=["aapl","apple","iphone", "ipad","imac ","mac "])
      
except Exception as e:
	print(e)

