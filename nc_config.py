'''
    Necessary input for txt* or csv* **2nc
    Execute cav2nc.py to generate a netCDF file.
    
    Works for 1D netCDF (dimensions: lat=1, lon=1)
    
    The row names in the header of the csv file (order unimportant):
        u2      Wind speed (2m over ground) (magnitude) m/s
        G       Solar radiation at each time step [W m-2]
        T2      Air temperature (2m over ground) [K]
        rh2     Relative humidity (2m over ground)[%]
        prec    Snowfall per time step [m]  (shoud be total precipitation)
        p       Air Pressure [hPa]
        N       Cloud cover  [fraction][%/100]
        sh      Initial snow height [m]
        
    Author: Björn Saß (bjoern.sass@fau.de)
    Created: 01.03.2018
'''

# full path or name (if its in root dir) to csv input
filepath = 'C:/Users/Bjoern Lukas/Documents/Promotion/skripte/cosipy/fau-fdm/test_suite/nc-handler/file.csv'

# separator of the lines/columns in csv file
separator = ';'

# full path or name (if its in root dir) of netCDF output file
nc_name = 'C:/Users/Bjoern Lukas/Documents/Promotion/skripte/cosipy/fau-fdm/test_suite/fancy_new_file_name.nc'

# Point coordinates
northing = 80.0491409302    # lat
easting = 19.5707874298     # lon

# Times and dates
''' set start '''
year = 2010      
month = 1       
day = 1
hour = 0            # 0-23 h
steps = 3           # delta hours between measurements

# snow depth/ height
sh = 1.6            # [m] please set to zero if not available

# description of the data as string
descript_ncfile = 'one dimensional input parameter for cosipy for Himalaya (Project Arindan Mandal)'
data_source = 'HAR v13.2, courtesy Mister extremely smart and clever'
your_name = 'Arindan Mandal'
