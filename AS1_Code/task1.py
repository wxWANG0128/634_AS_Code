from util import *

def main():
    trip = np.loadtxt(path+'taxi_id.csv',delimiter=",")
    trip_num = len(trip[:,0])
    taxi_num, taxi = get_taxi_num(trip)
    np.save(path + 'taxi', taxi)
    np.save(path + 'trip', trip)
    print('Number_of_taxi:',taxi_num,'Number_of_trips:',trip_num)

if __name__ == "__main__":
    main()