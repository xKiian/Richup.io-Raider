import websocket
import threading
import colorama
import random
import time
import os


def logo():
    os.system("cls && title Richup.io botter by xKian ^| Waiting for game code...")
    print(
        colorama.Fore.CYAN
        + "\n\n                                 ██████╗ ██╗ ██████╗██╗  ██╗██╗   ██╗██████╗ ██╗ ██████╗ \n                                 ██╔══██╗██║██╔════╝██║  ██║██║   ██║██╔══██╗██║██╔═══██╗\n                                 ██████╔╝██║██║     ███████║██║   ██║██████╔╝██║██║   ██║\n                                 ██╔══██╗██║██║     ██╔══██║██║   ██║██╔═══╝ ██║██║   ██║\n                                 ██║  ██║██║╚██████╗██║  ██║╚██████╔╝██║ ██╗ ██║╚██████╔╝\n                                 ╚═╝  ╚═╝╚═╝ ╚═════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝ ╚═╝ ╚═╝ ╚═════╝ \n                                                         by xKian                  \n    "
    )


success, failed = 0, 0


class spam:
    def __init__(self):
        self.ws = websocket.WebSocket()
        self.colors = ["#9A6E5E", "#73E85D"]  # you can add more colors

    def send(self, payload: str) -> None:
        self.ws.send(payload)

    def recieve(self) -> dict:
        data = self.ws.recv()
        return data if data else None

    def rand_number(self) -> str:
        return str(random.randint(1000, 9999))

    def join(self):
        global success, failed
        try:
            url = "wss://richup.io/socket.io/?EIO=4&transport=websocket"
            self.ws.connect(url, header=["Origin: https://richup.io"])
            self.recieve()
            self.send("40/api/game,")
            self.recieve()
            self.send('42/api/game,["enter-room",{"roomId":"%s"}]' % gamecode)
            self.recieve()
            self.send(
                '42/api/game,["join-game",{"roomId":"'
                + gamecode
                + '","name":"'
                + self.rand_number()
                + '","appearance":"'
                + random.choice(self.colors)
                + '"}]'
            )
            self.ws.close()
            success += 1
        except:
            failed += 1


def title():
    global success, failed
    while True:
        os.system(
            f"title Richup.io botter by xKian ^| Code: {gamecode} ^| Success: {str(success)} Failed: {str(failed)}"
        )
        print("[+] Success: " + str(success) + " Failed: " + str(failed), end="\r")
        time.sleep(0.5)


def main():
    global gamecode
    logo()
    gamecode = input("[?] Link/code: ").split("/")[-1]
    logo()
    threading.Thread(target=title).start()
    while True:
        threading.Thread(target=spam().join).start()


if __name__ == "__main__":
    main()
