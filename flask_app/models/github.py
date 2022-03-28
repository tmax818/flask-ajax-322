import requests
import json

class Github:
    def __init__( self , data ):
        self.avatar_url = data['avatar_url']
        self.bio = data['bio']
        self.html_url = data['html_url']
        self.name = data['name']


    @classmethod
    def data(cls, name):
        endpoint = f"https://api.github.com/users/{name}"
        res = requests.get(endpoint)
        return res.json()

    @classmethod
    def data_for_html(cls, name):
        endpoint = f"https://api.github.com/users/{name}"
        res = requests.get(endpoint)
        return res.json()
     