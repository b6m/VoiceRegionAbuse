import asyncio
import httpx
from colorama import Fore, init
import random

class VoiceRegionAbuse:
    

    def __init__(self):
        self.headers          =    {'Authorization': str(input('[?] Enter Your Token : '))}
        self.voice_id         =    int(input("[?] Enter A Voice ID : "))
        self.amount           =    int(input("[?] How Many Times Do You Want To Change The Region : "))
        self.group            =    f"https://discord.com/api/v9/channels/{self.voice_id}/call"
        self.voice_regions    =    ['brazil','hongkong','india','japan','rotterdam','russia','singapore','southafrica','sydney','us-central','us-east','us-south','us-west']


    async def VoiceRegionAbuse(self):
        try:
            for amount in range(self.amount):
                async with httpx.AsyncClient() as client:
                    region = random.choice(self.voice_regions)
                    r = await client.patch(self.group, headers=self.headers, json={"region": region})
                    if r.status_code in [200, 201, 202, 203, 204, 205, 206, 207, 208, 226]:
                        print(f"{Fore.LIGHTMAGENTA_EX}[{Fore.LIGHTGREEN_EX} ~ {Fore.LIGHTMAGENTA_EX}] {Fore.RESET} Changed To {region}")
                    elif r.status_code == 429:
                        print(f"{Fore.LIGHTMAGENTA_EX}[{Fore.LIGHTRED_EX} - {Fore.LIGHTMAGENTA_EX}] {Fore.RESET} Rate Limited")
                    elif r.status_code == 404:
                        print(f"{Fore.LIGHTMAGENTA_EX}[{Fore.LIGHTRED_EX} - {Fore.LIGHTMAGENTA_EX}] {Fore.RESET} Group or Call Not Found")
        except:
            print(f"{Fore.LIGHTMAGENTA_EX}[{Fore.LIGHTRED_EX}-{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Token Is Invalid")

if __name__ == "__main__":
    init()
    VoiceRegionAbuse = VoiceRegionAbuse()
    asyncio.run(VoiceRegionAbuse.VoiceRegionAbuse())
