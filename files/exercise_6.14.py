# -*- coding: utf-8 -*-
"""
Created on Thu Aug 06 22:40:17 2015

@author: Georg
"""
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.dates import YearLocator, MonthLocator, DateFormatter
plt.rc('figure', figsize=(10,8))

# Function to create dictionary of city names and corresponding text files
# from the information given in a html file
def read_list_file(inputfile):
    city_list = {}
    infile = open(inputfile, 'r')
    
    for line in infile:
        if ".5in'><b>" in line:  
            start = line.find(".5in'><b>")
            end = line.find(' (')
            city = line[start+len(".5in'><b>"):end]
            
            nextline = infile.next()
            nextnextline = infile.next()
            
            start = nextnextline.find('>')
            end = nextnextline.find('txt<')
            filename = nextnextline[start+1:end+3]
            city_list[city] = filename
        else:
            pass
    
    infile.close()
    
    return city_list
    
# Function to create a data dictionary with dates and corresponding temperatures
# from the information in a text file given the city name
def load_temp_data_v1(dic, city_name):
    filename = dic[city_name]
    base = 'C:/Users/Georg/Documents/PythonDokumente/Scipro-primer/src/misc/city_temp/'
    infile = open(base+filename, 'r')
    dates = []; temps = []
    
    for line in infile:
        words = line.split()
        date = '-'.join(words[0:3])
        dates.append(date)
        if words[3] == '-99':
            temp = np.nan
        else:
            temp = float(words[3])
        temps.append(temp)
        
    infile.close()
    
    datefmt = '%m-%d-%Y'
    dates = [datetime.strptime(_date, datefmt).date() for _date in dates]
    temps = np.array(temps)
    data_dic = {'city': city_name, 'Dates': dates, 'Temperature': temps}
    return data_dic

# Function to create a data dictionary with city names and the corresponding 
# dates and temperatures in a subdictionary given a list of city names
def load_temp_data_v2(dic, city_names):
    data_dic = {}
    for city in city_names:
        data_dic[city] = {}
        filename = dic[city]
        base = 'C:/Users/Georg/Documents/PythonDokumente/Scipro-primer/src/misc/city_temp/'
        infile = open(base+filename, 'r')
        dates = []; temps = []
        
        for line in infile:
            words = line.split()
            date = '-'.join(words[0:3])
            dates.append(date)
            if words[3] == '-99':
                temp = np.nan
            else:
                temp = float(words[3])
            temps.append(temp)
            
        infile.close()
    
        datefmt = '%m-%d-%Y'
        dates = [datetime.strptime(_date, datefmt).date() for _date in dates]
        temps = np.array(temps)
        data_dic[city]['Dates'] = dates
        data_dic[city]['Temperature'] = temps
        
    return data_dic

# Function to create plot of temperature data
def make_plot(data_dic):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    legends = []
    for city in data_dic:
        ax.plot_date(data_dic[city]['Dates'], data_dic[city]['Temperature'], '-', label=city)
        legends.append(city)
    ax.legend(legends, loc=1)
    ax.set_ylabel('Degree Fahrenheit')
    
    # Format x-axis
    years = YearLocator(1)  # major ticks every 1 year
    months = MonthLocator(2)  # minor ticks every 2 months
    yearsfmt = DateFormatter('%Y')
    ax.xaxis.set_major_locator(years)
    ax.xaxis.set_major_formatter(yearsfmt)
    ax.xaxis.set_minor_locator(months)
    ax.set_xlabel('Years')
    ax.autoscale_view()
    fig.autofmt_xdate()

# Location of html file
base = 'C:/Users/Georg/Documents/PythonDokumente/Scipro-primer/src/misc/city_temp/'
inputfile = base+'citylistWorld.htm'

# Create dictionary of city names and text files and print it out
liste = read_list_file(inputfile)
print "%-15s: %-15s\n%s" % ('City', 'Filename', '-'*30)
for key in sorted(liste):
    print "%-15s: %-15s" % (key, liste[key])
print "\nNo. of files:", len(liste)

# Call function v1 for one city
city_name = 'Bangui'
data_dic1 = load_temp_data(liste, city_name)
print "\nTemperature data for '%s' during first 12 months:" % (city_name)
for i in range(12):
    print data_dic1['Dates'][i], data_dic1['Temperature'][i]

# Call function v2 for a list of cities
city_names = ['Bangui', 'Cairo', 'Minsk']
data_dic2 = load_temp_data_v2(liste, city_names)
for city in data_dic2:
    print "\nTemperature data for '%s' during first 12 months:" % (city)
    for i in range(12):
        print data_dic2[city]['Dates'][i], data_dic2[city]['Temperature'][i]

# Make plot for list of cities
make_plot(data_dic2)