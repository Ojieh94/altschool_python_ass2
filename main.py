from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware
from middleware import ecommerce_middleware

from routers.customer import customer_router
from routers.product import product_router
from routers.order import order_router
from logger import logger

app = FastAPI()
logger.info("starting app")

app.add_middleware(BaseHTTPMiddleware, dispatch=ecommerce_middleware)

app.include_router(customer_router, prefix='/customers', tags=['Customer'])
app.include_router(product_router, prefix='/products', tags=['Product'])
app.include_router(order_router, prefix='/orders', tags=['Order'])

users = [
    {
        'name': 'john',
        'age': 12,
        'phone': '0999900000'
    },
    {
        'name': 'james',
        'age': 12,
        'phone': '0999900000'
    },
    {
        'name': 'janet',
        'age': 12,
        'phone': '0999900000'
    }
]


@app.get('/welcome')
def index():
    return {'message': 'Welcome to our store'}

@app.get('/users')
def get_users():
    return {'message': 'success', 'data': users}

@app.post('/users')
def create_user(name, age, phone):
    user = {
        'name': name,
        'age': age,
        'phone': phone
    }
    users.append(user)
    return {'message': 'User created successfully', 'data': user}

@app.put('/users/{name}')
def update_user(name, age, phone):
    for user in users:
        if user.get('name') == name:
            user['age'] = age
            user['phone'] = phone
            break
    return {'message': 'User updated successfully', 'data': user}

# GET
# POST
# PUT
# DELETE