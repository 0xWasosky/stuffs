import requests
import threading
import colorama
import time
import argparse


args = argparse.ArgumentParser()
args.add_argument("--username", type=str, required=True)
args.add_argument("--question", type=str, required=True)
args.add_argument("--request-number", "-n", type=int, default=100)
args.add_argument("--sleep", type=int, default=1)
args.add_argument("--thread", type=int, default=1)
parse = args.parse_args()


green = colorama.Fore.GREEN
yellow = colorama.Fore.YELLOW
red = colorama.Fore.RED

urlApi = "https://ngl.link/api/submit"
payload = {
    "username": parse.username,
    "question": parse.question,
    "deviceId": "",
    "gameSlug": "",
    "referrer": "",
}

headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "it-IT,it;q=0.8,en-US;q=0.5,en;q=0.3",
    "Connection": "keep-alive",
    "Content-Length": str(len(payload)),
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Host": "ngl.link",
    "Origin": "https://ngl.link",
    "Referer": f"https://ngl.link/{parse.username}",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origi",
    "TE": "trailers",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0",
    "X-Requested-With": "XMLHttpRequest"
}


def NglSpammer(num: int, timeout: int):
    sent = 0

    while sent < num:
        response = requests.post(urlApi, headers=headers, data=payload)

        if response.status_code == 404:
            print(f"{yellow} [ {parse.username} ] User not found ")
            break

        elif response.status_code == 200:
            print(
                f"{yellow} [ {parse.username} ] -> {parse.question}  {green} sent : {sent}")

        else:
            print(
                f"{red} [ {parse.username} ] -> {parse.question}  message not sent : {sent}")

        time.sleep(timeout)

        sent += 1


if __name__ == "__main__":
    for _ in range(parse.thread):
        thread = threading.Thread(target=NglSpammer, args=(
            parse.request_number, parse.sleep,))
        thread.start()
