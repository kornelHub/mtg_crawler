import requests

def main():
    base_url = 'https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid={}&type=card'
    for x in range(1, 296):
        file = open(f"./img/{x}.png", 'wb')
        file.write(requests.get(base_url.format(x)).content)
        file.close()

if __name__ == '__main__':
    main()