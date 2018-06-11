## Python Code to connect to the Drive using OAuth2.0
## By Anubhav Kumar

## CLient Id = 447774622426-70oin522m8b20ofq6og4f69fgpfvokd7.apps.googleusercontent.com

import requests

session = requests.Session()
r = session.get("https://www.googleapis.com/auth/drive?client_id=447774622426-70oin522m8b20ofq6og4f69fgpfvokd7.apps.googleusercontent.com&redirectUrl=www.google.com")
print r.text


