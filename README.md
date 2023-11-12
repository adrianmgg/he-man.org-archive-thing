
# about
saw [this post](https://www.tumblr.com/clarenecessities/733543437902757889), decided to throw together a script to archive threads

# setup
1. clone this repo
1. install the requirements `python3 -m pip install -r requirements.txt`

i might set this up as a pip installable thing but for now this is it

# usage
given this thread as an example https://www.he-man.org/forums/boards/showthread.php?168773-United-Kingdom-Collector-s-Delivery-Thread  
to save from page 17 to the end (which at time of writing is page 328), do this[^python3-executable]:
```
python3 archive.py --thread-id "168773-United-Kingdom-Collector-s-Delivery-Thread" --start-page 17 --end-page 328
```
and it should start saving pages
```
saving page 17...
page 17 saved at https://web.archive.org/web/20231112092515/https://www.he-man.org/forums/boards/showthread.php?168773-United-Kingdom-Collector-s-Delivery-Thread%2Fpage17
saving page 18...
page 18 saved at https://web.archive.org/web/20231112092627/https://www.he-man.org/forums/boards/showthread.php?168773-United-Kingdom-Collector-s-Delivery-Thread%2Fpage18
saving page 19...
page 19 saved at https://web.archive.org/web/20231112092653/https://www.he-man.org/forums/boards/showthread.php?168773-United-Kingdom-Collector-s-Delivery-Thread%2Fpage19
saving page 20...
page 20 saved at https://web.archive.org/web/20231112092710/https://www.he-man.org/forums/boards/showthread.php?168773-United-Kingdom-Collector-s-Delivery-Thread%2Fpage20
saving page 21...
page 21 saved at https://web.archive.org/web/20231112092733/https://www.he-man.org/forums/boards/showthread.php?168773-United-Kingdom-Collector-s-Delivery-Thread%2Fpage21
... and so on ...
```

[^python3-executable]: your python executable might not be `python3`, e.g. if you're on windows it might be `py -3`

i've only tested this script on python 3.11, but other relatively new 3.x versions should work too

when i run this it gets the occasional error, which seem to be from captures that got back a database error ([example](https://web.archive.org/web/20231112094951/https://www.he-man.org/forums/boards/showthread.php?168773-United-Kingdom-Collector-s-Delivery-Thread%2Fpage75)). those database errors don't seem to consistently happen though, so you can save it again later, but with the current version of this script you'll need to just look thru the log to see which ones failed and then manually redo them later.

# authenticating

you can save more pages per minute if you authenticate with your archive.org account. pass the `--authenticate` flag to archive.py if you're doing this, and see [this section of savepagenow's docs](https://palewi.re/docs/savepagenow/python.html#authentication) for where to put the credentials



