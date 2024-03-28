import datetime

from sqlalchemy import Enum
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from sqlalchemy import String, func, TIMESTAMP, BIGINT
import enum
from typing import Annotated

bigint = Annotated[int, int]
str32 = Annotated[str, 32]
str64 = Annotated[str, 64]
str255 = Annotated[str, 255]
boolFalse = Annotated[bool, mapped_column(server_default="false")]
created_at = Annotated[datetime.datetime, mapped_column(
    server_default=func.current_timestamp()
)]
updated_at = Annotated[datetime.datetime, mapped_column(
    server_default=func.current_timestamp(),
    onupdate=func.current_timestamp()
)]


class Base(DeclarativeBase):
    type_annotation_map = {
        bigint: BIGINT,
        str32: String(32),
        str64: String(64),
        str255: String(255),
        datetime.datetime: TIMESTAMP(timezone=False),
    }
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]


class SpamReason(enum.Enum):
    TWENTY_DUPLICATES_A_DAY = "20 дубликатов за день"
    SEVEN_DAYS_CONSECUTIVE_REQUESTS = "7 дней заявок подряд"
    ADVERTISING_ACCOUNT = "рекламный аккаунт"


class SpamUser(Base):
    __tablename__ = 'spam_users'

    user_id: Mapped[bigint] = mapped_column(primary_key=True)
    reason: Mapped[Enum(SpamReason)] = mapped_column(Enum(SpamReason))


class SpamLink(Base):
    __tablename__ = 'spam_link'

    link: Mapped[str64] = mapped_column(primary_key=True)
    reason: Mapped[str64] = mapped_column()
