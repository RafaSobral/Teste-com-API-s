import asyncio 
import time

async def outrafuncao():
    print(f"Funcao 0: {time.strftime('%X')}")
    await asyncio.sleep(1)
    print("Mensagem 0")

async def outrafuncao1():
    print(f"Funcao 1: {time.strftime('%X')}")
    await asyncio.sleep(1)
    print("Mensagem 1")

async def funcao():
    print(f"Iniciou: {time.strftime('%X')}")
    task = asyncio.create_task(outrafuncao())
    task1 = asyncio.create_task(outrafuncao1())
    await task
    await task1
    print(f"Terminou: {time.strftime('%X')}")

asyncio.run(funcao())