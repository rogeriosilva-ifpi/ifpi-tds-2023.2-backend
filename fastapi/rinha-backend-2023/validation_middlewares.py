from fastapi import Depends, HTTPException, Request, status
from starlette.middleware.base import (BaseHTTPMiddleware,
                                       RequestResponseEndpoint)
from starlette.requests import Request
from starlette.responses import Response

from person_repository import PersonRepository


class ValidateApelidoMiddleware(BaseHTTPMiddleware):

  async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
      
      if request.method != 'POST':
         return await call_next(request)

      data = await request.json()
      apelido = data['apelido']

      personRepo: PersonRepository = PersonRepository()
      person = personRepo.findBy(apelido=apelido)

      if person:
        return Response('Apelido Indisponível!', status_code=422)

      return await call_next(request)
