from sp_api.base import Marketplaces
from sp_api.api import CatalogItems, Products, ListingsItems
from sp_api.util import throttle_retry


class AmazonCatalogs:

    def __init__(self, credentials, refresh_token, seller_id, marketplace=Marketplaces.US):
        self.listing_api = ListingsItems(marketplace=marketplace, refresh_token=refresh_token, credentials=credentials)
        self.product_api = Products(marketplace=marketplace, refresh_token=refresh_token, credentials=credentials)
        self.seller_id = seller_id
        self.marketplace = marketplace

    @throttle_retry(tries=10, delay=5, rate=1.3)
    def get_listing_item(self, sku):
        return self.listing_api.get_listings_item(self.seller_id, sku)

    @throttle_retry(tries=10, delay=5, rate=1.3)
    def get_product_pricing_for_skus(self, sku_list):
        return self.product_api.get_product_pricing_for_skus(sku_list)




