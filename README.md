# 0day.today unofficial API | 0.2 beta
![Banner.png](https://raw.githubusercontent.com/MrSentex/0day.today-API/master/banner.png?token=AorkL9f8tQVCKNF6tnFOxW4LHEu_1_E4ks5cPhNmwA%3D%3D)

Unofficial API for 0day.today database.

This API is not affiliated in any way with "0day.today" and its operation may be against the terms and conditions of "0day.today", therefore the execution of the API will be carried out under the legal responsibility of the user and MrSentex will be uncharged from any illegal use of the API.

#### Special thanks: 

* @virtualminds (Telegram)

## Dependencies

All you need to use the API and start to work with it.

### Python

Dependencies needed to use the API with Python

* Python 2.7 with PyPi (pip)


Python packages needed:

* requests
* bs4
* unidecode

These dependencies are available in PyPi so they can be installed from the command `pip install <package>` or they can be installed with the following command: `pip install -r requeriments.txt` (Must be executed from the folder).

#### Usage

```python
from ApiLib import api_0day_today

search_param = "ssh"

Api = api_0day_today()

print "Searching '{}' in 0day.today database".format(search_param)

results = Api.search(search_param)

if results["status"] != "fail":

    for result in results["response"]:

        print "====== Exploit ======="
        print "Date: {}\nDescription: {}\nPlatform: {}\nPrice: {}\nAuthor: {}\nURL: {}".format(result["date"], result["desc"], result["platform"], result["price"], result["author"], result["url"])
        print "======================"

else:

    print "[ERROR] {}".format(results["exception"])
```

### PHP

Dependencies needed to use the API with PHP

* PHP (5/7)

PHP modules needed:

* php-curl
* php-xml
* parser.php (Already in repo, downloaded from http://simplehtmldom.sourceforge.net/)

The first two packages are installed through `apt`, `yum` or any other linux package installer. In the case of windows `php-xml` is already included in the php core and for the install of `php-curl` is necessary to modify the php.init file and possibly download php_curl.dll .

#### Usage
```php
<?php

    include("ApiLib.php");

    $api_0day_today = new api_0day_today();

    $search_param = "ssh";

    $search = $api_0day_today->search($search_param);

    if ($search["status"] === "fail") {
        printf("[Error] ".$search["exception"]."\n"); die();
    }

    foreach($search["response"] as $hit) {
        printf("====== Exploit ======\n");
        printf("Date: %s\n", $hit["date"]);
        printf("Description: %s\n", $hit["desc"]);
        printf("Platform: %s\n", $hit["platform"]);
        printf("Price: %s\n", $hit["price"]);
        printf("Author: %s\n", $hit["author"]);
        printf("URL : %s\n", $hit["url"]);
        printf("======================\n");
    }

?>
```

Also you can use search.py to filter the output.

#### Usage
```bash
usage: search.py [-h] [--search SEARCH] [--days DAYS] [--output OUTPUT]

0day.today api

optional arguments:
  -h, --help       show this help message and exit
  --search SEARCH  Search text
  --days DAYS      How many days back, default=30
  --output OUTPUT  nice/csv default=nice


python search.py --search sql --days 20 --output csv
Searching 'sql' in 0day.today database
12-11-2019,php,CBAS-Web 19.0.0 - (id) Boolean-based Blind SQL Injection Vulnerability
06-11-2019,asp,SD.NET RIM 4.7.3c - (idtyp) SQL Injection Vulnerability
06-11-2019,php,html5_snmp 1.11 - (Router_ID) SQL Injection Vulnerability
06-11-2019,php,rimbalinux AhadPOS 1.11 - (alamatCustomer) SQL Injection Vulnerability
06-11-2019,php,thejshen Globitek CMS 1.4 - (id) SQL Injection Vulnerability

```

