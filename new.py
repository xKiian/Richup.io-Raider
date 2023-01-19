import websocket, threading, random, os

os.system("cls & title richup.io botter by xKian ^| Waiting for game code...")
gamecode = input("Link/code: ")
try:gamecode = gamecode.split("/")[-1]
except:pass
joined = 0
class spam:
    def __init__(self):
        self.ws     = websocket.WebSocket()
        self.colors = ["#7F5ADA", "#FFC73F", "#9A6E5E"]

    def send(self, payload: str) -> None:
        self.ws.send(payload)
        self.recieve()

    def recieve(self) -> dict:
        data = self.ws.recv()
        return data if data else None
    
    def getrandomnumber(self) -> str:
        return str(random.randint(1000,9999))

    def join(self):
        try:
            global joined
            url = 'wss://richup.io/socket.io/?EIO=4&transport=websocket'

            self.ws.connect(url, header=['Origin: https://richup.io'])
            self.send("40/api/game,")
            self.send('42/api/game,["enter-room",{"roomId":"'+gamecode+'"}]')

            num = self.getrandomnumber()
            self.send('42/api/game,["join-game",{"roomId":"'+gamecode+'","name":"xKian'+num+'","appearance":"'+random.choice(self.colors)+'"}]')
            self.ws.close()
            print("[+] Joined game with", num)
            joined += 1
            os.system("title richup.io botter by xKian ^| Joined: "+str(joined))
        except:
            print("[-] Failed to join game")

while True:
    spam().join()