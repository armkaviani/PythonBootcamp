from News_Sender import GetNews
from Stock_Price import StockPrice


# Twilio credentials (replace with your real values)
TWILIO_SID = "your_twilio_sid"
TWILIO_AUTH_TOKEN = "your_twilio_auth_token"
VIRTUAL_TWILIO_NUMBER = "your_twilio_phone_number"
VERIFIED_NUMBER = "your_verified_phone_number"


def main():

    stock = StockPrice()
    should_get_news, diff_percent, up_down = stock.check_price_difference()

    if should_get_news:
        news = GetNews(
            twilio_sid=TWILIO_SID,
            twilio_auth=TWILIO_AUTH_TOKEN,
            from_number=VIRTUAL_TWILIO_NUMBER,
            to_number=VERIFIED_NUMBER
        )
        news.send_articles(stock_symbol=StockPrice.STOCK_NAME, up_down=up_down, diff_percent=diff_percent)
    else:
        print("Stock price movement not significant enough. No news sent.")


if __name__ == "__main__":
    main()