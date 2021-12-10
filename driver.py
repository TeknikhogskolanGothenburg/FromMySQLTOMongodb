from mysql_db.db import session
from mysql_db.models import Product


def main():
    products = session.query(Product).all()
    for product in products:
        print(product.productName)


if __name__ == '__main__':
    main()
