from incc_crawler import crawler
from incc_crawler.notificators import TelegramNotificator


telegram = TelegramNotificator()

if __name__ == "__main__":
    t1, t2 = crawler.build_results()
    telegram.send(t1, t2)
