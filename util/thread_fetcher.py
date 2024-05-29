import praw
import re 
import streamlit as st
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

class ThreadFetcher: 
    
    def __init__(self):
        # reddit = reddit = praw.Reddit("bot1", config_interpolation="basic")
        self.reddit = praw.Reddit(
            client_id=st.secrets['bot1']['client_id'],
            client_secret=st.secrets['bot1']['client_secret'],
            user_agent="reddit summarizer",
            username="scr1ptrr",
        )
        # self.reddit = praw.Reddit("bot1", user_agent="reddit summarizer user agent")
        self.reddit.read_only = True
        nltk.download('punkt')
        nltk.download('stopwords')
        nltk.download('wordnet')
    
    # @st.cache_data(ttl=3600)
    def fetchThread(_self, url):
        comment_arr = []
        submission = _self.reddit.submission(url=url)
        submission.comments.replace_more(limit=None)
        comment_list = submission.comments.list()
        for comment in comment_list:
            tokens = _self.tokenize(comment.body)
            comment_arr.append(tokens)
        return (submission, comment_arr)

    def tokenize(self, text):
        #Tokenization
        tokens = word_tokenize(text)

        #Noise
        tokens = [re.sub(r'[^\w\s]', '', token) for token in tokens]

        #Normalization
        tokens = [token.lower() for token in tokens]

        #Stopwords
        stop_words = set(stopwords.words('english'))
        tokens = [token for token in tokens if token not in stop_words]

        #Lemmatization
        lemmatizer = WordNetLemmatizer()
        tokens = [lemmatizer.lemmatize(token) for token in tokens]

        #Empty tokens
        tokens[:] = [item for item in tokens if item != '' ]

        return(tokens)
