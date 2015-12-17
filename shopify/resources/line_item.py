from ..base import ShopifyResource
from .product import Product


class LineItem(ShopifyResource):
    class Property(ShopifyResource):
        pass

    def product(self, **kwargs):
        return Product.find(self.product_id, **kwargs)
