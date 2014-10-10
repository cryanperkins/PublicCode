__author__ = 'Ryan Perkins'

from json import load
from urllib2 import urlopen
import urllib
from googlemaps import GoogleMaps
import geocoder
import json
#

#Convert an address into latitude and longitude
#To do: Use a while loop for the functions below.
driver_start = raw_input("Driver, enter your starting address.")
driver_end = raw_input("Driver, enter your destination.")
rider_start = raw_input("Rider, enter your starting address.")
rider_destination = raw_input("Rider, enter your destination.")



def driver_start_latlng():
    results1 = geocoder.google(driver_start)
    return [str(results1.lat), str(results1.lng)]


def driver_end_latlng():
    results2 = geocoder.google(driver_end)
    return [str(results2.lat), str(results2.lng)]


def rider_start_latlng():
    results3 = geocoder.google(rider_start)
    return [str(results3.lat), str(results3.lng)]


def rider_end_latlng():
    results4 = geocoder.google(rider_destination)
    return [str(results4.lat), str(results4.lng)]


def url_lookup():

    driver_start = ",".join(driver_start_latlng())

    rider_start = ",".join(rider_start_latlng())

    driver_destination = ",".join(driver_end_latlng())

    rider_destination = ",".join(rider_end_latlng())

    url = 'https://maps.googleapis.com/maps/api/distancematrix/json?'
    url += 'origins='
    url += driver_start + "|"
    url += rider_start + "|"
    url += rider_destination + "|"
    url += '&destinations='
    url += driver_destination + "|"
    url += rider_start + "|"
    url += rider_destination + "|"
    url += 'mode=driving&language=en-EN&'
    #url += 'key=AIzaSyAyspF7tDu4Tv0X23RQDjoCoVewalLRv4Q'
    return url


def data_load(url):
    response = urlopen(url)
    j = load(response)
    return j


def parse_json(json_object):
    """
    first duration dict object is the driver start to driver end
    second duration dict object is the driver start to rider start
    third duration dict object is the driver start to the rider end

    fourth duration dict object is the rider start to the driver end
    fifth duration dict object is the rider start to rider start
    sixth duration dict object is the rider start to the rider end
    seventh duration dict object is the rider end to the driver end
    eighth duration dict object is the rider end to the rider start
    ninth duration dict object is the rider end to the rider end
    :json object is passed in:
    """
    rows = json_object['rows']
    final_durations = []
    for row in rows:
        elements = row['elements']
        durations = {}
        for e in elements:
            if 'duration' in e.keys():
                duration = e['duration']['value']
                durations['duration'] = duration
                final_durations.append(duration)
    return final_durations


#This function below will calculate the extra amount of time that would be added
#to the driver's drive time if a passenger is picked up and dropped off at her destination first.
#It then informs the driver of the extra time added to the trip and asks if he would still like to pick up the poolryder.
#If the driver elects to pick up the poolryder the program moves to the get_directions function.  If the driver declines
#an incentive is offered in the attempt to bribe the driver and if that doesn't work the program ends.
def get_extra_driving_time(list_of_times):

    times = list_of_times
    extra_driving_time = (times[1] + times[5] + times[6] - times[0])/60

    if extra_driving_time >= 60:
        hours = extra_driving_time/60
        print "This will add {} hours to your drive time.".format(hours)
        ask_user = raw_input("If you would like to pick up this rider and get directions enter 'y', if not, press 'n'").lower()
        if ask_user == 'y':
            return get_directions()
        else:
            ask_user = raw_input("What if I gave you a free ice cream cone?  Enter 'y' or 'n'.").lower()
            if ask_user == 'y':
                print ("Awesome, ice cream is the best, and so are you.")
                return get_directions()
            else:
                print("Fine, be that way.")
    else:
        print "This will add {} minutes to your drive time".format(extra_driving_time)
        ask_user = raw_input("If you would like to pick up this rider and get directions enter 'y', if not, press 'n'").lower()
        if ask_user == 'y':
            return get_directions()
        else:
            ask_user = raw_input("What if I took you out to Denny's?  Enter 'y' or 'n'.").lower()
            if ask_user == 'y':
                print ("Great choice.  Denny's was my grandfather's favorite.")
                return get_directions()
            else:
                print("What's wrong with you?  Who could refuse Denny's?")


#This is the code to find directions from the driver's origin to the rider's origin to the rider's
#destination to the driver's destination using GoogleMaps.
def get_directions():
    api_key = 'AIzaSyAyspF7tDu4Tv0X23RQDjoCoVewalLRv4Q'
    gmaps = GoogleMaps(api_key)
    start = ",".join(driver_start_latlng())
    end = ",".join(rider_start_latlng())
    start2 = ",".join(rider_end_latlng())
    end2 = ",".join(driver_end_latlng())
    dirs = gmaps.directions(start, end)
    time = dirs['Directions']['Duration']['seconds']
    dist = dirs['Directions']['Distance']['meters']
    route = dirs['Directions']['Routes'][0]
    dirs1 = gmaps.directions(end, start2)
    time1 = dirs1['Directions']['Duration']['seconds']
    dist1 = dirs1['Directions']['Distance']['meters']
    route1 = dirs1['Directions']['Routes'][0]
    dirs2 = gmaps.directions(start2, end2)
    time2 = dirs2['Directions']['Duration']['seconds']
    dist2 = dirs2['Directions']['Distance']['meters']
    route2 = dirs2['Directions']['Routes'][0]
    for step in route['Steps']:
        #print step['Point']['coordinates'][1], step['Point']['coordinates'][0]
        print step['descriptionHtml']
    for step in route1['Steps']:
        #print step['Point']['coordinates'][1], step['Point']['coordinates'][0]
        print step['descriptionHtml']
    for step in route2['Steps']:
       # print step['Point']['coordinates'][1], step['Point']['coordinates'][0]
        print step['descriptionHtml']



request = url_lookup()
## json_obj = data_load()
#
## data_load()
## parse_json(json_obj)
##lat_lng() mk8
json_response = data_load(request)

times = parse_json(json_response)

get_extra_driving_time(times)
#maps = get_directions
#get_directions()

#get_directions()
# # https://maps.googleapis.com/maps/api/geocode/output?parameters
#
# # #Get the distance between two coordinates.
# orig_lat = '15.33.82'
# orig_lng = '2.29.45'
#
# dest_lat = '30.09.30'
# dest_lng = '18.68.32'


#
# orig_coord = orig_lat, orig_lng
# dest_coord = dest_lat, dest_lng
# format(str(orig_coord), str(dest_coord))
# result = json.load(urllib.urlopen(url))
# print(result)
# driving_time = result['rows'][0]['elements'][0]['duration']['value']
# print(driving_time)
#


# orig_coord = orig_lat, orig_lng
# dest_coord = dest_lat, dest_lng

# origins=Bobcaygeon+ON|41.43206,-81.38992
# destinations=Darling+Harbour+NSW+Australia|24+Sussex+Drive+Ottawa+ON|Capitola+CA

# def driving_time():
##http://maps.googleapis.com/maps/api/distancematrix/json?origins=Vancouver+BC|Seattle&destinations=San+Francisco|Victoria+BC&mode=bicycling&language=fr-FR&key=API_KEY
#url = 'http://maps.googleapis.com/maps/api/distancematrix/json?origins=start|&destinations=end|Victoria+BC&mode=driving&language=en-EN&key=api_KEY'
#
# url = "http://maps.googleapis.com/maps/api/distancematrix/json?origins={0}&destinations={1}&mode=driving&language=en-EN&sensor=false".format(str(orig_coord),str(dest_coord))
# result= simplejson.load(urllib.urlopen(url))
# driving_time = result['rows'][0]['elements'][0]['duration']['value']
# print driving_time

# #The idea here is to create a user class, under which we will have both drivers and riders.  Drivers can be riders and riders can be drivers.
# Class User():
#     def __init__(self,username):
#         self.username = username
#
#     def create_profile(self, name, address, email):
#         self.name = input('What is your name?')
#         self.address = raw_input("What is your address?")
#         self.email = raw_input("What is your email address?")
#
#

#     def __driver__(self, driver_loc, driver_destination):
#         self.driver_loc = raw_input('What is your starting address?'
#         self.driver_destination = raw_input('Where do you want to go?')
#
#
# Class_Rider(User):
#     def __rider__(self, rider_loc, rider_destination)
#     self.rider_loc = raw_input("From where do you want a ride?")
#     self.rider_destination = raw_input("Where do you want to go?")
#
# def driver(dst, dd):
#     for address in dst
#     driver_start = raw_input("Driver, enter your starting address.")
#     driver_destination= raw_input("Driver, enter your destination.")
#
#     return driver_start, driver_destination
#
# def rider(r):
#     rider_start = raw_input("Rider, enter your starting address.")
#     rider_destination = raw_input("Rider, enter your destination.")
#     return r #rider_start, rider_destination
#
# #driver()

