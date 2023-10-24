from fastapi import FastAPI, Request

from animais_controller import router as animals_router
from carros_controller import prefix as cars_prefix
from carros_controller import router as cars_router
from middlewares.log_middleware import LogMiddleware

app = FastAPI()


app.include_router(cars_router, prefix=cars_prefix)
app.include_router(animals_router)


# Opcao FASTAPI
@app.middleware('http')
def log_middleware(request: Request, next_call):
    print('LOG Middleware in Action!')
    return next_call(request)


# Opcao Starlette
app.add_middleware(LogMiddleware, **{'path': '/cars/'})


@app.get('/hello')
def hello():
    return {"mensagem": "Olá seja bem-vindo!"}
