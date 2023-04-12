import  requests
import  re
import time
import  json
import  sys


print("  ____  __ __  ______   ___       ______    ___  _      _     ")
print(" /    ||  |  ||      | /   \     |      |  /  _]| |    | |    ")
print("|  o  ||  |  ||      ||     |    |      | /  [_ | |    | |    ")
print("|     ||  |  ||_|  |_||  O  |    |_|  |_||    _]| |___ | |___ ")
print("|  _  ||  :  |  |  |  |     |      |  |  |   [_ |     ||     |")
print("|  |  ||     |  |  |  |     |      |  |  |     ||     ||     |")
print("|__|__| \__,_|  |__|   \___/       |__|  |_____||_____||_____|")

print("by salamcyb")
print("insta:salam_cyb")







def number(username):
    headers1 = {
        'Host': 'tellonym.me',
        # 'Cookie': '_ga=GA1.2.1537484107.1681050840; _gid=GA1.2.1009281128.1681050840',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Te': 'trailers'
    }

    response = requests.get(f'https://tellonym.me/{username}', headers=headers1)
    pattern = r'/\d+_'
    matches = re.findall(pattern, response.text)
    if username not in response.text:
        print("Username not found")
        sys.exit(0)



    for match in matches:
        number = match[1:-1]
        return  number
        break

url = "https://api.tellonym.me/tells/new"
x=0
id=number(input("please enter username:"))
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0",
    "Accept": "application/json",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate",
    "Referer": "https://tellonym.me/",
    "Tellonym-Client": "web:3.58.4",
    "Content-Type": "application/json;charset=utf-8",
    "Origin": "https://tellonym.me",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "Te": "trailers"
}


file_name = "ass.txt"


with open(file_name, "r",encoding='utf-8') as file:
    for line in file:
        tell_value = line.strip()
        # Data payload
        data = {
            "isInstagramInAppBrowser": False,
            "isSnapchatInAppBrowser": False,
            "isSenderRevealed": False,
            "tell": tell_value,
            "userId": id,
            "limit": 25
        }
        response = requests.post(url, headers=headers, data=json.dumps(data))
        x=x+1
        print(x,line)
        time.sleep(5)
