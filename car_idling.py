""" Car Idling Feature """
import matplotlib.pyplot as plt   # Library for plotting
import pandas as pd


def custom_filter(fuel, time, numb_n):
    """Filter to find top N values and plot them"""
    final_list = []
    time_list = []
    for i in range(numb_n):
        max1 = 0
        sample = len(fuel)
        for j in range(sample):
            if fuel[j] > max1:
                max1 = fuel[j]
                time1 = time[j]
        fuel.remove(max1)
        final_list.append(max1)
        time_list.append(time1)
    x_axis = time_list  # x axis values
    y_axis = final_list  # corresponding y axis values
    plt.plot(x_axis, y_axis)  # plotting the points
    plt.xlabel('Time')  # naming the x axis
    plt.ylabel('Fuel(Litre)')  # naming the y axis
    plt.title('Car Idling Analysis-Fuel Wastage On 2nd Nov ')  # graph title
    plt.show()  # function to show the plot


def feature2():
    """Main Function of the feature - car idling"""
    data_f = pd.read_csv('city2.csv')  # Read csv file
    d_f = pd.DataFrame(data_f)  # Create Dataframe
    f_s = 0
    kmpl = d_f['Kilometers Per Litre(Instant)(kpl)']  # Instantaneous Mileage
    distance_km = d_f['Trip Distance(km)']  # Trip Distance
    dist_km = []  # For list conversion
    diff = 0   # Variable to calculate distance covered in each second
    fuel_spent = []  # List for calculating fuel used when vehicle is idle
    for i in distance_km:   # Converting Series to list
        dist_km.append(i)
    sample_size = len(dist_km)  # Finding number of samples
    time = d_f['GPS Time']   # Extracting time values
    sample_distance = []  # Distance covered between two samples
    for i in range(sample_size-1):
        diff = dist_km[i+1]-dist_km[i]  # Distance covered in Km
        sample_distance.append(diff)
    for i in range(sample_size-1):
        f_s = 0
        if kmpl[i] == 0:  # If mileage is zero append zero
            fuel_spent.append(0)
            continue
        f_s = sample_distance[i]/kmpl[i]  # Calculate fuel spent during idling
        fuel_spent.append(f_s)
    total_fuel_spent = sum(fuel_spent)  # Calculate total fuel spent during
    # idling
    print('Plotting time values with maximum fuel wastage')
    curr_time = []  # List to store all the time values in HR:MM:SS format
    for i in range(sample_size-1):
        curr_time.append(time[i][11:19])
    custom_filter(fuel_spent, curr_time, 6)  # Calling function
    print('\nTotal Fuel wasted during the trip in Litres :', total_fuel_spent)
    # Total fuel wasted
