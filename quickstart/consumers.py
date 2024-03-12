from channels.generic.websocket import WebsocketConsumer
import json
from asgiref.sync import async_to_sync

class WSConsumer(WebsocketConsumer):
    def connect(self):
        self.group_name = "ca_group"  # Nom du groupe
        async_to_sync(self.channel_layer.group_add)(self.group_name, self.channel_name)
        self.accept()
        message = {'type': 'confirmation', 'content': 'Connexion établie avec succès!'}
        self.send(text_data=json.dumps(message))
        
    def disconnect(self, close_code):
        print("Disconnected", close_code)
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        self.send(text_data=json.dumps({
            'message': message
        }))
    
    def send_message(self, event):
        message = event
        print("Message sent", message)
        self.send(text_data=json.dumps({
            'message': message
        }))
