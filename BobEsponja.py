from time import sleep 
import asyncio

class AsyncSpongeBob:
    async def cook_bread(self):
     await asyncio.sleep(3)

    async def cook_hamburguer(self):
     await asyncio.sleep(10)

    async def mount_sandwich(self):
     await asyncio.sleep(3)

    async def make_milkshake(self):
     await asyncio.sleep(5)

    async def cook(self):
      await asyncio.gather(
        self.cook_bread(),
        self.cook_hamburguer(),
        self.make_milkshake()
      )
      await self.mount_sandwich()

async_spongebob = AsyncSpongeBob()
asyncio.run(async_spongebob.cook())
       



