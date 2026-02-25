# app/models.py
import enum
from datetime import datetime, date
from sqlalchemy import String, Integer, Date, DateTime, Enum, ForeignKey, Text, Boolean, Numeric, Index
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db import Base

class InvoiceStatus(str, enum.Enum):
    pending = "pending"        # antes do vencimento
    due_today = "due_today"    # vence hoje
    overdue = "overdue"        # atrasada
    paid = "paid"
    canceled = "canceled"

class Channel(str, enum.Enum):
    whatsapp = "whatsapp"
    sms = "sms"
    email = "email"

class AttemptType(str, enum.Enum):
    reminder = "reminder"
    due = "due"
    overdue = "overdue"
    negotiation = "negotiation"
    confirmation = "confirmation"

class Customer(Base):
    __tablename__ = "customers"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    full_name: Mapped[str] = mapped_column(String(140))
    phone_e164: Mapped[str] = mapped_column(String(32), unique=True, index=True)  # +55...
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    invoices: Mapped[list["Invoice"]] = relationship(back_populates="customer")

class Invoice(Base):
    __tablename__ = "invoices"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    customer_id: Mapped[int] = mapped_column(ForeignKey("customers.id"), index=True)
    amount: Mapped[float] = mapped_column(Numeric(12, 2))
    due_date: Mapped[date] = mapped_column(Date, index=True)
    status: Mapped[InvoiceStatus] = mapped_column(Enum(InvoiceStatus), default=InvoiceStatus.pending, index=True)

    external_payment_id: Mapped[str | None] = mapped_column(String(80), nullable=True)
    pix_copy_paste: Mapped[str | None] = mapped_column(Text, nullable=True)
    payment_link: Mapped[str | None] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    customer: Mapped["Customer"] = relationship(back_populates="invoices")
    attempts: Mapped[list["ChargeAttempt"]] = relationship(back_populates="invoice")

class ChargeAttempt(Base):
    __tablename__ = "charge_attempts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    invoice_id: Mapped[int] = mapped_column(ForeignKey("invoices.id"), index=True)

    channel: Mapped[Channel] = mapped_column(Enum(Channel), default=Channel.whatsapp)
    attempt_type: Mapped[AttemptType] = mapped_column(Enum(AttemptType))
    message: Mapped[str] = mapped_column(Text)
    sent_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    delivery_status: Mapped[str] = mapped_column(String(50), default="sent")  # sent|delivered|failed

    invoice: Mapped["Invoice"] = relationship(back_populates="attempts")

Index("ix_attempts_invoice_type_sent", ChargeAttempt.invoice_id, ChargeAttempt.attempt_type, ChargeAttempt.sent_at)
