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

############################

#calculates similarity between two products
def sim(product1,product2):

    product1a=product1-product1.mean()
    product2a=product2-product2.mean() 
    
    num= np.sum(product1a*product2a)
    den= np.sqrt(np.sum(product1a**2))*np.sqrt(np.sum(product2a**2))
    
    if num==0:
        result=0
    else:
        result =num/den
    
    return result
    
#############################

#predicts rating the user would give to a certain movie
def predict(user_ratings,similarity):
    
    norm_ratings=(2*user_ratings-6)/4
    num = np.sum(norm_ratings*similarity)
    den = np.sum(np.absolute(similarity))

    if den==0:
        result = 0
    else:    
        result =2*(num/den)+3

    return result

#############################

def main():
    user= sys.argv[1]
    
    reviews_path = './data/reviews.csv'
    
    #saves the data from the csv file to a pandas dataframe
    #here I use only 7.000 rows of data due to how long the program takes to run (also because my computer is too slow)
    data = pd.read_csv(reviews_path,nrows=7000)
    
    #saves all the reviewed movies to a series
    all_products = data.productid.unique()
    
    #saves the movies reviewed by the user and their ratings
    user_products = data[data.userid == user].productid
    user_ratings = data[data.userid == user].score
    
    #filters user who made less than 5 reviews
    if len(user_products)>=5:
    
        pred_result= pd.Series()
        #loops through all the movies
        for product in all_products:
            
            #saves the users who reviewed the movie
            reviewers = data[data.productid == product].userid
            
            #filters movies who had less than 5 reviews
            if len(reviewers)>=5:
            
                sim_result= pd.Series()
                for p in all_products:
                    new_data= data[data.productid.isin([product,p])]
                    data_table=pd.pivot_table(new_data,index=["userid"],columns=["productid"],values="score")
                    
                    #similarity between two movies
                    similarity = sim(data_table[product],data_table[p]) 
                    sim_result.set_value(p,similarity)
            
                sim_result= sim_result.drop(product).sort_values(ascending = False)
                
                #saves the similarity values for the movies seen by our user
                S=sim_result.get(user_products).fillna(0)
                
                #if the similarity series is empty we don't predict a rating
                if not S.nonzero():
                    continue
                else:
                    user_ratings.index=S.index
            
                    #predicted rating for the movie
                    predicted= predict(user_ratings,S)
                    
                    if predicted>4 and product not in user_products:
                        pred_result.set_value(product,predicted)
            else:
                continue
                
        final_result = pred_result.sort_values(ascending=False)[:5]
        
        #prints list of 5 recommended movies in order
        print('We recommend the following movies based on your preferences:')
        for movie in final_result.index:
                print movie  
                    
    else:
        print("\n --> This user doesn't have enough reviews. Please choose another user.")  
            
    #prints running time        
    print("--- Time4: %s seconds ---" % (time.time() - start_time))
    
if __name__ == "__main__":
    main()