from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import NoResultFound

from db.models import SpamLink


class SpamLinkRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, link: str, reason: str) -> SpamLink:
        new_spam_link = SpamLink(link=link, reason=reason)
        self.session.add(new_spam_link)
        await self.session.commit()
        return new_spam_link

    async def is_spam_link(self, link: str) -> bool:
        try:
            query = select(SpamLink).where(SpamLink.link == link)
            result = await self.session.execute(query)
            result.scalar_one()
            return True
        except NoResultFound:
            return False
