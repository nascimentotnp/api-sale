from sqlalchemy import Column, Integer, String, Float, Boolean

from gateways.databases.gateway_database import Base


class Product(Base):
    __tablename__ = 'produto'

    id = Column(Integer, primary_key=True, autoincrement=False)
    title = Column(String(255), nullable=False)
    price = Column(Float, nullable=False)
    description = Column(String(255), nullable=False)
    category = Column(String(100), nullable=False)
    image = Column(String(255), nullable=False)
    rating_rate = Column(Float, nullable=False)
    rating_count = Column(Integer, nullable=False)
    active = Column(Boolean, default=True, nullable=False)

    def __init__(self, product_id, title, price, description, category, image, rating_rate, rating_count):
        self.id = product_id
        self.title = title
        self.price = price
        self.description = description
        self.category = category
        self.image = image
        self.rating_rate = rating_rate
        self.rating_count = rating_count
        self.active = True

    def serialize(self):
        return {
            'id': self.id,
            'título': self.title,
            'preço': self.price,
            'descrição': self.description,
            'categoria': self.category,
            'imagem': self.image,
            'avaliação': {
                'avaliar': self.rating_rate,
                'contagem': self.rating_count
            }
        }
