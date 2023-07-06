import os
os.environ['AWS_ENV'] = 'SANDBOX'

credentials = dict(
    refresh_token='Atzr|IwEBIObDGBTpGvUcf55GYrCu2wKmFf_lgBkkBD48bmHW2M-wuFOs2O45AQZ2bu11GMfB-bSG2dY14QjhNOt1yvbUa94gzKdVEiZDdTVBzF07nYenxs30BVCYyINn002puEZ-9Fh3D_RvaxBCvNcpS2IwFbwXCNvwMD6K0160YI3cTPOmMT4LZ5eykTXL6KlKU6jxoFDO8wvsPoDE8lD8BbWfTVFsyPlQIybCOufLoKOiYhYk-Q8TIKUHnRvBilq_sM2O-iZU78Z1jfGXGiLgBy9DYRcJXybR4GEwxIXQ_zDi_8znYA',
    lwa_app_id='amzn1.application-oa2-client.2012e16cda8f46edb6180c6cd3dcd6d8',
    lwa_client_secret='amzn1.oa2-cs.v1.81a2cc9af8280a7352460951ecc89dbce2a78b774d711736d03dd37f7d10b487',
    aws_access_key='AKIAZ2ETATIEAD2VJISF',
    aws_secret_key='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',
    role_arn='arn:aws:iam::674618186248:role/silk_test',
)

from sp_api.api import Catalog, CatalogItems


# 获取所有产品 (test success)
# res = Catalog(credentials=credentials).list_items(MarketplaceId='TEST_CASE_200', SellerSKU='SKU_200')
# 获取单个产品 (test success)
# res = Catalog(credentials=credentials).get_item('ASIN_200', MarketplaceId='ATVPDKIKX0DER')

# 根据条件获取产品 (sandbox success  keywords应该是一个array，以逗号分隔的字符串)
# res = CatalogItems(credentials=credentials).search_catalog_items(keywords="red,polo,shirt",
#                                                                  marketplaceIds='ATVPDKIKX0DER',
#                                                                  includedData='summaries')

# sandbox调用，根据ASIN获取单个产品，includedData表示要显示的信息  （sandbox success）
# res = CatalogItems(credentials=credentials).get_catalog_item('B07N4M94X4',
#                                                              marketplaceIds='ATVPDKIKX0DER',
#                                                              includedData=["identifiers", "images", "productTypes",
#                                                                            "salesRanks", "summaries", "variations",
#                                                                            "vendorDetails"])

# print(res)

custom_resource = {
    'redis': {
        'host': 'your_redis_hostname',
        'port': 'your_redis_port',
        'username': 'your_redis_username',
        'password': 'your_redis_password'
    }
}

def create_custom_destination(name, **kwargs):
    # 修改resource_name和data字典以使用自定义的资源类型和参数
    resource_name = 'redis' if not kwargs.get('account_id') else 'eventBridge'

    data = {
        'resourceSpecification': {
            resource_name: custom_resource['redis'] if resource_name == 'redis' else {
                'region': kwargs.get('region', None),
                'accountId': kwargs.get('account_id')
            }
        },
        'name': name,
    }

    # 调用原始的create_destination方法，并传递修改后的参数
    return Notifications(credentials=credentials).create_destination(name, arn=None, **data)

from sp_api.api import Notifications

# create Destination
# res = Notifications(credentials=credentials).create_destination(scope='sellingpartnerapi::notifications',
#                                          name='test',
#                                          arn='arn:aws:sqs:us-east-2:444455556666:queue1',)

res = create_custom_destination(name='test')
print(res)


# first
# second
# third
# forth
# fifth

# 1
# 2
# 3
# 4