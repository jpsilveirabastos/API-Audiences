from .config import DBNAME, USER, PASSWORD, HOST
import psycopg2

class Db:
    '''Connect to Postgres'''
    def connect():
        conn = psycopg2.connect(dbname=DBNAME, user=USER, password=PASSWORD, host=HOST)
        cur = conn.cursor()
        return cur,conn
    '''Disconnect to Postgres'''
    def disconnect(cur, conn):
        cur.close()
        conn.close()

    def fb_table():
        '''Table used to save facebook data'''
        fb_audience = 'fb_audience'
        return fb_audience
    
    def gg_table():
        '''Table used to save google data'''
        gg_audience = 'gg_audience'
        return gg_audience
