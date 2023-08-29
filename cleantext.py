import numpy as np
import pandas as pd
import re
import sys

from bs4 import BeautifulSoup
from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords




tokenizer = RegexpTokenizer(r'\w+')
en_stopwords = set(stopwords.words('english'))
ps = PorterStemmer()

def remove_emoji(review):
    
    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', review)

def remove_review_digits(review):
    review = re.sub(r'[d]+', r'', review)
    review = re.sub(r'[0-9]*','',review)
    review = re.sub(r'([0-9]*\-[0-9]*)*', '', review)
    return review

def remove_chars(review):
    review = re.sub(r'[/(){}\[\]\|]', '', review)
    review = re.sub(r'[!$%^?&*><]', '', review)
    review = re.sub(r'[\'\"،—.,;+-=]', '', review)
    review = re.sub(r'[\n]', '', review) # removing \n
    review = re.sub(r"\s+",' ',review) # remove_extra_white_space
    return review

    

def getcleanedReview(review):
    
    review = review.lower()
    review = remove_emoji(review) # remove if any emoji present
    review =  re.sub(r'http[^\s]*','',review)
    review = BeautifulSoup(review, "lxml").text
    review = remove_review_digits(review)
    review = remove_chars(review)
    
    
    #tokenize
    tokens = tokenizer.tokenize(review)
    new_token = [token for token in tokens if token not in en_stopwords]
    stemmed_token = [ps.stem(token) for token in new_token]
    
    cleaned_review = ' '.join(stemmed_token)
    
    return cleaned_review

# #one method to accept input file and return clean ouput file of movie reviews
# def getStemmedDocument(inputfile, outputfile):

#     out = open(outputfile, 'w', encoding= 'utf8')
#     with open(inputfile, encoding='utf8') as f:
#         reviews = f.readlines()
    
#     for review in reviews:
#         cleaned_review = getstemmedReview(review)
#         print( (cleaned_review) , file= out)

#     out.close()

# #read command line arguments
# inputfile = sys.argv[1]

# outputfile = sys.argv[2]

# getStemmedDocument(inputfile, outputfile)