import numpy as np
import csv
from matplotlib import pyplot as plt
import math as m


def readData(filename, set):
    elongation, force = [], []
    with open(filename, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            if (row[2*set-2] == '') or (row[2*set-1] == ''):
                break
            elongation.append(float(row[2*set-2]))
            force.append(float(row[2*set-1]))

        f.close()
    return elongation, force

elongation, force = readData('/home/hnobles12/Documents/TAMU/Fall 2020/TAMU/AERO-214/Lab1/Data/6061.csv', 1)


def graph6061(set):
    elongation, force = readData('/home/hnobles12/Documents/TAMU/Fall 2020/TAMU/AERO-214/Lab1/Data/6061.csv', set)
    l0 = (1.948/12)/3.28 # m
    d0 = (0.232/12)/3.28 # m
    #lf = (2.32/12)/3.28  # m
    area = m.pi*(d0/2)**2 # m^2

    stress = [] # N/m^2
    strain = [] # m/m
    young_mod_list = [] # N/m^2

    for i in force:
        stress.append(i*1000/area) # N/m^2
    
    for i in elongation:
        strain.append((i/1000)/l0) # m/m
    
    plt.plot(strain, stress)
    
    plt.xlabel("Strain (m/m)")
    plt.ylabel("Stress (N/m^2)")
    plt.title("Stress vs. Strain\nAl 6061 - Data Set {}".format(set))
    plt.show()

    for i in range(len(stress)):
        if (strain[i] == 0):
            continue
        young_mod_list.append(stress[i]/strain[i])
    
    young_mod = np.average(young_mod_list)
    print("Young's Modulus: {} GPa".format(young_mod/1e9))




def graph2024(set):
    elongation, force = readData('/home/hnobles12/Documents/TAMU/Fall 2020/TAMU/AERO-214/Lab1/Data/2024.csv', set)
    l0 = (1.986/12)/3.28 # m 
    d0 = (0.234/12)/3.28 # m
    #lf = (2.176/12)/3.28  # m
    area = m.pi*(d0/2)**2 # m^2

    stress = [] # N/m^2
    strain = [] # m/m
    young_mod_list = [] # N/m^2

    for i in force:
        stress.append(i*1000/area) # N/m^2
    
    for i in elongation:
        strain.append((i/1000)/l0) # m/m
    
    plt.plot(strain, stress)
    
    plt.xlabel("Strain (m/m)")
    plt.ylabel("Stress (N/m^2)")
    plt.title("Stress vs. Strain\nAl 2024 - Data Set {}".format(set))
    plt.show()

    for i in range(len(stress)):
        if (strain[i] == 0):
            continue
        young_mod_list.append(stress[i]/strain[i])
    
    young_mod = np.average(young_mod_list)
    print("Young's Modulus: {} GPa".format(young_mod/1e9))


def graphA36(set, exp):
    if exp == 3:
        data_file = '/home/hnobles12/Documents/TAMU/Fall 2020/TAMU/AERO-214/Lab1/Data/A36-exp3.csv'
    elif exp == 4: 
        data_file = '/home/hnobles12/Documents/TAMU/Fall 2020/TAMU/AERO-214/Lab1/Data/A36-exp4.csv'
    else:
        Exception("Invalid Option.")
        return

    elongation, force = readData(data_file, set)
    l0 = (1.92/12)/3.28 # m 
    d0 = (0.24/12)/3.28 # m
    #lf = (2.405/12)/3.28  # m
    area = m.pi*(d0/2)**2 # m^2

    stress = [] # N/m^2
    strain = [] # m/m
    young_mod_list = [] # N/m^2

    for i in force:
        stress.append(i*1000/area) # N/m^2
    
    for i in elongation:
        strain.append((i/1000)/l0) # m/m
    
    plt.plot(strain, stress)
    
    plt.xlabel("Strain (m/m)")
    plt.ylabel("Stress (N/m^2)")
    plt.title("Stress vs. Strain\nA36 Steel - Data Set {}, Expiriment: {}".format(set,exp))
    plt.show()

    for i in range(len(stress)):
        if (strain[i] == 0):
            continue
        young_mod_list.append(stress[i]/strain[i])
    
    young_mod = np.average(young_mod_list)
    print("Young's Modulus: {} GPa".format(young_mod/1e9))


#graph6061(5)
#graph2024(1)
#graphA36(1,4)