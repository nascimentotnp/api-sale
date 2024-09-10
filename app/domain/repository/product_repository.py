from domain.entity.entities import Product
from gateways.databases.connection import session


def create_products(product_id, title, price, description, category, image, rating_rate, rating_count):
    if read_products_by_id(product_id):
        print(f'Produto {product_id} já existe no banco.')
        return
    new_product = Product(
        id=id,
        title=title,
        price=price,
        description=description,
        category=category,
        image=image,
        rating_rate=rating_rate,
        rating_count=rating_count
    )
    session.add(new_product)
    session.commit()


def read_all_products():
    return session.query(Product).all()


def read_active_products():
    return session.query(Product).filter(Product.active).all()


def read_products_by_id(product_id):
    return session.query(Product).filter(Product.id == product_id).first()


def update_products(product_id, **kwargs):
    product = session.query(Product).get(product_id)
    for key, value in kwargs.items():
        setattr(product, key, value)
    session.commit()


def delete_products(product_id):
    product = session.query(Product).get(product_id)
    product.active = False
    session.commit()
