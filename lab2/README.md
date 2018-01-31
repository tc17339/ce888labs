In the vehicles.py, I creat four pictures,including 2 scaterplots and  2 histograms. They proved a more intuitional analyz way from csv file of vehicles. In the new_bootstrap, the code calculated the standard deviation and found the upper bound and lower bound.

![logo](./hist_vehi.png?raw=true)

This histogram show the relation between the day and sales.as you can see it draw the distribution of those number. You can easies concluded some information from this histogram. we can see the 30 to 35 days have the highest sales in the cars.

![logo](./scate_vehi.png?raw=true)

This is the scatterplots of vehicles.csv. This picture show the distribution of current fleet and new fleet.Thorough this scatterploy, you can see the how far the each point.It's easy to achieved through the python.

In the new_bootstrap.py,  This is used to  find the confidence interval. I used
function:

def boostrap(statistic_func, iterations, data)

The function would return 3 parameters,it's mean ,lower bound and  upper bound.
data = df.values.T[0]
data = df.values.T[1] This is used to restore the first and second columns, then called the bootstrap function.
