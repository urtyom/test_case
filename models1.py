import sqlalchemy as sa
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Product(Base):
    __tablename__ = "products"

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(length=255), nullable=False)
    created_at = sa.Column(sa.DateTime, nullable=False)
    price = sa.Column(sa.Numeric(10, 2), nullable=False)
    quantity = sa.Column(sa.Integer, nullable=False)

    def __str__(self):
        return f'ID - {self.id}, Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}, Created At: {self.created_at}'


def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
