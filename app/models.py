import uuid
from sqlalchemy import String, Numeric, Integer, ForeignKey, DateTime, func , Index
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db import Base

class Category(Base):
    __tablename__ = "categories"

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4
    )
    name: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False
    )
    products: Mapped[list["Product"]] = relationship(back_populates="category")
class Product(Base):
    __tablename__ = "products"
    __table_args__ = (
        Index("idx_products_product_name", "product_name"),
    )

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4
    )

    product_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    price: Mapped[float] = mapped_column(
        Numeric(10, 2),
        nullable=False
    )

    quantity: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    category_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("categories.id"),
        nullable=False
    )

    created_at: Mapped[DateTime] = mapped_column(
        DateTime,
        server_default=func.now(),
        nullable=False
    )
    
    description: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    category: Mapped["Category"] = relationship(
        back_populates="products"
    )