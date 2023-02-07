from .get_data import GetData
from datetime import datetime
from google.protobuf import json_format

class SaveData:

    def __init__(self, cur, conn):
        '''Initializing the object's attributes'''
        
        self.conn = conn # To connect with Postgres
        self.cur = cur # The cursor from Postgres
        self.data = datetime.now().date() # Setting today's date

    def fb_save_data(self, fb_table):
        '''Saving data from Facebook to database'''
        
        # Getting data
        fb_audience = GetData().fb_get_data()
        
        for i in fb_audience:

            id_publico = i['id']
            nome_publico = i['name']
            account_id = i['account_id']
            source_subtype = i['data_source']['sub_type']
            publico_subtype = i['subtype']
            tamanho_publico = i['approximate_count_upper_bound']
            
            # Saving data in Postgres
            query = f"INSERT INTO {fb_table} (data, id_publico, nome_publico, account_id, source_subtype, publico_subtype, tamanho_publico) VALUES (%s, %s, %s, %s, %s, %s, %s);"
            lista_res = [self.data,id_publico,nome_publico,account_id,source_subtype,publico_subtype,tamanho_publico]
            self.cur.execute(query,lista_res)
            self.conn.commit()
    
    def gg_save_data(self, gg_table):
        '''Saving data from Google to database'''
        
        # Getting data
        gg_audience = GetData().gg_get_data()
        
        for batch in gg_audience:
            for row in batch.results:
                dict_c = json_format.MessageToDict(row._pb)
                if dict_c['userList']['type'] != 'SIMILAR':

                    id_publico = dict_c['userList']['id']
                    nome_publico = dict_c['userList']['name']
                    _type = dict_c['userList']['type']
                    size_range_for_search = dict_c['userList']['sizeRangeForSearch']
                    size_range_for_display = dict_c['userList']['sizeRangeForDisplay']
                    size_for_search = int(dict_c['userList']['sizeForSearch'])
                    size_for_display = int(dict_c['userList']['sizeForDisplay'])
                    
                    # Saving data in Postgres
                    query = f"INSERT INTO {gg_table} (data, id_publico, nome_publico, type, size_range_for_search, size_range_for_display, size_for_search, size_for_display) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"
                    lista_res = [self.data,id_publico,nome_publico,_type,size_range_for_search,size_range_for_display,size_for_search,size_for_display]
                    self.cur.execute(query,lista_res)
                    self.conn.commit()


