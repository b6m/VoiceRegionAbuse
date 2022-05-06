# vra.py
# author: b6m
# date: 2022-05-05
import httpx
import asyncio
import random
import logging

logging.basicConfig(level=logging.INFO,
                    format='\u001b[36;1m[\u001b[0m%(asctime)s\u001b[36;1m]\u001b[0m %(message)s\u001b[0m',
                    datefmt='%H:%M:%S'
                    )

headers          =    {'Authorization': str(input('\u001b[36;1m[\u001b[0m?\u001b[36;1m] \u001b[0m Enter Your Token   • '))}
voice_id         =    int(input('\u001b[36;1m[\u001b[0m?\u001b[36;1m] \u001b[0m Voice ID   •  '))

class VoiceRegionAbuse:
    
    def __init__(self):
        self.group            =    f"https://discord.com/api/v9/channels/{voice_id}/call"
        self.voice_regions    =    ['brazil','hongkong','india','japan','rotterdam','russia','singapore','southafrica','sydney','us-central','us-east','us-south','us-west']

    async def RegionAbuse(self): 
        while True:
            try:

                async with httpx.AsyncClient() as client:
                    region = random.choice(self.voice_regions)
                    r = await client.patch(self.group, headers=headers, json={"region": region})
                    
                    if r.status_code in [200, 201, 202, 203, 204, 205, 206, 207, 208, 226]:
                        logging.info(f'   Successfully Changed Voice Region • {region}')
                    
                    elif r.status_code == 429:
                        logging.warning(f"   Too Many Requests")
                        
                    elif r.status_code == 404:
                        logging.error(f"   Voice Channel Not Found")
            except Exception as e:
                logging.critical(f"   {e}")


async def __run__():
    tasks = []
    for i in range(56):
        tasks.append(VoiceRegionAbuse().RegionAbuse())
    await asyncio.gather(*tasks)
    
if __name__ == "__main__":
    asyncio.run(__run__())