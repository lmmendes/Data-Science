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


def convert(string):

    i= string.find('/')
    a = float(string[:i])
    b = float(string[i+1:])
    if b!=0:
        result = a/b
    else:
        result = 0
        
    return result

#file paths
movies_path = './data/movies.txt'
reviews_path = './data/reviews.csv'

movies = open(movies_path, 'rb')
reviews = open(reviews_path, 'wb')
writer = csv.writer(reviews)

columns = ['productid','userid','score']

#writes header of 'reviews.csv'
writer.writerow(columns)

dict={}
for line in movies:
    line = line.strip()
    
    #there is an empty line after each review entry
    if not line:
        helpfulness = dict.get('helpfulness')
        if helpfulness >= 0.5:
            writer.writerow([dict.get(column) for column in columns])
            dict={}
        else:
            dict={}
    else:
        #the key should have the same name as the columns
        end = line.find(':')
        start = line.find('/')
        key = line[start+1:end]
        key = key.lower().strip()
        
        string_value = line[end+1:]
        
        if key == 'helpfulness':
            value = convert(string_value)
        else:
            value = string_value.strip()
        
        dict[key] = value
        
if dict:
    writer.writerow([dict.get(column) for column in columns])


print('File converted successfully!')
print("--- Time: %s seconds ---" % (time.time() - start_time))

#closes files
movies.close()
reviews.close()