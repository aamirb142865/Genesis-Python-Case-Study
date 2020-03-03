""" Feature 3 - Knock Detection"""
import pandas as pd
DATA = pd.read_csv('city2.csv')
D = pd.DataFrame(DATA)     # dataframe conversion


def feature4():
    """Main Function of feature 4 """
    load = D['Engine Load(%)']
    rpm = D['Engine RPM(rpm)']
    time = D['GPS Time']   # Extracting time values
    adv_timing = D['Timing Advance']
    load_value = []  # Lists to be stored
    rpm_value = []
    flag = []
    a_time = []
    for i in load:  # Conversion of series to list
        load_value.append(i)
    for i in rpm:  # Conversion of series to list
        rpm_value.append(i)
    for i in adv_timing:  # Conversion of series to list
        a_time.append(i)
    for i in range(len(load)):  # Specifying range for knock detection
        if rpm_value[i] < 500 and (load_value[i] > 25):
            flag.append(1)
        elif rpm_value[i] < 1000 and (load_value[i] > 35):
            flag.append(1)
        elif rpm_value[i] < 1500 and (load_value[i] > 40):
            flag.append(1)
        elif rpm_value[i] < 2000 and (load_value[i] > 42):
            flag.append(1)
        elif rpm_value[i] < 3000 and (load_value[i] > 44):
            flag.append(1)
        elif rpm_value[i] < 4000 and (load_value[i] > 46):
            flag.append(1)
        elif rpm_value[i] < 5000 and (load_value[i] > 48):
            flag.append(1)
        else:
            flag.append(0)
    for i in range(len(load)):
        if flag[i] == 1 and a_time[i] >= 20:  # Checking if timing advance is
                                                # significant
            print('Knock Was Produced on', time[i])
