from fastapi import APIRouter, HTTPException

from schema.product import Product, ProductCreate, products

product_router = APIRouter()

# create product
# list all products

@product_router.post('/', status_code=201)
def create_product(payload: ProductCreate):
    # get the product id
    product_id = len(products) + 1
    new_product = Product(
        id=product_id,
        name=payload.name,
        price=payload.price,
        quantity_available=payload.quantity_available
    )
    products[product_id] = new_product
    return {'message': 'Product created successfully', 'data': new_product}

@product_router.get('/', status_code=200)
def list_products():
    return {'message': 'success', 'data': products}

@product_router.put('/{product_id}', status_code=200)
def update_product(product_id: int, upd_product: ProductCreate):
    product = products.get(product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    if product.name is not None:
        product.name = upd_product.name
    if product.price is not None:
        product.price = upd_product.price
    if product.quantity_available is not None:
        product.quantity_available = upd_product.quantity_available

    
    return {"message": "Product updated successfully", "data": upd_product}

