import json
from incc_crawler import crawler
from incc_crawler.notificators import TelegramNotificator


telegram = TelegramNotificator()


def lambda_handler(event, context):
    t1, t2 = crawler.build_results()
    telegram.send(t1, t2)

    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "message": "hello world",
            }
        ),
    }


if __name__ == "__main__":
    t1, t2 = crawler.build_results()
    telegram.send(t1, t2)
