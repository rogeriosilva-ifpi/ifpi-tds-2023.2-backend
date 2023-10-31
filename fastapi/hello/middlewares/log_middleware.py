

import typing
from os import path

from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware, DispatchFunction
from starlette.types import ASGIApp


class LogMiddleware(BaseHTTPMiddleware):

    def __init__(self, app: ASGIApp, path: str | None = None) -> None:
        super().__init__(app)
        self.path = path

    async def dispatch(self, request: Request, call_next) -> Response:

        print('PATH', request.url.path)
        if self.path and request.url.path == path:
            print('LOG Class Middleware in Action')

        return await call_next(request)


def log_middleware(request: Request, next_call):
    print('LOG Middleware in Action!')
    return next_call()
