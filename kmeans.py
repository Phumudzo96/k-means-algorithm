import matplotlib.pyplot as plt
import math
import csv
import random

# Firstly, defining the function to calculate the distance between two points on the graph.
def distance_between_points(point1, point2):
    return math.sqrt((point2[1] - point1[1]) ** 2 + (point2[0] - point1[0]) ** 2)

# Then defining a function to take in a list of points and calculate the mean point to return e.g. [x, y].
def xy_mean(points):
    y = 0
    x = 0
    for p in points:
        x += p[0]
        y += p[1]
    return [
        x / len(points),
        y / len(points),
    ]

# This function calculates the nearest center point for an individual point, i.e. compares one point 'point' to a list
# of 'center_points' and once the smallest distance is found, it returns the index of the smallest distance.
# The index of the smallest distance is important because it will reference the mean point with the smallest distance.
def pick_nearest_center_point_idx(center_points, point):
    closest_center_point_idx = 0
    distance_to_closest_center_point = distance_between_points(center_points[0], point)

    for center_point_idx, center_point in enumerate(center_points):
        this_distance = distance_between_points(center_point, point)
        if this_distance < distance_to_closest_center_point:
            distance_to_closest_center_point = this_distance
            closest_center_point_idx = center_point_idx

    return closest_center_point_idx


# def build_clusters(center_points, points): cluster[]
# given some center points and points - build and return clusters
# This function allows for a list of dictionaries to be built, which have the correct number of clusters (i.e. center
# points) as inputed by the user.
# The points are then placed into the correct cluster with the nearest center point.
def build_clusters(cpoints, points):
    clusters = [{'center_point': cpoint, 'data_points': []} for cpoint in cpoints]
    # we have a list of clusters with only the center point set
    # [
    #   {'center_point': [1, 2], 'data_points': []},
    #   {'center_point': [3, 5], 'data_points': []},
    #   ...
    # ]

    # place each point into the cluster with the nearest center point
    for point in points:
        nearest_center_point_idx = pick_nearest_center_point_idx(cpoints, point)
        clusters[nearest_center_point_idx]['data_points'].append(point)

    return clusters

# Starting the main execution of the program.
if __name__ == '__main__':

    # Firstly, a list variable is used to store the x, y values from the given CSV file of country data.
    country_data = []

    # Opening csv file and storing the data into x and y values and thereafter appending each point as a separate list
    # to the 'country_data' list variable; this will become a list of lists with each point at a separate list item.
    with open('dataBoth.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')

        for row in readCSV:
            if row[0] != 'Countries':
                birth = float(row[1])
                life = float(row[2])

                country_data.append([birth, life])

    # Welcome message and getting input from the user concerning the number of clusters and iterations they wish to use.
    print('Welcome to the K-Means Algorithm Program.')
    no_clusters = int(input('\nHow many clusters would you like to include? '))
    no_iterations = int(input('\nHow many iterations would you like to run? '))

    # Setting a list variable to store the calculated clusters.
    built_clusters = []

    # Now to perform the clustering, this loop runs the number of times/ iterations specified by the user.
    # For the first loop, no mean has been set, therefore when 'i == 0', random points are drawn, depending on the
    # number of clusters specified by the user. They are then stored in the list 'cluster_center_points'.
    for i in range(no_iterations):
        # Variable set to display sum of squared distances for each iteration below.
        iteration_sum_distances = 0.0

        if i == 0:
            # First iteration draws random mean points from the list of lists, 'country_data'.
            cluster_center_points = random.sample(country_data, no_clusters)
        else:
            # Thereafter, new means are calculated within the clusters and added to the list.
            cluster_center_points = [xy_mean(c['data_points']) for c in built_clusters]

        # Setting a list with dictionaries, i.e. 'center_point': [[x, y], 'data_points': [x, y], [x, y]] etc.
        # This will have the number of clusters as inputed and place the data points in the correct clusters.
        built_clusters = build_clusters(cluster_center_points, country_data)

        # This part was added in for compulsory task 2.
        # This calculates the squared distances for each point and the mean for each iteration and displays it.
        for cluster in built_clusters:
            mean = cluster['center_point']

            for point in cluster['data_points']:
                iteration_sum_distances += distance_between_points(point, mean)


        print(f"\nSum of squared distances for iteration {i + 1} is {iteration_sum_distances}.")


    # Creating the figure for the graph and setting appropriate headings.
    figure = plt.figure()
    plt.title('Birth Rates and Life Expectancies in Countries Across the World')
    plt.xlabel('Birth Rates')
    plt.ylabel('Life Expectancies')
    # Setting variables to store the number of countries, cluster count and list of country names to display.
    # Number of countries will also be used to calculate the means for x and y.
    cluster_count = 1
    country_list = []
    # Now looping through the clusters to plot the points and print out various information regarding the results.
    # Random colors are chosen for each cluster, depending on the number of clusters chosen.
    for cluster in built_clusters:
        r = random.random()
        b = random.random()
        g = random.random()

        # Color list created with random choices.
        color = [[r, g, b]]

        no_countries = 0

        # Looping through each point in each cluster's list of points.
        # Point values are separated to x and y, so as to calculate the sums and then average values for each cluster.
        for point in cluster['data_points']:
            x = point[0]
            y = point[1]
            sum_x = 0
            sum_y = 0
            sum_x += x
            sum_y += y

            # Scattering each point onto the graph with its cluster color.
            plt.scatter(point[0], point[1], c=color)

            # Incrementing country count for each point in a cluster.
            no_countries += 1

            # Opening the file to check which countries have been placed in each cluster.
            # If the point matches the country listed in the file, the country name is added to 'country_list'.
            with open('dataBoth.csv') as csvfile:
                readCSV = csv.reader(csvfile, delimiter=',')

                for row in readCSV:
                    if row[0] != 'Countries' and x == float(row[1]) and y == float(row[2]):
                        country_name = str(row[0])
                        country_list.append(country_name)

        # Displaying results related to number of number of countries, list of country names and x and y means for each
        # cluster.
        print(f"\nCluster {cluster_count} contains {no_countries} countries.")
        print(f"\nThe list of countries in cluster {cluster_count} is {country_list}")
        print(f"\nCluster {cluster_count} birth rate = {sum_x / no_countries}")
        print(f"\nCluster {cluster_count} life expectancy = {sum_y / no_countries}")

        # Clearing the country_list of names to start afresh for the next iteration/ next cluster.
        # Also iterating the cluster count for reference.
        country_list.clear()
        cluster_count += 1


    # Displaying the plotted clusters.
    plt.show()





