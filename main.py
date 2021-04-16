import requests
import logging
import random
import time
import sys
logging.basicConfig(filename='getter.log', level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', filemode='w')


url = sys.argv[1]
interval = sys.argv[2]
header = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:77.0) Gecko/20100101 Firefox/77.0"}

test = requests.get(url, headers=header)
if test.status_code == 200:
    print("Got 200, reaching {} with max interval {}".format(url,interval))
else:
    sys.exit(1)


while True:
    pause = random.randrange(0, int(interval))
    time.sleep(pause/1000)
    req = requests.get(url, headers=header)
    logging.info("{} RESPONSE: {}".format(url, req.status_code))