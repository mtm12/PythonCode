from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import subjectivity
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import *
from nltk.sentiment.vader import SentimentIntensityAnalyzer
#import matplotlib.pyplot as plt
#import matplotlib.animation as animation
#from matplotlib import style

#import time

#style.use("ggplot")

ckey = 'o3fwB4Zx9oUwKLgQ4EaCt23U4'
csecret = 'fshLSCOdobU0LzGbSd4UbuOvpT4RBYauPUKTHSU1DJRRyupeE0'
atoken = '384070998-j7zDgdwksKYxdBRT6NW5MRrV52zdvseprmgud3LJ'
asecret = 'tSSdEO02yQwtXPpKNTrkkv42cP5O8nK2OPm8p3y3TxAqQ'

totalScore = 0 
x = 0

class listener(StreamListener):

	def on_data(self, data):

		try:
                  #print(data)
                  global totalScore
                  global x                 
                  tweet = data.split(',"text":"')[1].split('","source')[0]
                  time = data.split('"created_at":"')[1].split('","id')[0]
                  #print(time + "::" + tweet)
                  ss = sid.polarity_scores(tweet)
                  sumation = ss['pos'] - ss['neg']
                  totalScore = sumation + totalScore
                  #print(sumation)
                  #print(totalScore)
                  x +=1
                  outputScore = open('twitter_trump_score2.txt','a')
                  outputScore.write(str(x) + "," + str(totalScore) + "," + str(time))
                  outputScore.write('\n')
                  outputScore.close()
                  return True
			
		except Exception as e:
                  print(e)
                  print('from on_data')
                  pass
		
	def on_error(self, status):
         print(status)
         print('from on_error')
         pass
              
try:
               
        n_instances = 100
        subj_docs = [(sent, 'subj') for sent in subjectivity.sents(categories='subj')[:n_instances]]
        obj_docs = [(sent, 'obj') for sent in subjectivity.sents(categories='obj')[:n_instances]]
        len(subj_docs), len(obj_docs)
        subj_docs[0]
        train_subj_docs = subj_docs[:80]
        test_subj_docs = subj_docs[80:100]
        train_obj_docs = obj_docs[:80]
        test_obj_docs = obj_docs[80:100]
        training_docs = train_subj_docs+train_obj_docs
        testing_docs = test_subj_docs+test_obj_docs
        sentim_analyzer = SentimentAnalyzer()
        all_words_neg = sentim_analyzer.all_words([mark_negation(doc) for doc in training_docs])
        unigram_feats = sentim_analyzer.unigram_word_feats(all_words_neg, min_freq=4)
        len(unigram_feats)
        sentim_analyzer.add_feat_extractor(extract_unigram_feats, unigrams=unigram_feats)
        training_set = sentim_analyzer.apply_features(training_docs)
        test_set = sentim_analyzer.apply_features(testing_docs)
        trainer = NaiveBayesClassifier.train
        classifier = sentim_analyzer.train(trainer, training_set)
        for key,value in sorted(sentim_analyzer.evaluate(test_set).items()):
                print('{0}: {1}'.format(key, value))
        
        sid = SentimentIntensityAnalyzer()
        
        auth = OAuthHandler(ckey, csecret)	
        auth.set_access_token(atoken, asecret)
        twitterStream = Stream(auth, listener())
        #twitterStream.filter(track=["googl", "google", "goog"])
        twitterStream.filter(track=["trump"], stall_warnings=True)
      
except Exception as e:
        print(e)
        print('e')
        pass

