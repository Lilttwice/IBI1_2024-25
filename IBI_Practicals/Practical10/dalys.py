# plotting overall burden of disease across countries over time, in other words, 'disability adjusted life years’ or DALYs
# summing together the mortality and morbidity
# data from the public repository: dalys-rate-from-all-causes.csv
# demand-code-output

#3 Libraries needed for importing a dataset
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

os.chdir("/Users/a1/Desktop/IBI_2024-25/IBI_Practicals/Practical10")

# pwd
current_dir = os.getcwd()
print(current_dir)
#output
#/Users/a1/Desktop/IBI_2024-25/IBI_Practicals/Practical10


# ls
dir_list = os.listdir()
print(dir_list)
# #['dalys.py', 'dalys-rate-from-all-causes.csv']


# read the data
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

#4 working with dataframes
# try filename.head/tail(number), it shows first/last n rows
# print(dalys_data.head(3))
# print(dalys_data.tail(3))
# between commas should be read as separate things and every print contains first row with no data but names of the columns
print(dalys_data.head(2), dalys_data.tail(2))
#        Entity Code  Year     DALYs
#0  Afghanistan  AFG  1990  86375.17
#1  Afghanistan  AFG  1991  83381.07         Entity Code  Year     DALYs
#6838  Zimbabwe  ZWE  2018  60084.52
#6839  Zimbabwe  ZWE  2019  58969.11


# to know what type of datapoints/ columns are in the dataset/ how many rows are there
print(dalys_data.info())
#<class 'pandas.core.frame.DataFrame'>
#RangeIndex: 6840 entries, 0 to 6839
#Data columns (total 4 columns):
# #   Column  Non-Null Count  Dtype  
#---  ------  --------------  -----  
# 0   Entity  6840 non-null   object 
# 1   Code    6150 non-null   object 
# 2   Year    6840 non-null   int64  
# 3   DALYs   6840 non-null   float64
#dtypes: float64(1), int64(1), object(2)
#memory usage: 213.9+ KB
#None


#For each numeric column, describe() shows the number of entries, mean, standard deviation and a number of quantiles
#the maximum/minimum DALYs (across all rows of the dataframe)
#the first year/ the most recent year when DALYs were recorded?
print(dalys_data.describe())
#               Year          DALYs
#count  6840.000000    6840.000000
#mean   2004.500000   42372.219173
#std       8.656074   22596.140799
#min    1990.000000   15045.110000
#25%    1997.000000   26973.065000
#50%    2004.500000   35035.490000
#75%    2012.000000   52732.695000
#max    2019.000000  693367.490000


# see only specific values in the dataframe
# iloc: access values by row and column
# loc: access values by row number and column name.
# after iloc or loc, there are square brackets.
# [a,b]=[row, column]
# For instance, this shows you what’s in the first row, fourth column (as always in Python, counting begins at zero).
# the title of the columns does not count
print(dalys_data.iloc[0,3])
# 86375.17

# to show several rows and columns
# 3 samples:

#Before you see, know that title will always be shown,
# for rows, it will be shown vertically
# for columns, it will be shown horizontally

# if file.csv have a title, row number should -2 before input, because title-1 and zero-1.
print(dalys_data.iloc[2,0:4])
# and if column number is less than input number, it will be ignored
#print(dalys_data.iloc[2,0:5])=print(dalys_data.iloc[2,0:6])=...
#last row will show the specific row's dtype and row number
#output:
# Entity    Afghanistan
#Code              AFG
#Year             1992
#DALYs        79890.55
#Name: 2, dtype: object

# :will show whole number of row/column, a:b,will show a:b-1
print(dalys_data.iloc[0:2,:])
#output;
#        Entity Code  Year     DALYs
#0  Afghanistan  AFG  1990  86375.17
#1  Afghanistan  AFG  1991  83381.07


print(dalys_data.iloc[0:10:3,0:5])
# a:b:c, c is step, b will minus 1
#output:
#        Entity Code  Year     DALYs
#0  Afghanistan  AFG  1990  86375.17
#3  Afghanistan  AFG  1993  80292.52
#6  Afghanistan  AFG  1996  81310.23
#9  Afghanistan  AFG  1999  82624.94

print(dalys_data.iloc[0:10:2,0:4])
#output:
#        Entity Code  Year     DALYs
#0  Afghanistan  AFG  1990  86375.17
#2  Afghanistan  AFG  1992  79890.55
#4  Afghanistan  AFG  1994  83334.93
#6  Afghanistan  AFG  1996  81310.23
#8  Afghanistan  AFG  1998  86656.29

#How would you show the third column (the year) for the first 10 rows (inclusive)? Your output should contain 10 rows in total. 
# What was the 10th year for which DALYs were recorded in Afghanistan?
# Answer：
print(dalys_data.iloc[0:10, 2])
# from the output:
#0    1990
#1    1991
#2    1992
#3    1993
#4    1994
#5    1995
#6    1996
#7    1997
#8    1998
#9    1999
#Name: Year, dtype: int64
# The 10th year for which DALYs were recorded in Afghanistan is 1999.


#iloc: both Numbers and Booleans to access entries
#I wanted to see the first three rows, but only the first, second, and fourth column. I could do this using numbers:
dalys_data.iloc[0:3,[0,1,3]]
#output: no year this time
#        Entity Code     DALYs          
#0  Afghanistan  AFG  86375.17
#1  Afghanistan  AFG  83381.07
#2  Afghanistan  AFG  79890.55
# But I could also do this using the column names:
print(dalys_data.iloc[0:3,["Entity","Code","DALYs"]])

# I could also do the following thing, which may seem a bit strange at first:
# my_columns is a list of Booleans that must be the same length as the number of columns in the dataframe: if my_column is shorter or longer than the number of columns in the dataframe, Index error
#If I use it to read columns with iloc, Python will go through the list and show me the columns where the value is True.
my_columns = [True, True, False, True]
print(dalys_data.iloc[0:3,my_columns])
#the above three have the same output


# loc uses column names.
#  the number in the loc means what csv file row sequence, instead of counting from 0 for iloc in python way
print(dalys_data.loc[2:4,"Year"])
#output:
#2    1992
#3    1993
#4    1994
#Name: Year, dtype: int64


#look for rows that interest us without having to know the row numbers, loc can localize that
# eg: I am interested in DALYs reported in the year 1990.
# Using loc, it’s fairly easy to get the column part right.
# dalys_data.loc[blabla,"DALYs"], blabla is the part that tells Python which rows I want to see.
# eg: dalys_data.loc[every row where Year is 1990,"DALYs"]
# in this case, blabla need to be able to skim throught all the rows in the file, use what was use to read the file "dalys_data.rowname"
print(dalys_data.loc[dalys_data.Year==1990,"DALYs"])


# read just the “Year” column, but all the rows from dalys_data?
print(dalys_data.loc[:,"Year"])
#output:
#0       1990
#1       1991
#2       1992
#3       1993
#4       1994
#        ... 
#6835    2015
#6836    2016
#6837    2017
#6838    2018
#6839    2019
#Name: Year, Length: 6840, dtype: int64

# Use Boolean to show DALYs for all countries in 1990
daly_1990 = dalys_data.loc[dalys_data["Year"] == 1990, "DALYs"]
print("\nDALYs for all countries in 1990:")
print(daly_1990)

# Compute mean DALYs for UK and France
uk_data = dalys_data.loc[dalys_data["Entity"] == "United Kingdom", ["DALYs", "Year"]]
france_data = dalys_data.loc[dalys_data["Entity"] == "France", ["DALYs", "Year"]]
uk_mean = uk_data["DALYs"].mean()
france_mean = france_data["DALYs"].mean()
print(f"\nMean DALYs for UK: {uk_mean:.2f}")
print(f"Mean DALYs for France: {france_mean:.2f}")
# Comment: Compare means
if uk_mean > france_mean:
    print("# Mean DALYs in the UK is greater than in France.")
else:
    print("# Mean DALYs in the UK is smaller than or equal to France.")

# Plot DALYs over time for the UK
plt.figure(figsize=(10, 6))
plt.plot(uk_data["Year"], uk_data["DALYs"], 'b*', label="UK DALYs")
plt.xticks(uk_data["Year"], rotation=-90)
plt.xlabel("Year")
plt.ylabel("DALYs (Disability-Adjusted Life Years)")
plt.title("DALYs in the United Kingdom Over Time")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("uk_dalys_plot.png")  # Save plot
plt.show()

# Answer a custom question (Line 66 starts this section)
# Question: How have DALYs in China changed along time compared to the UK?
china_data = dalys_data.loc[dalys_data["Entity"] == "China", ["DALYs", "Year"]]
plt.figure(figsize=(10, 6))
plt.plot(china_data["Year"], china_data["DALYs"], 'r+', label="China DALYs")
plt.plot(uk_data["Year"], uk_data["DALYs"], 'b*', label="UK DALYs")
plt.xticks(china_data["Year"], rotation=-90)
plt.xlabel("Year")
plt.ylabel("DALYs (Disability-Adjusted Life Years)")
plt.title("DALYs in China vs. UK Over Time")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("china_uk_dalys_plot.png")  # Save plot
plt.show()
# Summary statistics for discussion in question.txt
china_mean = china_data["DALYs"].mean()
print(f"Mean DALYs for China: {china_mean:.2f}")