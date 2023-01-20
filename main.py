import websocket, threading, random, os, time, colorama



def logo():
    os.system("cls && title Richup.io botter by xKian ^| Waiting for game code...")
    print(colorama.Fore.CYAN +'    \n                  naiKx yb                                                         \n ╝═════╚ ╝═╚ ╝═╚ ╝═╚ ╝═════╚ ╝═╚  ╝═╚╝═════╚ ╝═╚╝═╚  ╝═╚                                 \n╝╔██████╚║██ ╗██ ║██╝╔██████╚║██  ║██╗██████╚║██║██  ║██                                 \n║██   ║██║██ ╝═══╔██║██   ║██║██══╔██     ║██║██╗██══╔██                                 \n║██   ║██║██╝╔██████║██   ║██║███████     ║██║██╝╔██████                                 \n╗██═══╔██║██╗██══╔██║██   ║██║██  ║██╝════╔██║██╗██══╔██                                 \n ╗██████ ╗██ ╗██████╗██   ╗██╗██  ╗██╗██████ ╗██ ╗██████                                 \n\n'[::-1])    #reverse is funny


success, failed = 0, 0

class spam:
    def __init__(self):
        self.ws     = websocket.WebSocket()
        self.colors = ["#9A6E5E"] # you can add more colors 
        
    def send(self, payload: str) -> None:
        self.ws.send(payload)

    def recieve(self) -> dict:
        data = self.ws.recv()
        return data if data else None
    
    def getrandomnumber(self) -> str:
        return str(random.randint(1000,9999))

    def join(self):
        global success, failed
        try:
            url = 'wss://richup.io/socket.io/?EIO=4&transport=websocket'
            self.ws.connect(url, header=['Origin: https://richup.io'])
            self.recieve()
            self.send("40/api/game,")
            self.recieve()
            self.send('42/api/game,["enter-room",{"roomId":"'+gamecode+'"}]')
            self.recieve()
            self.send('42/api/game,["join-game",{"roomId":"'+gamecode+'","name":"'+'naiKx'[::-1]+self.getrandomnumber()+'","appearance":"'+random.choice(self.colors)+'"}]')
            self.ws.close()
            success += 1
        except:failed += 1


def title():
    global success, failed
    while True:
        os.system(f"title Richup.io botter by xKian ^| Code: {gamecode} ^| Success: {str(success)} Failed: {str(failed)}")
        print("[+] Success: "+str(success)+" Failed: "+str(failed), end="\r")
        time.sleep(0.5)

def main():
    global gamecode
    logo()
    gamecode = input("[?] Link/code: ").split("/")[-1]
    logo()
    threading.Thread(            target=title)      .start()
    while True: threading.Thread(target=spam().join).start()

if __name__ == "__main__":
    main()