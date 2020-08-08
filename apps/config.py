class Config():
    pass


class Develop(Config):
    DEBUG = True


class Product(Config):
    DEBUG = False


config = {
    "develop": Develop,
    "product": Product
}