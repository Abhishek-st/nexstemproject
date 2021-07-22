from channels.generic.websocket import AsyncWebsocketConsumer
import json
from djangoHiring.model import predictOutcome

class DashConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        self.groupname='dashboard'
        await self.channel_layer.group_add(
            self.groupname,
            self.channel_name,
        )

        await self.accept()

    async def disconnect(self):

        await self.channel_layer.group_discard(
            self.groupname,
            self.channel_name
        )
    

    async def receive(self, text_data):
        datapoint = json.loads(text_data)
        val =datapoint['value']
        print(val)
        await self.channel_layer.group_send(
            self.groupname,
            {
                'type':'processing',
                'value':val
            }
        )

        print ('>>>>',text_data)

    async def processing(self,event):
        valOther=event['value']
        await self.send(text_data=json.dumps({'value':valOther}))


class ModelPredictConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        self.groupname='predictDashboard'
        self.data = []
        await self.channel_layer.group_add(
            self.groupname,
            self.channel_name,
        )

        await self.accept()

    async def disconnect(self):

        await self.channel_layer.group_discard(
            self.groupname,
            self.channel_name
        )
    

    async def receive(self, text_data):
        datapoint = json.loads(text_data)
        val =datapoint['value']
        await self.channel_layer.group_send(
            self.groupname,
            {
                'type':'processing',
                'value':val
            }
        )

    async def processing(self,event):
        valOther=event['value']
        self.data.append(valOther)
        if(len(self.data)==200):
            print("###########################################################################################\n")
            pred = predictOutcome(self.data)
            print(pred)
            await self.send(text_data=json.dumps({'value':str(pred)}))
            self.data.clear()
            print("###########################################################################################\n")

            
        