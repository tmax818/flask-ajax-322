
import requests

DATABASE = 'models_schema'

class Model:
    def __init__( self , data ):
        self.id = data['id']
        self.param1 = data['param1']
        self.param2 = data['param2']
        self.param3 = data['param3']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def data(cls):
        name = "tmax818"
        endpoint = f"https://api.github.com/users/{name}"
        res = requests.get(endpoint)
        return res.json()

    @classmethod
    def weather(cls):
        key = '61107cb5aeddc3fe473d540e1768ff09'
        lat = "34.3863074"
        lon = "-118.5441854"
        endpoint = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}"
        res = requests.get(endpoint)
        return res.json()