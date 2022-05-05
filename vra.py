# vra.py
# author: b6m
# date: 2022-05-05
import asyncio
import httpx
from datetime import datetime
from pystyle import Colors, Colorate
import random

headers          =    {'Authorization': str(input(Colorate.Horizontal(Colors.blue_to_purple,'[?] Enter Your Token : ')))}
voice_id         =    int(input(Colorate.Horizontal(Colors.blue_to_purple,"[?] Enter A Voice ID : ")))
amount           =    int(input(Colorate.Horizontal(Colors.blue_to_purple,"[?] How Many Times Do You Want To Change The Region : ")))



class VoiceRegionAbuse:
    
    def __init__(self):
        self.group            =    f"https://discord.com/api/v9/channels/{voice_id}/call"
        self.voice_regions    =    ['brazil','hongkong','india','japan','rotterdam','russia','singapore','southafrica','sydney','us-central','us-east','us-south','us-west']


    async def RegionAbuse(self):
        try:
            for _ in range(amount):
                async with httpx.AsyncClient() as client:
                    region = random.choice(self.voice_regions)
                    r = await client.patch(self.group, headers=headers, json={"region": region})
                    if r.status_code in [200, 201, 202, 203, 204, 205, 206, 207, 208, 226]:
                        _time_ = datetime.now().strftime("%H:%M:%S")
                        print(Colorate.Horizontal(Colors.white_to_blue, f"[ - @ {_time_} ] Sucessfully Changed To {region}", 1))
                    elif r.status_code == 429:
                        _time_ = datetime.now().strftime("%H:%M:%S")
                        print(Colorate.Horizontal(Colors.white_to_red, f"[ - @ {_time_} ] Rate Limited", 1))
                    elif r.status_code == 404:
                        _time_ = datetime.now().strftime("%H:%M:%S")
                        print(Colorate.Horizontal(Colors.white_to_red, f"[ - @ {_time_} ] Voice Call Does Not Exist", 1))


        except Exception as e:
            _time_ = datetime.now().strftime("%H:%M:%S")
            print(Colorate.Horizontal(Colors.white_to_red, f"[ - @ {_time_} ] {e}", 1))

async def __run__():
    tasks = []
    for i in range(56):
        tasks.append(VoiceRegionAbuse().RegionAbuse())
    await asyncio.gather(*tasks)
    
        
if __name__ == "__main__":
    asyncio.run(__run__())
