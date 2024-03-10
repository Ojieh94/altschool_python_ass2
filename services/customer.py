from fastapi import HTTPException
from logger import logger

from schema.customer import CustomerCreate, customers


class CustomerService:

    
    @staticmethod
    def check_existing_customer(payload: CustomerCreate):
        for customer in customers:
            if customer.username == payload.username:
                logger.warning("Username already exists")
                raise HTTPException(
                    status_code=409, detail="Username already taken. Please try another username")
        return payload
        
            


customer_service = CustomerService()