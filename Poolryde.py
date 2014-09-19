__author__ = 'Ryan Perkins'

from json import load
from urllib2 import urlopen
import urllib
from googlemaps import GoogleMaps
import geocoder


# #This is the code to find directions from one location to another using GoogleMaps.
# api_key = 'AIzaSyAyspF7tDu4Tv0X23RQDjoCoVewalLRv4Q'
# gmaps = GoogleMaps(api_key)
# start = raw_input('Enter your starting address.')
# end = raw_input('Enter your destination.')
# dirs = gmaps.directions(start, end)
# time = dirs['Directions']['Duration']['seconds']
# dist = dirs['Directions']['Distance']['meters']
# route = dirs['Directions']['Routes'][0]
# for step in route['Steps']:
#     print step['Point']['coordinates'][1], step['Point']['coordinates'][0]
#     print step['descriptionHtml']

#

#Convert an address into latitude and longitude
#To do: Use a while loop for the functions below.

def driver_start_latlng():
    driver_start = raw_input("Driver, enter your starting address.")
    results1 = geocoder.google(driver_start)
    return [str(results1.lat), str(results1.lng)]


def driver_end_latlng():
    """


    :return:
    """
    driver_end = raw_input("Driver, enter your destination.")
    results2 = geocoder.google(driver_end)
    return [str(results2.lat), str(results2.lng)]

def rider_start_latlng():
    rider_start = raw_input("Rider, enter your starting address.")
    results3 = geocoder.google(rider_start)
    return [str(results3.lat), str(results3.lng)]

def rider_end_latlng():
    rider_destination = raw_input("Rider, enter your destination.")
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


def parse_json(j):
    for node in j['rows']:
        print response

#url_lookup()
url = url_lookup()
json_obj = data_load()

data_load()
parse_json(json_obj)
#lat_lng()

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