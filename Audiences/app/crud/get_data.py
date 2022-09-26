from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.api import FacebookAdsApi 
from google.ads.googleads.client import GoogleAdsClient
# from ..core.config import ACCESS_TOKEN,AD_ACCOUNT_ID,APP_SECRET,APP_ID,DEVELOPER_TOKEN,REFRESH_TOKEN,CLIENT_ID,CLIENT_SECRET,USE_PROTO_PLUS,LOGIN_CUSTOMER_ID,CLIENT_CUSTOMER_ID

class GetData:

    @classmethod
    def fb_connect(self):
        '''Conectar com a API do facebook'''
        FacebookAdsApi.init(app_id='244112144481695', app_secret='3a0ce148e278c623f58ebd8696f03cd9', access_token='EAADeBMmoPZA8BAK3342XUrw6QqdtTkZBEmEPRkNym681GLZAenGD601L6b2FUqcCcnhwKQUD6c7bgrCwOyQ0v67YqPskC7H7iPTO9Ryv7B2dRkyadnI8kcYLz1Ar950267d3ephG997MdqEkxcat3kP7ZAxoax99JQ38QXBUSXMVwd3yjUKCepZCmGlb0llwZD')
        my_account = AdAccount('act_539335706086363')
        return my_account

    @classmethod
    def gg_connect(self):
        '''Conectar com a API do google'''
        credentials = {
            "developer_token": 'TuiDyP9dHpwqeTiK2CK3hw',
            "refresh_token": '1//04AYdl28RusvgCgYIARAAGAQSNwF-L9Ir-UYWM8jEcQKtn5POLNP2PSNGK4_9rXp4yfLAlJUz5bxSp_JT6eXDNnmk4yeWpXwzPKA',
            "client_id": '153099513924-s4996uqr8lgdjin3im0jqrr0dj820vbb.apps.googleusercontent.com',
            "client_secret": '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',
            "use_proto_plus": True,
            "login_customer_id": '3769811531'}
        client_g = GoogleAdsClient.load_from_dict(credentials, version="v10")
        ga_service = client_g.get_service("GoogleAdsService")
        return ga_service
    
    def fb_get_data(self):
        my_account = self.fb_connect()
        fields = [
            'id',
            'name',
            'approximate_count_upper_bound',
            'subtype',
            'data_source',
            'account_id'
        ]
        params = {
        }
        audiences = list(my_account.get_custom_audiences(fields=fields, params=params))

        audiences_filt = list(filter(lambda c: c['subtype'] != 'LOOKALIKE', audiences))

        return audiences_filt

    def gg_get_data(self):
        ga_service = self.gg_connect()
        query = """
            SELECT
                user_list.id,
                user_list.type,
                user_list.size_range_for_search,
                user_list.size_range_for_display,
                user_list.size_for_search,
                user_list.size_for_display,
                user_list.name
            FROM user_list
        """
        stream = ga_service.search_stream(customer_id='3769811531', query=query)

        return stream

