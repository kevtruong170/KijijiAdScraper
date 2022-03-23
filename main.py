from bs4 import BeautifulSoup
import requests
import adClass
import time
import emailClient
import filterFuncs
import parseAd

userEmail = emailClient.eLogin()
if userEmail is None:
    quit()

#Car filter
carList = filterFuncs.findCars

#Add functionality for location filter
location = filterFuncs.location
locationFilter = filterFuncs.retrieveLocation(location)

#Checking if user specified a location
if locationFilter is None:
    defaultLocation = 1
else:
    defaultLocation = 0

x = 1
newCar = 0

while x == 1:
    for car in carList:
        adList = []
        #Creating the link that will be used to search the car
        searchLink = filterFuncs.createLink(defaultLocation, car, location, locationFilter)
        response = requests.get(searchLink)
        siteListings = BeautifulSoup(response.text, 'lxml')

        #Filtering listings by removing third-party ads
        ads = siteListings.find_all("div", attrs={"class": ["info"]})
        ads = [x for x in ads if ("cas-channel" not in x["class"]) & ("third-party" not in x["class"])]

        #Parsing an ad
        for div in ads:
            datePosted = parseAd.getDate(div)
            if datePosted is None:
                continue

            #Retrieving title
            title = parseAd.getTitle(div)

            #Retrieving link
            link = parseAd.getLink(div)

            #Retrieving location
            location = parseAd.getLoc(div)

            #Retrieving price
            price = parseAd.getPrice(div)

            #Retreiving description
            description = parseAd.getDesc(div)

            #Adding into list object
            adObj = adClass.Listing(title, link, location, datePosted, price, description)
            adList.append(adObj)

        for listing in adList:
            newCar = 1;
            emailClient.sendEmail(listing, userEmail)

    #Sends response to user if last update contains a new car
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S ", t)

    if newCar == 1:
        print(current_time + "New car sent")

    else:
        print(current_time + "No new car")

    newCar = 0
    time.sleep(600)