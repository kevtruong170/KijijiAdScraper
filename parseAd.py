import filterFuncs

def getDate(div):
    #Parsing date
    adDate = div.find(attrs={"class": ["date-posted"]}).text.strip()
    #Checking time because we only take ads newer than 10 minutes
    time = checkTime(adDate)
    #If none, that means there time is longer than an hour
    if time is None:
        return None

    #If minutes is less than 10, we return the datetime
    if int(time) < 10:
        return adDate

def checkTime(datePosted):
    numericTime = ""
    if "minutes" in datePosted:
        for text in datePosted:
            #Only grabbing the integers if ad was posted within minutes
            if text.isdigit():
                numericTime = numericTime + text
        return numericTime
    else:
        return None

def getTitle(div):
    return div.find(attrs={"class": ["title"]}).text.strip()

def getLink(div):
    #Use thise method to grab href tags
    link = div.find('a')
    link = filterFuncs.siteLink + link.get('href')
    return link

def getLoc(div):
    location = div.find(attrs={"class": ["location"]}).text.strip()
    #Removes trailing whitespace/breaks in text due to Kijiji parsing format
    location = location.split("\n")[0]
    return location

def getPrice(div):
    div.find(attrs={"class": ["price"]}).text.strip()

def getDesc(div):
    description = div.find(attrs={"class": ["description"]}).text.strip()
    fullDesc = ""
    breakWord = description.split("\n")
    fullDesc = breakWord[0]
    # Weird parsing of kijiji description using BS4, if there is a second line, also grab that

    try:
        if "\n" not in breakWord[1]:
            fullDesc = fullDesc + " " + breakWord[1]
    except:
        print("No second line")
    return fullDesc