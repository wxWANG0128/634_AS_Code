from util import *
import os.path

def main():
    start_time_1 = 1294722000
    start_time_2 = 1310187600
    start_time_3 = 1315371600

    trip = np.load('trip.npy')

    if not os.path.isfile(path + 'trips_in_day_0111.npy'):
        trips_in_day_0111 = get_trips_in_day(trip, start_time_1)
        np.save(path + 'trips_in_day_0111', trips_in_day_0111)
    else:
        trips_in_day_0111 = np.load(path + 'trips_in_day_0111.npy')

    if not os.path.isfile(path + 'trips_in_day_0709.npy'):
        trips_in_day_0709 = get_trips_in_day(trip, start_time_2)
        np.save(path + 'trips_in_day_0709', trips_in_day_0709)
    else:
        trips_in_day_0709 = np.load(path + 'trips_in_day_0709.npy')

    if not os.path.isfile(path + 'trips_in_day_0907.npy'):
        trips_in_day_0907 = get_trips_in_day(trip, start_time_3)
        np.save(path + 'trips_in_day_0907', trips_in_day_0907)
    else:
        trips_in_day_0907 = np.load(path + 'trips_in_day_0907.npy')

    plot_trips_in_day(trips_in_day_0111, trips_in_day_0709, trips_in_day_0907)

if __name__ == "__main__":
    main()

