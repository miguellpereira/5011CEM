import pandas as pd                     #imports the pandas library
import geopandas as gpd                 #imports the geopandas library
from scipy.io import netcdf             #imports the scipy library
import numpy as np                      #imports the numpy library
import matplotlib.pyplot as plt         #imports the matplotlib library

#function to display the menu of ozone data choices and the colour choice
def displayMenu(options):
    for i in range (len(options)):
        print("{:d}. {:s}".format(i+1, options[i]))
    
    choice = 0
    while not(np.any(choice == np.arange(len(options))+1)):
        choice = inputNumber("\nPlease choose a menu entry: ")
        
    return choice
    
#function to check if the user choice is between the available menu choices
def inputNumber(prompt):
    while True:
        try:
            num = float(input(prompt))
            break
        except ValueError:
            pass
    return num

#declare the ozone data choices
menuChoices = np.array(["Ensemble Ozone", "Chimere Ozone", "Emep Ozone", "Match Ozone", "Eurad Ozone", "Silam Ozone", "Mocage Ozone"])
#declare the colour choices
colourChoices = np.array(["Normal", "Protanopia", "Deuteranopia", "Tritanopia"])


#Stores the path to the file "Combined.nc", which is the "o3_surface_20180701000000.nc" but renamed
datafile=r'C:\Users\luisl\Desktop\EZ\Combined.nc' #EDIT HERE -> edit to the path where your "Combined.nc" file is located

file2read = netcdf.NetCDFFile(datafile,'r')             #gets the path to the file and stores the information inside this variable
dataType = 'chimere_ozone'                              #declares a default value for dataType
ozoneData = file2read.variables[dataType][:]*1          #declares a default value for ozoneData
lon = file2read.variables['lon'][:]*1                   #gets the longitude value from the .nc file
lat =  file2read.variables['lat'][:]*1                  #gets the latitude value from the .nc file
hours =  file2read.variables['hour'][:]*1               #gets the hours value from the .nc file
time = len(hours)                                       #stores the lenght of the hours variable

print("\nOzone data types: \n")                         #prints "Ozone data types: " to the user

#calls the function displayMenu with the menuChoices as argument and stores user input in the choice variable
choice = displayMenu(menuChoices);

while True:
    if choice == 1:                                     #if the user choice is 1
        print('Ensemble Ozone Data Will Be Visualised') #prints "Ensemble Ozone Data Will Be Visualised" to the user
        dataType = 'ensemble_ozone'                     #sets the dataType to 'ensemble_ozone'
        break
    elif choice == 2:                                   #if the user choice is 2
        print('Chimere Ozone Data Will Be Visualised')  #prints "Chimere Ozone Data Will Be Visualised" to the user
        dataType = 'chimere_ozone'                      #sets the dataType to 'chimere_ozone'
        break
    elif choice == 3:                                   #if the user choice is 3
        print('Emep Ozone Data Will Be Visualised')     #prints "Emep Ozone Data Will Be Visualised" to the user
        dataType = 'emep_ozone'                         #sets the dataType to 'emep_ozone'
        break
    elif choice == 4:                                   #if the user choice is 4
        print('Match Ozone Data Will Be Visualised')    #prints "Match Ozone Data Will Be Visualised" to the user
        dataType = 'match_ozone'                        #sets the dataType to 'match_ozone'
        break
    elif choice == 5:                                   #if the user choice is 5
        print('Eurad Ozone Data Will Be Visualised')    #prints "Eurad Ozone Data Will Be Visualised" to the user
        dataType = 'eurad_ozone'                        #sets the dataType to 'eurad_ozone'
        break
    elif choice == 6:                                   #if the user choice is 6
        print('Silam Ozone Data Will Be Visualised')    #prints "Silam Ozone Data Will Be Visualised" to the user
        dataType = 'silam_ozone'                        #sets the dataType to 'silam_ozone'
        break
    elif choice == 7:                                   #if the user choice is 7
        print('Mocage Ozone Data Will Be Visualised')   #prints "Mocage Ozone Data Will Be Visualised" to the user
        dataType = 'mocage_ozone'                       #sets the dataType to 'mocage_ozone'
        break
        
        
print("\nColours: \n")                                      #prints "Colours: " to the user

#calls the function displayMenu with the colourChoices as argument and stores user input in the colourChoice variable
colourChoice = displayMenu(colourChoices)

while True:
    if colourChoice == 1:                                   #if the user choice is 1
        print("Default Colouring Applied!")                 #prints "Default Colouring Applied!" to the user
        colourPallet = 'hsv'                                #declares the colourPallet variable and sets the value to 'hsv'
        break
    elif colourChoice == 2:                                 #if the user choice is 2
        print("Protanopia Friendly Colouring Applied!")     #prints "Protanopia Colouring Applied!" to the user
        colourPallet = 'spring'                             #sets the value of colourPallet to 'spring'
        break
    elif colourChoice == 3:                                 #if the user choice is 3
        print("Deuteranopia Friendly Colouring Applied!")   #prints "Deuteranopia Colouring Applied!" to the user
        colourPallet = 'winter'                             #sets the value of colourPallet to 'winter'
        break
    elif colourChoice == 4:                                 #if the user choice is 4
        print("Tritanopia Friendly Colouring Applied!")     #prints "Tritanopia Colouring Applied!" to the user
        colourPallet = 'autumn'                             #sets the value of colourPallet to 'autumn'
        break
 

ozoneData = file2read.variables[dataType][:]*1              #sets the value of ozoneData to match the dataType that the user chose

x,y = np.meshgrid(lon, lat)                                 #creates a meshgrid with the values of lat and lon

plt.ion()                                                   #enables the interactive plot

fig = plt.figure(figsize=(10,6))                            #creates a figure with 10 inches width and 6 inches height

world = gpd.read_file(r'C:\Users\luisl\Desktop\Mapa\Europe_coastline.shp')  #gets the data from the shapefile Europe_coastline


for i in range(0,time):                                             #for loop to go through all hours in the .nc file

    ax = plt.pcolor(x, y ,ozoneData[i,:,:], cmap = colourPallet)    #creates a pcolor with the longitude, latitude, the hour[i] and the colourPallet chosen by the user
    plt.title('The time is:{}'.format(i))                           #creates a title that shows the hour that corresponds with the data shown
    plt.xlabel('Latitude')                                          #stets the X label to Latitude
    plt.ylabel('Longitude')                                         #stets the Y label to Longitude
    #plt.colorbar()                                                  #shows a colourbar on the side of the map
    plt.pause(0.01)                                                 #pauses the loop for a bit so that the user can see the data without it updating so fast
    