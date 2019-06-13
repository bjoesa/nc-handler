#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
    This scritpt stores your csv files in a netCDF (nc) file.
    Make your decisions in the nc_config.py file.
    If you want to have any insight in the nc file afterwards,
    try to use the nc_reader.py script.
    
    Excexute this script to get the nc file.
    Be sure that all necessary packages (panda, datetime, netCDF4, numpy)
    are installed.
    
    Author: Björn Saß (bjoern.sass@fau.de)
    Created: 01.03.2018
'''

from datetime import datetime, timedelta
import pandas
from netCDF4 import Dataset, num2date, date2num
import numpy as np

from nc_config import filepath, northing, easting, nc_name, year, month, day, \
                      hour, steps, sh, \
                      descript_ncfile, data_source, your_name, separator


''' READ in csv ''' 
data_frame = pandas.read_csv(filepath, sep = separator)
data_frame.keys

T2 = data_frame.T2.tolist()
G = data_frame.G.tolist()
N = data_frame.N.tolist()
p = data_frame.p.tolist()
rH2 = data_frame.rh2.tolist()
u2 = data_frame.u2.tolist()
prec = data_frame.prec.tolist()

''' Open netCDF file '''
ncfile = Dataset(nc_name, 'w', format='NETCDF4_CLASSIC')
print ('NETCDF file format: ', ncfile.file_format)

# dimensions
lat = ncfile.createDimension('lat', 1)
lon = ncfile.createDimension('lon', 1)
time = ncfile.createDimension('time', None)

# dimensional variables
times = ncfile.createVariable('time', np.float64, ('time',))
latitudes = ncfile.createVariable('latitude', np.float64, ('lat',))
longitudes = ncfile.createVariable('longitude', np.float64, ('lon',))

# data variables
G_var = ncfile.createVariable('G', np.float64, ('time',))
N_var = ncfile.createVariable('N', np.float64, ('time',))
sh_var = ncfile.createVariable('sh', np.float64)
p_var = ncfile.createVariable('p', np.float64, ('time',))
rH2_var = ncfile.createVariable('rh2', np.float64, ('time',))
T2_var = ncfile.createVariable('T2', np.float64, ('time',))
u2_var = ncfile.createVariable('u2', np.float64, ('time',))
prec_var = ncfile.createVariable('prec', np.float64, ('time',))

# additional date/time code
# dat = ncfile.createVariable('datum', 'S1', ('time',))

# global attributes
ncfile.description = descript_ncfile
jetzt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
ncfile.history = 'Created ' + jetzt + ' by ' + your_name
ncfile.source = data_source

print (ncfile.history)
print (ncfile.source)

# variable attributes
latitudes.units = 'degree_north/northing'
longitudes.units = 'degree_east/easting'
G_var.units = 'W m-2'
N_var.units = '%/100'
sh_var.units = 'm'
p_var.units = 'hPa'
rH2_var.units = '%'
T2_var.units = 'K'
u2_var.units = 'm s-1'
prec_var.units = 'mmWE'

times.units = 'hours since %s' % year + '-%s-' % month + '%s ' % day + '%s:00:00' % hour
times.calendar = 'gregorian'
# print (times.units)

# set variables
latitudes[:] = northing
longitudes[:] = easting

G_var[:] = G
N_var[:] = N
sh_var[:] = sh
p_var[:] = p
rH2_var[:] = rH2
T2_var[:] = T2
u2_var[:] = u2
prec_var[:] = prec

# defining date/times
dates = []

G_var.shape[0]

for n in range(G_var.shape[0]):
    dates.append(datetime(year, month, day, hour) + n * timedelta(hours=steps))
    
times[:] = date2num(dates, units=times.units, calendar=times.calendar)

#print ('time values (in units %s): ' % times.units + '\n', times)

dates = num2date(times[:], units=times.units, calendar=times.calendar)

print ('dates corresponding to time values:\n', dates)

ncfile.close()
