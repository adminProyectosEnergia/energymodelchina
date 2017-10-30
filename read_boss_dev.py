# This code was executed in Python V3.6
#Reference: https://automatetheboringstuff.com/chapter15/
# https://pypi.python.org/pypi/schedule

import schedule, time
from time import gmtime, strftime
import requests
from requests.auth import HTTPBasicAuth
import json

account= 'duke.e.demand@gmail.com'
password= 'duke@123'

device_id = 'bcf3f09b3d99af32be661cedaf7b05b64d86f029'

#Request to get data from metering devices
print("-----------------------------------------Get Data----------------------")
url6 ='https://account.bosscontrols.com/api/portals/v1/data-sources/'+ device_id +'/data'

#def print_time(a='default'):
#     print("Time", time.time(), a)

def reqbossdata():
    r6=requests.get(url6, auth=HTTPBasicAuth(account,password))

    #parse json response
    json_data= r6.json()[0]

    sample_dict = json.loads(json_data[1]).get('sample')
    #print('Dictionary: {0}'.format(sample_dict))

    instant_power = sample_dict.get('mw')
    instant_voltage = sample_dict.get('mv')
    instant_current= sample_dict.get('ma')
    instant_pf = sample_dict.get('pf')
    #print results
    #print("----------------------")
    current_time= strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())

    print('Time: {0}, Time: {1}, Power: {2}, Voltage: {3}, Current: {4}, PF: {5}'.format(current_time, 
            time.time(), instant_power, instant_voltage, instant_current,instant_pf))


if __name__ == "__main__":
    reqbossdata()
    schedule.every(1).minutes.do(reqbossdata)
    while True:
        schedule.run_pending()
        #just to do something
        time.sleep(0.5)
        #print('Pause') 