from sqlalchemy import Column, Integer, String, Numeric, DateTime
from .database import Base

#Criando o modelo de vendas
class Sale(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, index=True)
    restaurant_id = Column(Integer)
    product_name = Column(String)
    quantity = Column(Integer)
    total = Column(Numeric)
    created_at = Column(DateTime)
