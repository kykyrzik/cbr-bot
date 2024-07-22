from typing import Optional, Mapping, Any

import aiohttp
from aiohttp import BasicAuth


class ClientSessionManager:
    def __init__(
            self,
            headers: Optional[Mapping[str, Any]] = None,
            auth: Optional[BasicAuth] = None
    ) -> None:
        self.headers = headers
        self.auth = auth

    async def __aenter__(self) -> aiohttp.ClientSession:
        self.session = aiohttp.ClientSession(headers=self.headers, auth=self.auth)
        return self.session

    async def __aexit__(self, exc_type, exc, tb) -> None:
        await self.session.close()
