import asyncio, websockets, time, traceback

async def w(id):
    try:
        print(f"[Worker {id}] Tentando conectar...")
        async with websockets.connect("ws://5.255.97.147:8765/script", max_queue=None) as ws:
            print(f"[Worker {id}] Conectado com sucesso")
            for i in range(2000):
                try:
                    start = time.perf_counter()
                    await ws.send("fsociety")
                    print(f"[Worker {id}] Mensagem {i+1} enviada")

                    try:
                        resp = await asyncio.wait_for(ws.recv(), timeout=1)
                        latency = (time.perf_counter() - start)*1000
                        print(f"[Worker {id}] Mensagem {i+1} recebida: {resp} (latência: {latency:.2f} ms)")
                    except asyncio.TimeoutError:
                        print(f"[Worker {id}] Mensagem {i+1} timeout: sem resposta")
                except Exception as e:
                    print(f"[Worker {id}] Erro ao enviar/receber mensagem {i+1}: {e}")
    except Exception as e:
        print(f"[Worker {id}] Erro na conexão: {e}")
        traceback.print_exc()

asyncio.run(asyncio.gather(*[w(i) for i in range(50)]))
