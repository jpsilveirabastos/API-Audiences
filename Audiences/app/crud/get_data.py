from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.api import FacebookAdsApi 
from google.ads.googleads.client import GoogleAdsClient
from ..core.config import ACCESS_TOKEN,AD_ACCOUNT_ID,APP_SECRET,APP_ID,DEVELOPER_TOKEN,REFRESH_TOKEN,CLIENT_ID,CLIENT_SECRET,USE_PROTO_PLUS,LOGIN_CUSTOMER_ID,CLIENT_CUSTOMER_ID

class GetData:

    @classmethod
    def fb_connect(self):
        '''Conectar com a API do facebook'''
        FacebookAdsApi.init(app_id=APP_ID, app_secret=APP_SECRET, access_token=ACCESS_TOKEN)
        my_account = AdAccount(AD_ACCOUNT_ID)
        return my_account

    @classmethod
    def gg_connect(self):
        '''Conectar com a API do google'''
        credentials = {
            "developer_token": DEVELOPER_TOKEN,
            "refresh_token": REFRESH_TOKEN,
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
            "use_proto_plus": USE_PROTO_PLUS,
            "login_customer_id": LOGIN_CUSTOMER_ID}
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
        stream = ga_service.search_stream(customer_id=CLIENT_CUSTOMER_ID, query=query)

        return stream

