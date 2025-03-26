import sys

import matplotlib.pyplot as plt
import pandas as pd

infile_try_csv = sys.argv[1]


# dataframe = pd.read_csv("out/try.csv", sep=";", header=None, names=["time", "temperature_year",
#                                                                    "temperature_summer", "temperature_winter"])
dataframe = pd.read_csv(infile_try_csv, sep=";")


dataframe.plot(kind='line',
               x='time',
               y=["temperature_Jahr",
                  "temperature_Somm",
                  "temperature_Wint"],
               color=['pink', 'red', 'blue'],
               lw=1
               )

# plt.title('TRY 2045, Raunheim')
filename = infile_try_csv.split('/')[-1]
filename_without_extension = filename.split('.')[0]
plt.title(filename_without_extension)

# add lines at 20 degrees and at 30 degrees celsius
plt.axhline(20, color='blue', lw=0.5)
plt.axhline(30, color='red', lw=0.5)

# slice the year in quaters, for hour-based datasets for 1 year
plt.axvline(2190, color='lightgray', lw=1)
plt.axvline(4380, color='lightgray', lw=0.5)
plt.axvline(6570, color='lightgray', lw=0.5)
plt.ylabel('Temperature [°C]')
plt.xlabel('Date and Time [mm-dd-hh]')
plt.minorticks_on()
# plt.grid(True)

plt.show()

