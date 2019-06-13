#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
    Get some information of csv2nc.py generated netCDF files.
    
    Author: Björn Saß (bjoern.sass@fau.de)
    Created: 01.03.2018
'''


import xarray as xr
from nc_config import nc_name

# read data
DATA = xr.open_dataset(nc_name)

print (20*'-')
print ('description: '.upper(), DATA.attrs['description'])
print ('history: '.upper(), DATA.attrs['history'])
print ('source: '.upper(), DATA.attrs['source'])
print (20*'-')
print (DATA.coords['time'][0:10])
print (20*'-')
print (DATA.data_vars)
print (20*'-')

lat = DATA['latitude'].values
lon = DATA['longitude'].values
print ('LAT (N)', lat[0], 'LON (E)', lon[0])
print (20*'-')

# save parameter as variable array
wind_speed = DATA['u2'].values              # Wind speed (magnitude) m/s
solar_radiation = DATA['G'].values          # Solar radiation at each time step [W m-2]
temperature_2m = DATA['T2'].values          # Air temperature (2m over ground) [K]
relative_humidity = DATA['rh2'].values      # Relative humidity (2m over ground)[%]
snowfall = DATA['prec'].values              # Snowfall per time step [m]
air_pressure = DATA['p'].values             # Air Pressure [hPa]
cloud_cover = DATA['N'].values              # Cloud cover  [fraction][%/100]
initial_snow_height = DATA['sh'].values     # [m]
    
print ('Temperature [K]:', temperature_2m[0:10])
print (20*'-')
print ('Init. snow height [m]:',initial_snow_height)
print (20*'-')
print ('Solar radiaiton [W m-2]:', solar_radiation[0:10])
print (20*'-')
print ('Rel. Humid. [%]:', relative_humidity[0:10])
print (20*'-')
print ('Snowfall [m]:', snowfall[0:10])
print (20*'-')
print ('Air pressure [hPa]:', air_pressure[0:10])
print (20*'-')
print ('Cloud cover [%/100]:', cloud_cover[0:10])
print (20*'-')
print ('Wind speed [m/s]:', wind_speed[0:10])
