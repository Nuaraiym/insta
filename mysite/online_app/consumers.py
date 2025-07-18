import json
from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):                                          # постмен кнопка connect связка
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]  # путь  в постмен
        self.room_group_name = f"chat_{self.room_name}"

        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name) # путь,баары туура келсе чыгарат

        await self.accept()

    async def disconnect(self, close_code):                    # дал келбесе чыгарбайт
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):                # получить сообщение
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        # Send message to room group                    # отправить сообщение
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat.message", "message": message}
        )

    # Receive message from room group
    async def chat_message(self, event):                 # получить сообщение
        message = event["message"]

        # Send message to WebSocket                      # отправить сообщение
        await self.send(text_data=json.dumps({"message": message}))