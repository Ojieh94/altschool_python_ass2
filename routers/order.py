from fastapi import APIRouter, Depends, HTTPException
from schema.customer import Customer, customers

from schema.order import Order, OrderCreate, OrderStatus, orders
from services.order import order_service

order_router = APIRouter()

# list all order
# create an order 

@order_router.get('/', status_code=200)
def list_orders():
    response = order_service.order_parser(orders)
    return {'message': 'success', 'data': response}

@order_router.post('/', status_code=201)
def create_order(payload: OrderCreate = Depends(order_service.check_availability)):
    
    lis_customer = [customer.id for customer in customers]

    customer_id = payload.customer_id
    product_ids = payload.items

    if customer_id in lis_customer:
        # get current order id
        order_id = len(orders) + 1
        new_order = Order(
            id=order_id,
            customer_id=customer_id,
            items=product_ids,
        )
        orders.append(new_order)
        return {'message': 'Order created successfully', 'data': new_order}
    else:
        raise HTTPException(status_code=404, detail=f"Customer with ID {customer_id} not found")
    
@order_router.put('/{order_id}', status_code=200)
def checkout_order(order_id: int = Depends(order_service.check_existing_order)):
    for order in orders:
        if order.id == order_id:
            order.status = OrderStatus.checked.value
            return {'message': 'Checked order successfully', 'data': order}

    
    

