""" Feature 2 - Fuel Trim Analysis """
import matplotlib.pyplot as plt   # Library for plotting
import pandas as pd
DATA = pd.read_csv('city2.csv')
D = pd.DataFrame(DATA)     # dataframe conversion


def feature3():
    """Main function of the feature"""
    f_trim = D['Fuel trim bank 1 sensor 1(%)']  # Fuel trim sensor value
    f_trim_mode = ["IT", "NT", "M"]   # Fuel trim has 3 modes
    f_trim_flag = 0       # Flag for non ideal trim
    index = 0
    count = 0
    f_trim_mil = 0        # Indicator for fuel trim malfunction
    f_plot = []  # Conversion from series to list
    t_plot = []
    time = D['GPS Time']   # Extracting time values
    t_i = []
    for i in time:
        t_i.append(i)
    sample = len(f_trim)
    for i in range(sample):
        if ((f_trim[i] >= 10) or (f_trim[i] <= -10)):
            f_plot.append(f_trim[i])
            t_plot.append(t_i[i])
            count = count + 1
    fuel_trim_condition = []
    x_axis = t_plot  # x axis values
    y_axis = f_plot  # corresponding y axis values
    if count >= 1:  # Only If values are non ideal a graph is plotted
        print('Plotting Non Ideal Fuel Trim Values')
        plt.plot(x_axis, y_axis)  # plotting the points
        plt.xlabel('Time')  # naming the x axis
        plt.ylabel('Fuel trim bank 1 sensor 1(%)')  # naming the y axis
        plt.title('Fuel Trim Values')  # giving a title to my graph
        plt.show()  # function to show the plot
    for i in f_trim:
        if ((i <= 10) and (i >= -10)):      # Ideal Condition
            fuel_trim_condition.append(f_trim_mode[0])
        elif ((i <= 25) and (i >= -25)):    # Non Ideal Condition
            fuel_trim_condition.append(f_trim_mode[1])
        else:
            fuel_trim_condition.append(f_trim_mode[2])  # Malfunction
    for i in fuel_trim_condition:
        if i == f_trim_mode[2]:
            print('Warning: Malfunction in Fuel Trim Sensor')
            f_trim_mil = 1
            f_trim_flag = 1
            f_trim_time = time[index]
            print('Malfunctioning Observed on', f_trim_time)
        elif i == f_trim_mode[1]:
            f_trim_flag = 1
            f_trim_time = time[index]
        else:
            pass
        index = index+1
    if f_trim_flag == 1 and f_trim_mil != 1:
        print('Vehicle Fuel Trim is Non-ideal')
        print('Non-Ideal Behaviour Observed First on', f_trim_time)
    else:
        print('Vehicle has efficient Fuel Trim Ability')
