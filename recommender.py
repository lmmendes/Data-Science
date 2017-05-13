# FABER VENTURES CHALLENGE 2017
# Mafalda Jotta Garcia

"""
Movie recommender engine
    Reads data from Amazon movie review dataset (Movies.txt), 
    found at http://snap.stanford.edu/data/web-Movies.html .
    Gives a list of movie recommendations for a certain user, based on his own and other's reviews. 
"""

import sys
import math
import time
import pandas as pd
import numpy as np


start_time = time.time()

#calculates similarity between two products
def sim(product1,product2):

    product1a=product1-product1.mean()
    product2a=product2-product2.mean() 
    
    num= np.sum(product1a*product2a)
    den= np.sqrt(np.sum(product1a**2))*np.sqrt(np.sum(product2a**2))
    
    result =num/den
    
    return result
    
###########################
#predicts rating the user would give to a certain movie
def predict(user_ratings,similarity,user_products):



    return result

###########################
def main():
    user= sys.argv[1]
    
    reviews_path = './reviews.csv'
    
    data = pd.read_csv(reviews_path)
    
    #saves all the reviewed movies to a series
    all_products = data.productid
    
    #saves the movies reviewed by the user and their ratings
    user_products = data[data.userid == user].productid
    user_ratings = data[data.userid == user].score
    
    
    
    
    
    
    
     print("--- Time4: %s seconds ---" % (time.time() - start_time))
    
if __name__ == "__main__":
    main()