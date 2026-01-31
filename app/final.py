from sqlalchemy import select, update
from app.db import SessionLocal
from app.models import Product, Category
def fetch_all_products():
    with SessionLocal() as session:
        stmt = select(Product)
        products = session.execute(stmt).scalars().all()
        return products
def bulk_price_update(category_name: str):
    with SessionLocal() as session:
        try:
            with session.begin():  # TRANSACTION
                stmt = (
                    update(Product)
                    .where(
                        Product.category_id == (
                            select(Category.id)
                            .where(Category.name == category_name)
                            .scalar_subquery()
                        )
                    )
                    .values(price=Product.price * 1.10)
                )
                session.execute(stmt)

            print(f"Prices updated by 10% for category: {category_name}")
        except Exception as e:
            print("Update failed, transaction rolled back")
            print(e)

if __name__ == "__main__":
    products = fetch_all_products()
    print(" Current Products:")
    for p in products:
        print(p.product_name, p.price)

    bulk_price_update("Electronics")

