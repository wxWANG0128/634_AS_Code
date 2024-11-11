from os import path
import os
from util import *

def main():
    if not os.path.isfile(path + 'location.npy'):
        location = np.loadtxt(path + 'intersections.csv', delimiter=",")
        np.save(path + 'location', location)
    else:
        location = np.load(path + 'location.npy')

    trip = np.load('trip.npy')

    if not os.path.isfile(path + 'heat_arr.npy'):
        trip_arr = get_trip_loc_dis(location, trip, 'arr')
    else:
        trip_arr = np.load('heat_arr.npy')

    if not os.path.isfile(path + 'heat_dep.npy'):
        trip_dep = get_trip_loc_dis(location, trip, 'dep')
    else:
        trip_dep = np.load('heat_dep.npy')

    trip_dep = np.expand_dims(trip_dep, axis=1)
    trip_dis_dep = np.concatenate((location[:,1:],trip_dep),axis=1)
    trip_arr = np.expand_dims(trip_arr, axis=1)
    trip_dis_arr = np.concatenate((location[:,1:],trip_arr),axis=1)

    plot_trip_loc_dis(trip_dis_dep,trip_dis_arr)

if __name__ == "__main__":
    main()
