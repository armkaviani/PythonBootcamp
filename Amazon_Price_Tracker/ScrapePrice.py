from bs4 import BeautifulSoup
import lxml
import requests


class ScrapePrice:
    def __init__(self):
        self.url = "https://www.amazon.de/Logitech-Gaming-Kopfh%C3%B6rer-Surround-Klangtreiber-Headphone/dp/B07MTXLFXV/ref=sr_1_4?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=28GXIN4VG8M5T&dib=eyJ2IjoiMSJ9.PTZ2aC8WbFMDKjv8QX5pEgjKhSjuraYR65WPzTyFUuA1PY3yoHEKrx6XerWmAdbbuynYl5HK3plH92e7nuCfJLK8xc-mv1tB5d7yA9RfqDDjON3v8tmFTq2fqCdDzFeBBzulrMXaTfkCiLOBKXJS55IwDBsk3cDP5h0_Lj5oiCCnmMyAcNeIBkHgxkvpmYDo3uJjcVv6KiJ64fVGd2YCPAfQ3IG1lXT7tM8eJ93_svs.RpCmA7p4uzBVRz2pSHyXF8QG1FE43r80hVv7r39EFbI&dib_tag=se&keywords=headset&qid=1748446561&sprefix=headset%2Caps%2C110&sr=8-4"
        self.headers = { "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
                        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
                }


    
    