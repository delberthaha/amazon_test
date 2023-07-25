import json
import os
from urllib.parse import urlencode

from sp_api.base import ReportType

os.environ['AWS_ENV'] = 'SANDBOX'


credentials = dict(
    refresh_token='Atzr|IwEBIObDGBTpGvUcf55GYrCu2wKmFf_lgBkkBD48bmHW2M-wuFOs2O45AQZ2bu11GMfB-bSG2dY14QjhNOt1yvbUa94gzKdVEiZDdTVBzF07nYenxs30BVCYyINn002puEZ-9Fh3D_RvaxBCvNcpS2IwFbwXCNvwMD6K0160YI3cTPOmMT4LZ5eykTXL6KlKU6jxoFDO8wvsPoDE8lD8BbWfTVFsyPlQIybCOufLoKOiYhYk-Q8TIKUHnRvBilq_sM2O-iZU78Z1jfGXGiLgBy9DYRcJXybR4GEwxIXQ_zDi_8znYA',
    lwa_app_id='amzn1.application-oa2-client.2012e16cda8f46edb6180c6cd3dcd6d8',
    lwa_client_secret='amzn1.oa2-cs.v1.81a2cc9af8280a7352460951ecc89dbce2a78b774d711736d03dd37f7d10b487',
    aws_access_key='AKIAZ2ETATIEAD2VJISF',
    aws_secret_key='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',
    role_arn='arn:aws:iam::674618186248:role/silk_test',
)


# class Credentials:
#     def __init__(self, **kwargs):
#         for key, value in kwargs.items():
#             setattr(self, key, value)

# credentials = Credentials(
#     refresh_token='Atzr|IwEBIObDGBTpGvUcf55GYrCu2wKmFf_lgBkkBD48bmHW2M-wuFOs2O45AQZ2bu11GMfB-bSG2dY14QjhNOt1yvbUa94gzKdVEiZDdTVBzF07nYenxs30BVCYyINn002puEZ-9Fh3D_RvaxBCvNcpS2IwFbwXCNvwMD6K0160YI3cTPOmMT4LZ5eykTXL6KlKU6jxoFDO8wvsPoDE8lD8BbWfTVFsyPlQIybCOufLoKOiYhYk-Q8TIKUHnRvBilq_sM2O-iZU78Z1jfGXGiLgBy9DYRcJXybR4GEwxIXQ_zDi_8znYA',
#     lwa_app_id='amzn1.application-oa2-client.2012e16cda8f46edb6180c6cd3dcd6d8',
#     lwa_client_secret='amzn1.oa2-cs.v1.81a2cc9af8280a7352460951ecc89dbce2a78b774d711736d03dd37f7d10b487'
# )


from sp_api.api import Catalog, CatalogItems, Sellers, Authorization
from sp_api.auth import AccessTokenClient


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

# 获取seller信息（sandbox）
# res = Sellers(credentials=credentials, refresh_token=refresh_token).get_marketplace_participation()
# print(res)
# print(res.payload.name)
# print(res.payload.demainName)
# 获取authorization_code
# res = Authorization(credentials=credentials).get_authorization_code(
#     mwsAuthToken='test',
#     developerId='test',
#     sellingPartnerId='test',
#     withScopes='sellingpartnerapi::migration'
# )

# get access token
# res = AccessTokenClient(credentials=credentials).get_auth()

# get grantless_authorization
# res = AccessTokenClient(credentials=credentials).authorize_auth_code('ANDMxqpCmqWHJeyzdbMH')

# print(res.refresh_token)
# print(res.access_token)

# custom_resource = {
#     'redis': {
#         'host': 'your_redis_hostname',
#         'port': 'your_redis_port',
#         'username': 'your_redis_username',
#         'password': 'your_redis_password'
#     }
# }

# def create_custom_destination(name, **kwargs):
#     # 修改resource_name和data字典以使用自定义的资源类型和参数
#     resource_name = 'redis' if not kwargs.get('account_id') else 'eventBridge'
#
#     data = {
#         'resourceSpecification': {
#             resource_name: custom_resource['redis'] if resource_name == 'redis' else {
#                 'region': kwargs.get('region', None),
#                 'accountId': kwargs.get('account_id')
#             }
#         },
#         'name': name,
#     }
#
#     # 调用原始的create_destination方法，并传递修改后的参数
#     return Notifications(credentials=credentials).create_destination(name, arn=None, **data)
#
# from sp_api.api import Notifications

# create Destination
# res = Notifications(credentials=credentials).create_destination(scope='sellingpartnerapi::notifications',
#                                          name='test',
#                                          arn='arn:aws:sqs:us-east-2:444455556666:queue1',)

# res = create_custom_destination(name='test')
# print(res)


# first
# second
# third
# forth
# fifth

# 1
# 2
# 3
# 4
# from sp_api.api import Reports
# class Report:
#     def __init__(self, credentials=None):
#         self.credentials = credentials
#
#     def create_reports(self):
#         response = Reports(credentials=self.credentials).create_report(
#             reportType=ReportType.GET_MERCHANT_LISTINGS_DATA,
#             dataStartTime='2019-12-10T20:11:24.000Z',
#             marketplaceIds=[
#                 "A1PA6795UKMFR9",
#                 "ATVPDKIKX0DER"
#             ]
#         )
#         return response
#
# credentials = dict(
#     refresh_token='Atzr|IwEBIObDGBTpGvUcf55GYrCu2wKmFf_lgBkkBD48bmHW2M-wuFOs2O45AQZ2bu11GMfB-bSG2dY14QjhNOt1yvbUa94gzKdVEiZDdTVBzF07nYenxs30BVCYyINn002puEZ-9Fh3D_RvaxBCvNcpS2IwFbwXCNvwMD6K0160YI3cTPOmMT4LZ5eykTXL6KlKU6jxoFDO8wvsPoDE8lD8BbWfTVFsyPlQIybCOufLoKOiYhYk-Q8TIKUHnRvBilq_sM2O-iZU78Z1jfGXGiLgBy9DYRcJXybR4GEwxIXQ_zDi_8znYA',
#     lwa_app_id='amzn1.application-oa2-client.2012e16cda8f46edb6180c6cd3dcd6d8',
#     lwa_client_secret='amzn1.oa2-cs.v1.81a2cc9af8280a7352460951ecc89dbce2a78b774d711736d03dd37f7d10b487',
#     aws_access_key='AKIAZ2ETATIEAD2VJISF',
#     aws_secret_key='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',
#     role_arn='arn:aws:iam::674618186248:role/silk_test',
# )
#
# res = Report(credentials).create_reports()
# print(res)


import datetime

# 假设您有一个时间戳值
# timestamp = 1626508800

# 将时间戳转换为datetime对象
# dt = datetime.datetime.fromtimestamp(timestamp)

# 将datetime对象格式化为ISO 8601格式的时间字符串
# iso8601_time = dt.isoformat()
#
# print(iso8601_time)

from sp_api.base import Marketplaces

# import requests
#
# request_data = dict(
#     grant_type='refresh_token',
#     refresh_token='Atzr|IwEBIObDGBTpGvUcf55GYrCu2wKmFf_lgBkkBD48bmHW2M-wuFOs2O45AQZ2bu11GMfB-bSG2dY14QjhNOt1yvbUa94gzKdVEiZDdTVBzF07nYenxs30BVCYyINn002puEZ-9Fh3D_RvaxBCvNcpS2IwFbwXCNvwMD6K0160YI3cTPOmMT4LZ5eykTXL6KlKU6jxoFDO8wvsPoDE8lD8BbWfTVFsyPlQIybCOufLoKOiYhYk-Q8TIKUHnRvBilq_sM2O-iZU78Z1jfGXGiLgBy9DYRcJXybR4GEwxIXQ_zDi_8znYA',
#     client_id='amzn1.application-oa2-client.2012e16cda8f46edb6180c6cd3dcd6d8',
#     client_secret='amzn1.oa2-cs.v1.81a2cc9af8280a7352460951ecc89dbce2a78b774d711736d03dd37f7d10b487'
# )
# headers = {
#     'content-type': 'application/json',
#     'accept': 'application/json'
# }
# response = requests.post(
#     url='https://api.amazon.com/auth/o2/token',
#     headers=headers,
#     data=json.dumps(request_data)
# )
# print(response.json()['refresh_token'])


from sp_api.api import Catalog
