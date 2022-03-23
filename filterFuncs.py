siteLink = "https://www.kijiji.ca"
itemFilter = "/b-cars-trucks"
#Set specific location here
location = ""

#The location list is larger, provided three as an example
locationFilters = {
    "brantford": "k0c174l1700206",
    "kitchener-area": "k0c174l1700209",
    "gta-greater-toronto-area": "k0c174l1700272"
}

#Insert cars here, instead of spaces, use hyphens
findCars = ['acura-rsx', 'honda-civic-si','acura-integra', 'mazda-miata', 'honda-civic']

def retrieveLocation(stringLocation):
    #If none, user did not insert specified location
    if locationFilters.get(stringLocation) is None:
        print("Default location is set to Ontario")
        return None
    else:
        print("Location is set to: " + stringLocation)
        return locationFilters[stringLocation]

def createLink(defaultLocation, currCar, thisLoc, currLoc):
    if defaultLocation == 0:
        stringLoc = siteLink + itemFilter + "/" + thisLoc + "/" + currCar + "/" + currLoc
        return stringLoc
    else:
        stringLoc = "https://www.kijiji.ca/b-cars-trucks/ontario/" + currCar + "/new__used/k0c174l9004a49?rb=true"
        return stringLoc