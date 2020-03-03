"""Feature 1 Ideal Gear """
import pandas as pd
DATA = pd.read_csv('city2.csv')
D = pd.DataFrame(DATA)     # dataframe conversion


def get_gear(speed, gyro_y, mode):
    """Function to get gear number"""
    mil = {1: 0, 2: 11, 3: 35, 4: 53, 5: 78}  # Minimum gear:speed
# dictionary for mileage
    perf = {1: 0, 2: 24, 3: 45, 4: 66, 5: 83}  # Minimum gear:speed
# dictonary for performance
    gear = []
    mode = 1  # default mode is mileage
    inp = input("Select the mode 0 - Performace  1- Mileage  :")
    if inp == 0:  # mode selection
        mode = 0
    elif inp == 1:
        pass
    gyro = []
    for i in gyro_y:  # converting gyroscope Y values from series to list
        gyro.append(i)
    i = 0
    for val in speed:
        if gyro[i] >= 0.5:  # Threshold to get performance if vehicle is going
            mode = 0        # Uphill
        if mode == 1:  # mode for mileage
            if val >= mil[5]:  # Comparing values for mileage mode
                gear.append(5)
            elif val >= mil[4]:
                gear.append(4)
            elif val >= mil[3]:
                gear.append(3)
            elif val >= mil[2]:
                gear.append(2)
            else:
                gear.append(1)
        if mode == 0:  # Comparing values for performance mode
            if val >= perf[5]:
                gear.append(5)
            elif val >= perf[4]:
                gear.append(4)
            elif val >= perf[3]:
                gear.append(3)
            elif val >= perf[2]:
                gear.append(2)
            else:
                gear.append(1)
        i = i + 1
    return gear


def disp_gear(gear, time1, samples):
    """Function to display gear number"""
    print('There are totally', (max(samples)+1), 'samples')
    inp1 = int(input('Enter the lower limit of the samples to be observed '))
    inp2 = int(input('Enter the upper limit of the samples to be observed '))
    print("\n\t\tIdeal Gear Values\n")
    for i in range((inp1-1), (inp2)):
        print("Time: ", time1[i], "|  Gear Number: ", gear[i])


def feature1():
    """Main Function of the feature"""
    car_mode = ("Performance", "Mileage")  # Two modes of driving
    gyro_y = D[' G(y)']
    s_p = D['Speed (GPS)(km/h)']
    mode = car_mode.index("Mileage")  # default mode is set to mileage
    speed = []
    for i in s_p:  # converting speed series to list
        speed.append(i)
    samples = range(len(speed))  # Calculating range of samples
    t_m = D['GPS Time']
    time1 = []
    gear = []
    for i in t_m:  # Converting time series to list
        time1.append(i)
    gear = get_gear(speed, gyro_y, mode)  # Finding gear number
    disp_gear(gear, time1, samples)  # Displaying gear number
