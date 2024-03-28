from db.repositories.spam_link_repository import SpamLinkRepository


class SpamLinkService:

    def __init__(self, link_repo: SpamLinkRepository):
        self.link_repo = link_repo

    async def create(self, link: str, reason: str):
        if await self.link_repo.is_spam_link(link):
            raise ValueError(f"Ссылка {link} уже помечена как спам.")
        await self.link_repo.create(link, reason)

    async def is_spam(self, link: str) -> bool:
        return await self.link_repo.is_spam_link(link)
