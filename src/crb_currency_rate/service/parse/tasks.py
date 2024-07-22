from typing import Sequence, Annotated

from fast_depends import Depends, inject


from src.crb_currency_rate.common.marker.redis import RedisMarker
from src.crb_currency_rate.dto.currency_rate import CurrencyRateDTO
from src.crb_currency_rate.service.parse.rate_parse import get_currency_rates, currency_rate_data_mapper
from src.crb_currency_rate.service.parse.session import ClientSessionManager
from src.crb_currency_rate.service.redis import RedisManager


@inject
async def task_currency_rate(manager: Annotated[RedisManager, Depends(RedisMarker)]) -> None:
    session_manager = ClientSessionManager()
    async with session_manager as session:
        data: str = await get_currency_rates(session)
        result: Sequence[CurrencyRateDTO] = currency_rate_data_mapper(data)
        for i in result:
            await manager.set(i.code, i.value)
