# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from mysql import connector

class OpnSrcMlListPipeline:

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = connector.connect(
            host="localhost",
            user="root",
            passwd="root",
            database="opn_src_ml"
        )
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS projects""")
        self.curr.execute(
            """CREATE TABLE projects(
                  id INT NOT NULL AUTO_INCREMENT, 
                  name TEXT,
                  url TEXT,
                  PRIMARY KEY(id))
             """)
    def store_db(self,item):
        self.curr.execute(
            """INSERT INTO projects (name, url) VALUES(%s,%s)""", (
                item["prj_name"], item["url"]
            )
        )
        self.conn.commit()
    def process_item(self, item, spider):
        self.store_db(item)
        print("injecting in db")
        return item