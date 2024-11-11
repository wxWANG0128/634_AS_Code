import numpy as np
import matplotlib.pyplot as plt
import scipy
import branca
import folium
from folium.plugins import HeatMap
from math import radians, cos, sin, asin, sqrt

path = 'data/'


def get_adj(trip, zone, zone_list):
    adj = np.zeros((63, 63), dtype=int)
    for i in range(len(trip[:, 0])):
        if (np.any(zone[:, 0] == trip[i, 3]) and
                np.any(zone[:, 0] == trip[i, 4])
        ):
            ind_o = np.where(zone[:, 0] == trip[i, 3])[0][0]
            ind_d = np.where(zone[:, 0] == trip[i, 4])[0][0]
            ind_o = np.where(zone_list == zone[ind_o, 1])[0][0]
            ind_d = np.where(zone_list == zone[ind_d, 1])[0][0]
            adj[ind_o, ind_d] += 1
    return adj


def get_trip_hour(trip, start_time):
    end_time = start_time + 31449600
    ind = trip[:, 1] < 0
    for t in range(start_time, end_time + 86400, 86400):
        ind_new = np.logical_and(trip[:, 1] >= start_time, trip[:, 1] < start_time + 7200)
        ind = np.logical_or(ind, ind_new)
    trip_hour = trip[ind]
    return trip_hour


def get_trip_month(trip, start_time, day):
    ind = np.logical_and(trip[:, 1] >= start_time, trip[:, 1] < start_time + day * 86400)
    trip_month = trip[ind]
    return trip_month
