from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import subjectivity
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import *
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import mysql.connector

#import time

style.use("ggplot")

ckey = 'zwB3CO7lRQm7TJf11KlbfDDrS'
csecret = 'sPoDu8lxf6P3ghbjuCZur6pwnmhDrlsrrjDA72GiqQiqejPLpP'
atoken = '384070998-HMCt6W2hJYtZP3miMHz03lOnEXicAkwZfRFaUpi9'
asecret = 'q977XvDQQTcdgso16KfoWszGuPpFXFgDTRn6lauR360wy'

totalScore = 0 
#xar = []
#yar = []
x = 0
#y = 0
#fig = plt.figure()
#ax1 = fig.add_subplot(1,1,1)

class listener(StreamListener):

	def on_data(self, data):

		try:
                  #print(data)
                  global totalScore
                  #global xar
                  #global yar
                  global x
                  #global y
                  #global fig
                  #global ax1
                  #global ply
                  
                  tweet = data.split(',"text":"')[1].split('","source')[0]
                  #print(tweet)
                  #time = data.split('"created_at":"')[1].split('","id')[0]
                  #time = time.split(' ')
                  #timestamp = time[1] + " " + time[2] + " " + time[5] + " " + time[3]
                  #print(timestamp)
                  #location = data.split('"location":"')[1].split('","url')[0]
                  #saveMe = time + '::' + tweet + '::' + location + '\n'
                  #print(time + "::" + tweet)
                  #saveMe = time + '::' + tweet + '\n'
                  #output = open('twitter_msft.csv','a')
                  #output.write(saveMe)
                  #output.close()
                  ss = sid.polarity_scores(tweet)
                  #print(ss)
                  #print(ss['neg'])
                  #print(ss['pos'])
                  score = ss['pos'] - ss['neg']
                  
                  cnx = mysql.connector.connect(user='MarcMcLean', database='sentdb', password='mtm1221', host='localhost')
                  cursor = cnx.cursor()
                  #command = ("INSERT INTO `brexit` (`score`, `date`) VALUES (" + str(score) + "," + str(timestamp) + ")")
                  command = ("INSERT INTO `xom` (`score`) VALUES (" + str(score) + ")")
                  cursor.execute(command)
                  cnx.commit()
                  cursor.close()
                  cnx.close()


                  #totalScore = sumation + totalScore
                  #print(sumation)
                  #print(ss['pos'] - ss['neg'])
                  #print(totalScore)
                  #x +=1
                  #outputScore = open('twitter_brexit_score4-1.txt','a')
                  #outputScore.write(str(x) + "," + str(totalScore) + "," + str(sumation) + "," + str(time))
                  #outputScore.write(str(x) + "::" + str(score) + "::" + str(time) + "::" + location + "::" + tweet)
                  #outputScore.write(str(x) + "::" + str(score) + "::" + str(time))
                  #outputScore.write('\n')
                  #outputScore.close()
                  #x +=1
                  #xar.append(x)
                  #yar.append(totalScore)
                  #ax1.clear()
                  #ax1.plot(xar,yar)
                  
                  
                  
                  return True
			
		except Exception as e:
                  print(e)
                  print("1")
                  pass

		
	def on_error(self, status):
                 print(status)
                 print("2")
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
        twitterStream.filter(track=["xom", "exxon", "exxonmobil"])
        #ply.show()
      
except Exception as e:
        print(e)
        print("3")
        pass
     

