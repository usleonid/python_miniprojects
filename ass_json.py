from urllib.request import urlopen
# import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter location: ')
print('Retrieving', address)
uh = urlopen(address, context=ctx)
# uh = urllib.request.urlopen(address, context=ctx)

data = uh.read().decode()
print('Retrieved', len(data), 'characters')

sum = 0

info = json.loads(data)
for item in info['comments']:
    icount = int(item['count'])
    sum = sum + icount
print('Sum:',sum)
