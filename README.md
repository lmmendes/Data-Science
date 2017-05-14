# Faber-Ventures-Challenge

This is a simple python recommendation engine based on a movie reviews dataset from Amazon. 

# How to use:

- Download the 'movies.txt' dataset from http://snap.stanford.edu/data/web-Movies.html and place it on the data folder;
- Run 'python txt_to_csv.py' to convert and filter the dataset;
- When the conversion ends run 'python recommender.py <user_id>';
- A list of 5 movie recommendations will appear on your terminal.

# Relevant python libraries used:

- Pandas (http://pandas.pydata.org)
- Numpy (http://www.numpy.org)

# Overview of the algorithm:

- The first step is calculating the similarity between every pair of movies. This similarity is the correlation between the ratings given to movie X and the ones given to movie Y.
- The next step is making a prediction of what would be the rating given by <user_id> to each movie X. The value is calculated using the ratings given by the user to the movies he has reviewed and the similarity between said movies and movie X.
- The recommended movies are the ones with a higher predicted rating.

# Notes on possible improvements/extensions:

- The next addition to this program would be a web scrapper which would extract informations on the recommended movies from the Amazon website (for example title and year).
- This is a simple recommender engine, implementing a machine learning algorithm would make it more complex but also more powerful.
