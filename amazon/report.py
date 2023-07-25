import time

from sp_api.base import ReportType

credentials = dict(
    refresh_token='Atzr|IwEBIObDGBTpGvUcf55GYrCu2wKmFf_lgBkkBD48bmHW2M-wuFOs2O45AQZ2bu11GMfB-bSG2dY14QjhNOt1yvbUa94gzKdVEiZDdTVBzF07nYenxs30BVCYyINn002puEZ-9Fh3D_RvaxBCvNcpS2IwFbwXCNvwMD6K0160YI3cTPOmMT4LZ5eykTXL6KlKU6jxoFDO8wvsPoDE8lD8BbWfTVFsyPlQIybCOufLoKOiYhYk-Q8TIKUHnRvBilq_sM2O-iZU78Z1jfGXGiLgBy9DYRcJXybR4GEwxIXQ_zDi_8znYA',
    lwa_app_id='amzn1.application-oa2-client.2012e16cda8f46edb6180c6cd3dcd6d8',
    lwa_client_secret='amzn1.oa2-cs.v1.81a2cc9af8280a7352460951ecc89dbce2a78b774d711736d03dd37f7d10b487',
    aws_access_key='AKIAZ2ETATIEAD2VJISF',
    aws_secret_key='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',
    role_arn='arn:aws:iam::674618186248:role/silk_test',
)

from sp_api.api import Reports
from sp_api.base import Marketplaces

res = Reports(credentials=credentials).create_report(
    reportType=ReportType.GET_MERCHANT_LISTINGS_DATA_BACK_COMPAT,
    MarketplaceId='TEST_CASE_200'
)
time.sleep(10)
print(res)