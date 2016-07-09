#coding:utf-8
from twisted.enterprise import adbapi
import MySQLdb
import MySQLdb.cursors
from scrapy.crawler import Settings as settings
class ZadsPipeline(object):

    def __init__(self):

        dbargs = dict(
                host = '127.0.0.1' ,
                db = 'zreading',
                user = 'root', #replace with you user name
                passwd = 'root', # replace with you password
                charset = 'utf8',
                cursorclass = MySQLdb.cursors.DictCursor,
                use_unicode = True,
        )
        self.dbpool = adbapi.ConnectionPool('MySQLdb',**dbargs)


    '''
    The default pipeline invoke function
    '''
    def process_item(self, item,spider):
        res = self.dbpool.runInteraction(self.insert_into_table,item)
        return item

    def insert_into_table(self,conn,item):
        conn.execute('insert into zreading(title,author,pub_date,types,tags,view_counts,content) values(%s,%s,%s,%s,%s,%s,%s)', (item['title'],item['author'],item['pub_date'],item['types'],item['tags'],item['view_count'],item['content']))