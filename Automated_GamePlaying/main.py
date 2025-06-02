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
            

        if time.time() > bot.five_min:
            cps = bot.driver.find_element(By.ID, "cps").text
            print(f"Cookies per second: {cps}")
            break

if __name__ == "__main__":
    main()
 



