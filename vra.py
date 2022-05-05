# voice.py
# author: b6m
# date: 2022-05-05
import asyncio
import httpx
from datetime import datetime
from colorama import Fore, init
import random

headers          =    {'Authorization': str(input('[?] Enter Your Token : '))}
voice_id         =    int(input("[?] Enter A Voice ID : "))
amount           =    int(input("[?] How Many Times Do You Want To Change The Region : "))

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
                        print(f"{Fore.LIGHTMAGENTA_EX}[{Fore.LIGHTGREEN_EX} ~ @ {_time_} {Fore.LIGHTMAGENTA_EX}] {Fore.RESET} Changed To {region}")
                    elif r.status_code == 429:
                        _time_ = datetime.now().strftime("%H:%M:%S")
                        print(f"{Fore.LIGHTMAGENTA_EX}[{Fore.LIGHTRED_EX} - @ {_time_} {Fore.LIGHTMAGENTA_EX}] {Fore.RESET} Rate Limited")
                    elif r.status_code == 404:
                        _time_ = datetime.now().strftime("%H:%M:%S")
                        print(f"{Fore.LIGHTMAGENTA_EX}[{Fore.LIGHTRED_EX} - @ {_time_} {Fore.LIGHTMAGENTA_EX}] {Fore.RESET} Group Call Not Found")
        except Exception as e:
            print(f"{e}")
            print(f"{Fore.LIGHTMAGENTA_EX}[{Fore.LIGHTRED_EX}-{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Token Is Invalid")

async def __run__():
    tasks = []
    for i in range(56):
        tasks.append(VoiceRegionAbuse().RegionAbuse())
    await asyncio.gather(*tasks)
    
        
if __name__ == "__main__":
    init()
    asyncio.run(__run__())
