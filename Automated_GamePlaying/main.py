from Game_Bot import CookieClickerBot
import time

def main():
    bot = CookieClickerBot()

    while True:
        bot.click_cookie()

        if time.time() > bot.timeout:
            item_prices = bot.get_item_prices()
            affordable = bot.get_affordable_upgrades(item_prices)
            bot.purchase_upgrade(affordable)
            bot.timeout = time.time() + 5


if __name__ == "__main__":
    main()
 



