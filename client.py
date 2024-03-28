from db.models import SpamReason
from services.spam_link_service import SpamLinkService
from services.spam_user_service import SpamUserService
from utils.link_cleaner import clean_link


class SpamClient:
    def __init__(self, spam_link_service: SpamLinkService, spam_user_service: SpamUserService):
        self.spam_link_service = spam_link_service
        self.spam_user_service = spam_user_service

    async def create_spam_link(self, link: str, reason: str):
        """
        Добавляет ссылку в список спама после ее очистки.
        """
        cleaned_link = clean_link(link)
        await self.spam_link_service.create(cleaned_link, reason)

    async def is_spam_link(self, link: str) -> bool:
        """
        Проверяет, является ли ссылка спамом.
        """
        cleaned_link = clean_link(link)
        return await self.spam_link_service.is_spam(cleaned_link)

    async def create_spam_user(self, user_id: int, reason: SpamReason):
        """
        Добавляет пользователя в список спама.
        """
        await self.spam_user_service.create(user_id, reason)

    async def is_spam_user(self, user_id: int) -> bool:
        """
        Проверяет, помечен ли пользователь как спам.
        """
        return await self.spam_user_service.is_spam(user_id)
