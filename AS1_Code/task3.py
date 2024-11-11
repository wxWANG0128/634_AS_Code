from util import *
import os.path

def main():
    if not os.path.isfile(path + 'trips_per_day.npy'):
        trip = np.load(path + 'trip.npy')
        trips_per_day = get_trips_per_day(trip)
        np.save(path + 'trips_per_day',trips_per_day)
    else:
        trips_per_day = np.load(path + 'trips_per_day.npy')

    plot_trips_per_day(trips_per_day)

if __name__ == "__main__":
    main()