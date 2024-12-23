import asyncio
import websockets

async def test():
    uri = "ws://localhost:8000/chat/ws/chat"
    async with websockets.connect(uri) as websocket:
        print("Connected to WebSocket.")
        await websocket.send("Hello, this is a test message!")
        response = await websocket.recv()
        print(f"Received: {response}")

asyncio.run(test())
