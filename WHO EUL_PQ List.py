import requests
import re
from os import path

# Get response from WHO
url = 'https://extranet.who.int/pqweb/key-resources/documents/status-covid-19-vaccines-within-who-eulpq-evaluation-process'
r = requests.get(url)

# Extract filename with re from url
filename = re.findall('(?:.+\/)(.+)',r.url)[0]

# Save file if there's latest version
if path.exists(filename):
    print('Latest verson already in folder. Please come back several days later!')
else:
    with open(filename, 'wb') as f:
        f.write(r.content)
