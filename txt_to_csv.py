# FABER VENTURES CHALLENGE 2017
# Mafalda Jotta Garcia

"""
    Converts dataset file movies.txt to a csv file
    The output file includes the following information for each review:
    Product ID
    User ID
    Score
"""


import csv
import time
start_time = time.time()

#file paths
movies_path = './movies.txt'
reviews_path = './reviews.csv'

movies = open(input_path, 'r')
reviews = open(output_file_path, 'w')
writer = csv.writer(reviews)

columns = ['productid','userid','score']

#writes header of 'reviews.csv'
write.writerow(columns)

dict={}
for line in movies:
    line = line.strip()
    
    #there is an empty line after each review entry
    if not line:
        #----->filter with helpfulness!
        dict={}
    else:
        end = line.find(':')
        key = line[:end]
        start = key.find('/')
        key = line[start:]
        key = key.lower().strip()
        
        if key == 'helpfulness':
            #-------->convert from string to float
            
        else:
            value = line[end+1:]
            value = value.strip()
        
        dict[key] = value
if dict:
    writer.writerow([dict.get(column) for column in columns])



print("--- Time: %s seconds ---" % (time.time() - start_time))

#closes files
movies.close()
reviews.close()