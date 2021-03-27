import requests
from incc_crawler.settings import settings


class TelegramNotificator:
    def _build_url(self, message) -> str:
        url = (
            f"https://api.telegram.org/bot{settings.BOT_TOKEN}"
            f"/sendMessage?chat_id={settings.CHAT_ID}"
            f"&text={message}"
            f"&parse_mode={settings.CHAT_PARSE_MODE}"
        )
        return url

    def send(self) -> bool:
        message = "hello from python"
        url = self._build_url(message)

        response = requests.get(url)
        response.raise_for_status()
        return True
