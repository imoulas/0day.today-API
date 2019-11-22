#a tiny parser to filter data
#Isidoros Moulas
#imoulas@hotmail.com


import argparse
import time
from datetime import datetime, date, time, timedelta

parser = argparse.ArgumentParser(description='0day.today api')

parser.add_argument('--search', help="Search text")
parser.add_argument('--days',  help="How many days back, default=30")
parser.add_argument('--output', help="nice/csvm default=nice")
parser.set_defaults(days=30,output='nice')

args = parser.parse_args()

if not args.search:
    parser.error("--search must be given")

search_param = args.search
days_param = int(args.days)
output_param = args.output

from ApiLib import api_0day_today

Api = api_0day_today()

print "Searching '{}' in 0day.today database".format(search_param)

results = Api.search(search_param)

if results["status"] != "fail":

    for result in results["response"]:
        date_time_obj = datetime.strptime(result["date"], '%d-%m-%Y')
        diff = datetime.now() - date_time_obj
        if diff.days<=days_param:
           if output_param=='nice':
              print "====== Exploit ======="
              print "Date: {}\nDescription: {}\nPlatform: {}\nPrice: {}\nAuthor: {}\nURL: {}".format(result["date"], result["desc"], result["platform"], result["price"], result["author"], result["url"])
              print "======================"
           if output_param=='csv':
              print "{},{},{}".format(result["date"],result["platform"],result["desc"].replace(",",""))

else:

    print "[ERROR] {}".format(results["exception"])
