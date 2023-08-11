# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# scrap data -> items [container] -> pipeline -> SQL/Mongo Database
from itemadapter import ItemAdapter
# import mysql.connector
# code to inject to mongodb
import pymongo


class ScrapAmazonPipeline:
    def __init__(self):
        self.conn = pymongo.MongoClient("localhost", 27017)
        # creating database
        db = self.conn['quotes']
        self.collection = db['quotes_tb']

    def process_item(self, item, spider):
        self.collection.insert_one(dict(item))

#  code to inject to mysql server
# class ScrapAmazonPipeline:
#     def __init__(self):
#         self.create_connection()
#         self.create_table()
#
#     def create_connection(self):
#         self.conn = mysql.connector.connect(
#             host = "localhost",
#             user = "root",
#             passwd ="root",
#             database = "quotes"
#         )
#         self.curr = self.conn.cursor()
#
#     def create_table(self):
#         self.curr.execute("""DROP TABLE IF EXISTS quote_tb""")
#         self.curr.execute("""
#         CREATE TABLE quote_tb(
#             title text,
#             author text,
#             tag text)
#         """)
#
#     def store_db(self,item):
#         self.curr.execute("""INSERT INTO quote_tb VALUES (%s,%s,%s)""",(
#           item['title'], item['author'], item['tag']
#           ))
#         self.conn.commit()
#
#
#     def process_item(self, item, spider):
#         self.store_db(item)
#         print(f"injecting data in database")
#         return item
