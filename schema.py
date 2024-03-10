from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey, Numeric, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


engine = create_engine('sqlite:///example.db')
Base = declarative_base()


class Product_Category(Base):
    __tablename__ = 'product_category'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    description = Column(Text)
    created_at = Column(TIMESTAMP)
    modified_at = Column(TIMESTAMP)
    deleted_at = Column(TIMESTAMP)


class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    description = Column(Text)
    price = Column(Numeric(10, 2))
    product_category_id = Column(Integer, ForeignKey('product_category.id'))
    created_at = Column(TIMESTAMP)
    modified_at = Column(TIMESTAMP)
    deleted_at = Column(TIMESTAMP)

    category = relationship("Product_Category")


Base.metadata.create_all(engine)
