import asyncio, websockets

async def w(id):
    async with websockets.connect("ws://5.255.97.147:8765/script", max_queue=None) as ws:
        for _ in range(2000):
            await ws.send("fsociety")

asyncio.run(asyncio.gather(*[w(i) for i in range(50)]))
