from nltk.classify import NaiveBayesClassifier
from nltk.corpus import subjectivity
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import *
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize

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
'''
sentences = ["VADER is smart, handsome, and funny.1", "VADER is smart, handsome, and funny!",
"VADER is very smart, handsome, and funny.",
"VADER is VERY SMART, handsome, and FUNNY.",
"VADER is VERY SMART, handsome, and FUNNY!!!",
"VADER is VERY SMART, really handsome, and INCREDIBLY FUNNY!!!",
"The book was good.",
"The book was kind of good.",
"The plot was good, but the characters are uncompelling and the dialog is not great.",
"A really bad, horrible book.",
"At least it isn't a horrible book.",
":) and :D",
"",
"Today sux",
"Today sux!",
"Today SUX!",
"Today kinda sux! But I'll get by, lol"
]

paragraph = "It was one of the worst movies I've seen, despite good reviews. \
... Unbelievably bad acting!! Poor direction. VERY poor production. \
... The movie was bad. Very bad movie. VERY bad movie. VERY BAD movie. VERY BAD movie!"

lines_list = tokenize.sent_tokenize(paragraph)
sentences.extend(lines_list)



tricky_sentences = [
"Qualcomm is working with Google to help power future Android Auto platforms",
"Say hello to Google's #Allo!",
"Firebombing at GOOGLE HQ... ",
"Google exec shares her best career advice for 20-somethings",
"Google Home Is A Remote Control For Your House (And Your Life)",
"Google brings Android Pay to ATMs, Chrome and more apps",
"Google\u2019s freshly announced sharing app Spaces could be big: Google Spaces could be perfect"
"Check out GPlayCUBE for a free $25 Google Play code! "
"Wish I was there! Google ATAP team is doing the coolest things right now! https:\/\/t.co\/MnY0Vn03BY",
"Wish I was there! Google ATAP team is doing the coolest things right now!",
"does anyone else have a problem with Google play where its perpetually stuck trying to upload a song and it wont upload other songs?",
"#MazaaSih Google ungkap Rahasia Kepanjangan dari 'www' adalah: Wassalamualaikum Wr Wb\n?39",
"#SEO What marketers need to know about Google Assistant and Google Home https:\/\/t.co\/Rn42Gt4KX6",
"King of dark fantasy. Summon today. App Store: https:\/\/t.co\/pxBnHxh0nF Google Play: https:\/\/t.co\/8WmdkzUyGn #DarkSummoner",
"King of dark fantasy. Summon today. App Store: "
]


sentences.extend(tricky_sentences)
sid = SentimentIntensityAnalyzer()
for sentence in sentences:
     print(sentence)
     ss = sid.polarity_scores(sentence)
     for k in sorted(ss):
         print('{0}: {1}, '.format(k, ss[k]), end='')
     print()

'''
sid = SentimentIntensityAnalyzer()
tweet = "Wish I was there! Google ATAP team is doing the coolest things right now!"
ss = sid.polarity_scores(tweet)
print(ss)
     
     