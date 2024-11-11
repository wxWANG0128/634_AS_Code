from util import *

def main():
    trip = np.load(path + 'trip.npy')
    taxi_dis = np.unique(trip[:,0], return_counts = 'true')
    max, ind, max_taxi_id = get_max(taxi_dis)
    print('The maximum number of trips',max,'were made by taxi',max_taxi_id)
    plot_trips_per_taxi(taxi_dis)

if __name__ == "__main__":
    main()
