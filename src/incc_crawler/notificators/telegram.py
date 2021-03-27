import requests
from incc_crawler.settings import settings
from incc_crawler.notificators.factories import MessageFactory


class TelegramNotificator:
    def __init__(self):
        self.message_factory = MessageFactory()

    def _build_url(self, message) -> str:
        print(message)
        url = (
            f"https://api.telegram.org/bot{settings.BOT_TOKEN}"
            f"/sendMessage?chat_id={settings.CHAT_ID}"
            f"&text={message}"
            f"&parse_mode={settings.CHAT_PARSE_MODE}"
        )
        return url

    def send(self, overview, total) -> bool:
        message = self.message_factory.build_message(overview, total)
        url = self._build_url(message)

        response = requests.get(url)

        print("=" * 20)
        print(response)
        print(response.text)
        print("=" * 20)

        response.raise_for_status()
        return True
