from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import NoResultFound

from db.models import SpamUser, SpamReason


class SpamUserRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, user_id: int, reason: SpamReason) -> SpamUser:
        new_spam_user = SpamUser(user_id=user_id, reason=reason)
        self.session.add(new_spam_user)
        await self.session.commit()
        return new_spam_user

    async def is_spam_user(self, user_id: int) -> bool:
        try:
            query = select(SpamUser).where(SpamUser.user_id == user_id)
            result = await self.session.execute(query)
            result.scalar_one()
            return True
        except NoResultFound:
            return False
