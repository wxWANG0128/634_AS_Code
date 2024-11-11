import numpy as np
from util import *
import os

def main():
    trip = np.load('trip.npy')
    location = np.load('location.npy')

    if not os.path.isfile(path + 'dist_dis.npy'):
        dist_dis, time_dis = get_dist_and_time(trip, location)
        np.save(path + 'dist_dis', dist_dis)
        np.save(path + 'time_dis', time_dis)
    else:
        dist_dis = np.load(path + 'dist_dis.npy')
        time_dis = np.load(path + 'time_dis.npy')

    time_dis_p = gen_time_prob(time_dis)
    dist_dis_p = gen_dist_prob(dist_dis)

    plot_time_prob(time_dis_p)
    #plot_dist_prob(dist_dis_p)

if __name__ == "__main__":
    main()