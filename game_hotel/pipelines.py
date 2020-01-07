# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class GameHotelPipeline(object):
    def process_item(self, item, spider):
        conn = pymysql.connect(host="106.13.169.200", user="root", passwd="fool123000!", db="game_hotel")
        cursor = conn.cursor()
        insert_Time = ('').join(item['Time'])
        room_type = ('').join(item['room_type'])
        status = ('').join(item['status'])
        # price = ('').join(item['price'])
        hotel_name = ('').join(item['hotel_name'])
        if hotel_name == '铂宿电竞酒店':
            sql = """insert into 铂宿电竞酒店(insert_Time,room_type,status) values ('%s','%s','%s') """ % (
                insert_Time, room_type, status)
            print("正在存入数据库。。。。。。。。。。。。")
            cursor.execute(sql)
            conn.commit()
            conn.close()
            return item
        elif hotel_name == 'Teamwork电竞酒店':
            sql = """insert into Teamwork电竞酒店(insert_Time,room_type,status) values ('%s','%s','%s') """ % (
                insert_Time, room_type, status)
            print("正在存入数据库。。。。。。。。。。。。")
            cursor.execute(sql)
            conn.commit()
            conn.close()
            return item
        elif hotel_name == '青岛YK电竞民宿(CBD理工大学店)':
            sql = """insert into 青岛YK电竞民宿CBD理工大学店(insert_Time,room_type,status) values ('%s','%s','%s') """ % (
                insert_Time, room_type, status)
            print("正在存入数据库。。。。。。。。。。。。")
            cursor.execute(sql)
            conn.commit()
            conn.close()
            return item
        elif hotel_name == '青岛YK电竞民宿(崂山大拇指广场店)':
            sql = """insert into 青岛YK电竞民宿崂山大拇指广场店(insert_Time,room_type,status) values ('%s','%s','%s') """ % (
                insert_Time, room_type, status)
            print("正在存入数据库。。。。。。。。。。。。")
            cursor.execute(sql)
            conn.commit()
            conn.close()
            return item
        elif hotel_name == 'TOP电竞酒店':
            sql = """insert into TOP电竞酒店(insert_Time,room_type,status) values ('%s','%s','%s') """ % (
                insert_Time, room_type, status)
            print("正在存入数据库。。。。。。。。。。。。")
            cursor.execute(sql)
            conn.commit()
            conn.close()
            return item
        elif hotel_name == '艾克威电竞酒店':
            sql = """insert into 艾克威电竞酒店(insert_Time,room_type,status) values ('%s','%s','%s') """ % (
                insert_Time, room_type, status)
            print("正在存入数据库。。。。。。。。。。。。")
            cursor.execute(sql)
            conn.commit()
            conn.close()
            return item
        elif hotel_name == '玩家国度电竞酒店':
            sql = """insert into 玩家国度电竞酒店(insert_Time,room_type,status) values ('%s','%s','%s') """ % (
                insert_Time, room_type, status)
            print("正在存入数据库。。。。。。。。。。。。")
            cursor.execute(sql)
            conn.commit()
            conn.close()
            return item
        elif hotel_name == '青岛天敏电竞酒店':
            sql = """insert into 青岛天敏电竞酒店(insert_Time,room_type,status) values ('%s','%s','%s') """ % (
                insert_Time, room_type, status)
            print("正在存入数据库。。。。。。。。。。。。")
            cursor.execute(sql)
            conn.commit()
            conn.close()
            return item
        elif hotel_name == '铂悦电竞酒店(吾悦广场店)':
            sql = """insert into 铂悦电竞酒店吾悦广场店(insert_Time,room_type,status) values ('%s','%s','%s') """ % (
                insert_Time, room_type, status)
            print("正在存入数据库。。。。。。。。。。。。")
            cursor.execute(sql)
            conn.commit()
            conn.close()
            return item
        elif hotel_name == 'SOLO电竞酒店':
            sql = """insert into SOLO电竞酒店(insert_Time,room_type,status) values ('%s','%s','%s') """ % (
                insert_Time, room_type, status)
            print("正在存入数据库。。。。。。。。。。。。")
            cursor.execute(sql)
            conn.commit()
            conn.close()
            return item
        elif hotel_name == 'Online电竞酒店':
            sql = """insert into SOLO电竞酒店(insert_Time,room_type,status) values ('%s','%s','%s') """ % (
                insert_Time, room_type, status)
            print("正在存入数据库。。。。。。。。。。。。")
            cursor.execute(sql)
            conn.commit()
            conn.close()
            return item
        elif hotel_name == 'Galaxy电竞民宿':
            sql = """insert into SOLO电竞酒店(insert_Time,room_type,status) values ('%s','%s','%s') """ % (
                insert_Time, room_type, status)
            print("正在存入数据库。。。。。。。。。。。。")
            cursor.execute(sql)
            conn.commit()
            conn.close()
            return item