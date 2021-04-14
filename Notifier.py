from plyer import notification
import datetime
import time
import json
import requests

data=None
try:
    data=requests.get("https://corona-rest-api.herokuapp.com/Api/india")

except:
    print("No internet")

if(data!=None):
    data=data.json()["Success"]
while(True):

    notification.notify(
        title="COVID 19 stats on {} ".format(datetime.date.today()),
        message="Total cases: {totalcases}\nToday cases{todaycases}\nToday active:{active}".format(
            totalcases=data['cases'],
            todaycases=data['todayCases'],
            # todaydeaths=data['todayDeaths'],
            active= data['active']),
        #  app_icon=("Hopstarter-Malware-Malware.ico"),
        timeout= 50,
    )
    time.sleep(60*60*24)

        
    


