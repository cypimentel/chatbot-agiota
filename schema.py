# app/schemas.py
from datetime import date
from pydantic import BaseModel, Field

class CustomerCreate(BaseModel):
    full_name: str
    phone_e164: str

class CustomerOut(BaseModel):
    id: int
    full_name: str
    phone_e164: str
    is_active: bool
    class Config:
        from_attributes = True

class InvoiceCreate(BaseModel):
    customer_id: int
    amount: float = Field(gt=0)
    due_date: date

class InvoiceOut(BaseModel):
    id: int
    customer_id: int
    amount: float
    due_date: date
    status: str
    pix_copy_paste: str | None
    payment_link: str | None
    class Config:
        from_attributes = True

class IncomingMessage(BaseModel):
    phone_e164: str
    text: str

class PaymentWebhook(BaseModel):
    external_payment_id: str
    status: str  # paid|failed|canceled
