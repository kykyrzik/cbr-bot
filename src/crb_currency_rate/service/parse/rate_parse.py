from decimal import Decimal
from typing import cast, Sequence
from xml.etree.ElementTree import Element, fromstring

from aiohttp import ClientSession

from src.crb_currency_rate.dto.currency_rate import CurrencyRateDTO


async def get_currency_rates(session: ClientSession) -> str:
    async with session.get("https://cbr.ru/scripts/XML_daily.asp") as request:
        data = await request.text()
        return data


def currency_rate_data_mapper(data: str) -> Sequence[CurrencyRateDTO]:
    xml_data = fromstring(data)
    raw_data = []
    for value in xml_data:
        raw_data.append(
            CurrencyRateDTO(
                code=cast(str, cast(Element, value.find('CharCode')).text),
                value=Decimal(cast(str, cast(Element, value.find('VunitRate')).text).replace(',', '.')),
            )
        )
    return raw_data
