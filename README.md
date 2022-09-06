# k-means-algorithm
Open the ﬁle kmeans.py, in which comments have been included to help
guide you.  Take a look at the data provided, which consists of the two
variables (life expectancy, birth rate) measured for each country, and note
that there is one dataset for 2008 and one from 1953. This data is in csv ﬁle
format, which can be opened just like a text ﬁle. Open each ﬁle and take a
look at how the data is laid out. Your algorithm should work on either data
set.
●
To assist you in implementing the k-means algorithm, consider writing
functions that can do the following:
○
Find the Euclidean distance between two points, each of which has
an and a coordinate.
○
Find the distance to each of the centroids from each of the points.
Ie. If you have 15 points and 3 centroids, you need to calculate the
distance from each of the 15 points to each of the 3 centroids.
○
Compute the two-dimensional mean. To compute the mean (or
average) of a number of observations, you simply add all the
observations together and then divide by the number of
observations you added together. Thus, to compute the
two-dimensional mean (ie. the mean coordinate point ),
(𝑥, 𝑦)
calculate the mean of the x values and the mean of the y values of
all the points.
○
Read in the data from either of the provided csv ﬁles. Remember
that BirthRate is the ‘x’ value and LifeExpectancy is the  ‘ y’ value.
Hint: after reading in the data from the csv ﬁle, the data should be
in a form where you should easily be able to plot all the data as a
scatter plot to get an idea of what the data distribution looks like.
○
Visualise the data as a scatter plot, with the points in each cluster
shown in a different colour.
●
After doing this, implement the k-means algorithm using the steps
described in the ‘Speciﬁcations of k-means’ section above. You should let
the user decide how many clusters (k) there should be (although it might
make sense to begin with just two clusters, and generalise later, i.e. k=2).
The algorithm will need to run for a user-speciﬁed number of iterations,
though to begin you can hard-code this in with the value 6 and update
this later. You do not need to monitor the algorithm for convergence at
this point.
●
Once the algorithm has run, it should also output:
1.) The number of countries belonging to each cluster
2.) The list of countries belonging to each cluster
3.) The mean Life Expectancy and Birth Rate for each cluster
●
At the beginning of kmeans.py, please present the algorithm and how
you approached it in your own words. You may use docstrings for your
pseudocode. Please remember to reference any work that you reuse.
●
You will use kmeans.py in the following task, so ensure that it is completed
and working properly before moving onto the next task.
