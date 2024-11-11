import numpy as np
import matplotlib.pyplot as plt
import scipy
import branca
import folium
from folium.plugins import HeatMap
from math import radians, cos, sin, asin, sqrt

path = ''

def get_taxi_num(trip):
    taxi = np.unique(trip[:,0])
    num = len(taxi)
    return num, taxi

def get_max(taxi_dis):
    id = [taxi_dis[0]]
    num = [taxi_dis[1]]
    taxi_dis = np.concatenate((id,num))
    max = np.max(taxi_dis[1,:])
    max_id = np.where(taxi_dis==max)
    return max, max_id[1], taxi_dis[0,max_id[1]][0]

def plot_trips_per_taxi(taxi_dis):
    X = taxi_dis[0]
    Y = taxi_dis[1]
    plt.title("Trips per taxi distribution")
    plt.xlabel('Taxi ID')
    plt.ylabel('Trips')
    plt.plot(X, Y, linewidth=0.1)
    plt.savefig("trips_per_taxi.png", dpi=300)

def get_trips_per_day(trip):
    start_time = trip[0,1]
    end_time = trip[len(trip[:,0])-1,1]
    days = int((end_time - start_time)/86400)
    end_time = start_time + days * 86400
    start_time = start_time.astype('int64')
    end_time = end_time.astype('int64')
    trips_per_day = []
    for t in range(start_time,end_time,86400):
        x_1 = trip[:,1]>=t
        x_2 = trip[:,1]<(t+86400)
        x = np.logical_and(x_1,x_2)
        sum = np.count_nonzero(x)
        trips_per_day.append(sum)
    trips_per_day = np.array(trips_per_day)
    return trips_per_day

def moving_average(interval, windowsize):
    window = np.ones(int(windowsize)) / float(windowsize)
    re = np.convolve(interval, window, 'same')
    return re

def plot_trips_per_day(trips_per_day):
    x = np.arange(1,len(trips_per_day)+1)
    Y = trips_per_day
    ind = 0
    for i in Y:
        if i < 280000:
            Y[ind] = max(280000,int((Y[ind-1]+Y[ind+1])/2))
        ind = ind+1
    #Y_smooth = moving_average(Y,30)
    Y_smooth = scipy.signal.savgol_filter(Y, 80, 4)
    fig, ax = plt.subplots()
    y1 = Y
    ax.plot(x, y1, label='raw data', linewidth=0.4)
    y2 = Y_smooth
    ax.plot(x, y2, label='smooth data', linewidth=0.8)
    ax.set_xlabel('day')
    ax.set_ylabel('trips')
    ax.set_title('Trips distribution per day')
    ax.legend()
    plt.ylim(100000, 500000)
    #plt.show()
    plt.savefig("trips_per_day.png", dpi=300)

def get_trip_loc_dis(location,trip,mode):
    heat = []
    if mode == 'dep':
        ind = 3
    elif mode == 'arr':
        ind = 4
    else: raise AssertionError('mode invalid')
    for i in location[:,0]:
        x = trip[:,ind] == i
        sum = np.count_nonzero(x)
        heat.append(sum)
    heat = np.asarray(heat)
    np.save(path+'heat_'+mode,heat)
    return heat

def plot_trip_loc_dis(trip_dis_dep,trip_dis_arr):
    fig = branca.element.Figure()
    subplot1 = fig.add_subplot(1, 2, 1)
    subplot2 = fig.add_subplot(1, 2, 2)
    m1 = folium.Map(location=(40.77875878795411, -73.96835192523795),
                    zoom_start=13,
                    tiles="cartodb positron",
                    control_scale=True)
    m2 = folium.Map(location=(40.77875878795411, -73.96835192523795),
                    zoom_start=13,
                    tiles="cartodb positron",
                    control_scale=True)
    r = 25
    b = 30
    HeatMap(trip_dis_dep, radius=r, blur=b, max_zoom=5).add_to(m1)
    HeatMap(trip_dis_arr, radius=r, blur=b, max_zoom=5).add_to(m2)
    subplot1.add_child(m1)
    subplot2.add_child(m2)
    fig.save("task4.html")

def get_trips_in_day(trip,start_time):
    end_time = start_time + 86400
    trips_in_day = []
    for t in range(start_time,end_time-1800,1800):
        x_1 = trip[:,1]>=t
        x_2 = trip[:,1]<(t+1800)
        x = np.logical_and(x_1,x_2)
        sum = np.count_nonzero(x)
        trips_in_day.append(sum)
    trips_in_day = np.array(trips_in_day)
    return trips_in_day

def plot_trips_in_day(trips_in_day_1,trips_in_day_2,trips_in_day_3):
    x = np.arange(1,len(trips_in_day_1)+1)
    Y_1 = trips_in_day_1
    Y_2 = trips_in_day_2
    Y_3 = trips_in_day_3
    fig, ax = plt.subplots()
    y1 = Y_1
    ax.plot(x, y1, label='Jan 11', linewidth=0.6)
    y2 = Y_2
    ax.plot(x, y2, label='Jul 09', linewidth=0.6)
    y3 = Y_3
    ax.plot(x, y3, label='Sep 07', linewidth=0.6)
    ax.set_xlabel('/2 hour')
    ax.set_ylabel('trips')
    ax.set_title('Trips distribution in day')
    ax.legend()
    plt.xlim(0,48)
    # plt.show()
    plt.savefig("trips_in_day.png", dpi=300)



def geodistance(lng1,lat1,lng2,lat2):
    lng1, lat1, lng2, lat2 = map(radians, [float(lng1), float(lat1), float(lng2), float(lat2)])
    dlon=lng2-lng1
    dlat=lat2-lat1
    a=sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    distance=2*asin(sqrt(a))*6371*1000
    distance=round(distance/1000,3)
    return distance

def get_dist_and_time(trip,location):
    dist = []
    time = []
    for i in range(0, len(trip[:, 0]), 1):
        id_1 = int(trip[i,3]-1)
        id_2 = int(trip[i,4]-1)
        lng1 = location[id_1, 1]
        lat1 = location[id_1, 2]
        lng2 = location[id_2, 1]
        lat2 = location[id_2, 2]
        dist.append(geodistance(lng1, lat1, lng2, lat2))
        interval = np.int64(trip[i, 2]) - np.int64(trip[i, 1])
        if interval>3600*4 or interval<1:
            print(i,interval)
        else:
            time.append(interval/60)

    return np.array(dist), np.array(time)

def gen_time_prob(time_dis):
    time_prob = []
    for t in range(0,235,5):
        x_1 = time_dis>=t
        x_2 = time_dis<(t+5)
        x = np.logical_and(x_1,x_2)
        sum = np.count_nonzero(x)
        time_prob.append(sum)
    time_prob = np.array(time_prob)
    time_dis_sum = np.sum(time_prob)
    time_prob_ = []
    for i in range(0,len(time_prob),1):
        time_prob_.append(time_prob[i]/time_dis_sum)
    time_prob_ = np.array(time_prob_)
    return time_prob_

def gen_dist_prob(dist_dis):
    dist_prob = []
    for d in np.arange(0.,13.,0.1):
        x_1 = dist_dis>=d
        x_2 = dist_dis<(d+0.1)
        x = np.logical_and(x_1,x_2)
        sum = np.count_nonzero(x)
        dist_prob.append(sum)
    dist_prob = np.array(dist_prob)
    dist_dis_sum = np.sum(dist_prob)
    dist_prob_ = []
    for i in range(0,len(dist_prob),1):
        dist_prob_.append(dist_prob[i]/dist_dis_sum)
    dist_prob_ = np.array(dist_prob_)
    return dist_prob_

def plot_time_prob(time):
    X = range(0,120,5)
    Y = time[:24]
    plt.title("Trip time probability distribution")
    plt.xlabel('Time (min)')
    plt.ylabel('Probability')
    plt.plot(X, Y, linewidth=0.6)
    #plt.show()
    plt.savefig("time_prob.png", dpi=300)

def plot_dist_prob(dist):
    X = np.arange(0.,13.,0.1)
    Y = dist
    plt.title("Trip distance probability distribution")
    plt.xlabel('Distance (km)')
    plt.ylabel('Probability')
    plt.plot(X, Y, linewidth=0.6)
    #plt.show()
    plt.savefig("dist_prob.png", dpi=300)