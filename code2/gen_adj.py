import numpy as np
from util2 import *
import os

if os.path.isfile(path + 'trip.npy'):
    trip = np.load(path + 'trip.npy')
else:
    trip = np.loadtxt(path+'taxi_id.csv',delimiter=",")
    np.save(path + 'trip',trip)

if os.path.isfile(path + 'zone.npy'):
    zone = np.load(path + 'zone.npy')
else:
    zone = np.loadtxt(path + 'intersection_to_zone.csv', delimiter=",", dtype=int)
    np.save(path + 'zone',zone)

zone_list = np.unique(zone[:,1])

#ADJ_all
if os.path.isfile(path + 'adj_all.npy'):
    adj_all = np.load(path + 'adj_all.npy')
else:
    adj_all = get_adj(trip,zone,zone_list)
    np.save(path + 'adj_all',adj_all)

#ADJ_07-09

if os.path.isfile(path + 'trip_0709.npy'):
    trip_0709 = np.load(path + 'trip_0709.npy')
else:
    trip_0709 = get_trip_hour(trip,1293865200)
    np.save(path + 'trip_0709',trip_0709)

adj_0709 = get_adj(trip_0709,zone,zone_list)
np.save(path + 'adj_0709',adj_0709)

#ADJ_16-18

if os.path.isfile(path + 'trip_1618.npy'):
    trip_1618 = np.load(path + 'trip_1618.npy')
else:
    trip_1618 = get_trip_hour(trip,1293897600)
    np.save(path + 'trip_1618',trip_1618)

adj_1618 = get_adj(trip_1618,zone,zone_list)
np.save(path + 'adj_1618',adj_1618)

#ADJ_month
if os.path.isfile(path + 'trip_jan.npy'):
    trip_jan = np.load(path + 'trip_jan.npy')
else:
    trip_jan = get_trip_month(trip,1293840000,31)
    np.save(path + 'trip_jan',trip_jan)

if os.path.isfile(path + 'trip_feb.npy'):
    trip_feb = np.load(path + 'trip_feb.npy')
else:
    trip_feb = get_trip_month(trip,1296518400,28)
    np.save(path + 'trip_feb',trip_feb)

if os.path.isfile(path + 'trip_mar.npy'):
    trip_mar = np.load(path + 'trip_mar.npy')
else:
    trip_mar = get_trip_month(trip,1298937600,31)
    np.save(path + 'trip_mar',trip_mar)

if os.path.isfile(path + 'trip_apr.npy'):
    trip_apr = np.load(path + 'trip_apr.npy')
else:
    trip_apr = get_trip_month(trip, 1301616000, 30)
    np.save(path + 'trip_apr',trip_apr)

if os.path.isfile(path + 'trip_may.npy'):
    trip_may = np.load(path + 'trip_may.npy')
else:
    trip_may = get_trip_month(trip, 1304208000, 31)
    np.save(path + 'trip_may',trip_may)

if os.path.isfile(path + 'trip_jun.npy'):
    trip_jun = np.load(path + 'trip_jun.npy')
else:
    trip_jun = get_trip_month(trip, 1306886400, 30)
    np.save(path + 'trip_jun',trip_jun)

if os.path.isfile(path + 'trip_jul.npy'):
    trip_jul = np.load(path + 'trip_jul.npy')
else:
    trip_jul = get_trip_month(trip, 1309478400, 31)
    np.save(path + 'trip_jul',trip_jul)

if os.path.isfile(path + 'trip_aug.npy'):
    trip_aug = np.load(path + 'trip_aug.npy')
else:
    trip_aug = get_trip_month(trip, 1312156800, 31)
    np.save(path + 'trip_aug',trip_aug)

if os.path.isfile(path + 'trip_sep.npy'):
    trip_sep = np.load(path + 'trip_sep.npy')
else:
    trip_sep = get_trip_month(trip, 1314835200, 30)
    np.save(path + 'trip_sep',trip_sep)

if os.path.isfile(path + 'trip_oct.npy'):
    trip_oct = np.load(path + 'trip_oct.npy')
else:
    trip_oct = get_trip_month(trip, 1317427200, 31)
    np.save(path + 'trip_oct',trip_oct)

if os.path.isfile(path + 'trip_nov.npy'):
    trip_nov = np.load(path + 'trip_nov.npy')
else:
    trip_nov = get_trip_month(trip, 1320105600, 30)
    np.save(path + 'trip_nov',trip_nov)

if os.path.isfile(path + 'trip_dec.npy'):
    trip_dec = np.load(path + 'trip_dec.npy')
else:
    trip_dec = get_trip_month(trip, 1322697600, 31)
    np.save(path + 'trip_dec',trip_dec)

if not os.path.isfile(path + 'adj_jan.npy'):
    np.save(path + 'adj_jan', get_adj(trip_jan, zone, zone_list))
    np.save(path + 'adj_feb', get_adj(trip_feb, zone, zone_list))
    np.save(path + 'adj_mar', get_adj(trip_mar, zone, zone_list))
    np.save(path + 'adj_apr', get_adj(trip_apr, zone, zone_list))
    np.save(path + 'adj_may', get_adj(trip_may, zone, zone_list))
    np.save(path + 'adj_jun', get_adj(trip_jun, zone, zone_list))
    np.save(path + 'adj_jul', get_adj(trip_jul, zone, zone_list))
    np.save(path + 'adj_aug', get_adj(trip_aug, zone, zone_list))
    np.save(path + 'adj_sep', get_adj(trip_sep, zone, zone_list))
    np.save(path + 'adj_oct', get_adj(trip_oct, zone, zone_list))
    np.save(path + 'adj_nov', get_adj(trip_nov, zone, zone_list))
    np.save(path + 'adj_dec', get_adj(trip_dec, zone, zone_list))


adj_mall = np.load(path + 'adj_jan.npy')+np.load(path + 'adj_feb.npy')+np.load(path + 'adj_mar.npy')+np.load(path+'adj_apr.npy')+np.load(path + 'adj_may.npy')+np.load(path + 'adj_jun.npy')+np.load(path + 'adj_jul.npy')+np.load(path + 'adj_aug.npy')+np.load(path + 'adj_sep.npy')+np.load(path + 'adj_oct.npy')+np.load(path + 'adj_nov.npy')+np.load(path + 'adj_dec.npy')
a = adj_mall == adj_all
input()