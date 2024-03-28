from db.models import SpamReason
from db.repositories.spam_user_repository import SpamUserRepository


class SpamUserService:

    def __init__(self, user_repo: SpamUserRepository):
        self.user_repo = user_repo

    async def create(self, user_id: int, reason: SpamReason):
        if await self.user_repo.is_spam_user(user_id):
            raise ValueError(f"Пользователь с идентификатором {user_id} уже помечен как спам")
        await self.user_repo.create(user_id, reason)

    async def is_spam(self, user_id: int) -> bool:
        return await self.user_repo.is_spam_user(user_id)
