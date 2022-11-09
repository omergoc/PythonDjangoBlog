from django.db import connection

def date_convert(date):
    wcd1 = date
    wcd2_1 = wcd1.split(" ")[0]
    wcd2_2 = wcd1.split(" ")[1] #saat

    wcd3_1 = wcd2_1.split("/")[0] #gun
    wcd3_2 = wcd2_1.split("/")[1] #ay
    wcd3_3 = wcd2_1.split("/")[2] #yıl
    if(wcd3_2=="01"):
        wcd3_2 = "Ocak"
    elif(wcd3_2=="02"):
        wcd3_2 = "Şubat"
    elif(wcd3_2=="03"):
        wcd3_2 = "Mart"
    elif(wcd3_2=="04"):
        wcd3_2 = "Nisan"
    elif(wcd3_2=="05"):
        wcd3_2 = "Mayıs"
    elif(wcd3_2=="06"):
        wcd3_2 = "Haziran"       
    elif(wcd3_2=="07"):
        wcd3_2 = "Temmuz"     
    elif(wcd3_2=="08"):
        wcd3_2 = "Ağustos"     
    elif(wcd3_2=="09"):
        wcd3_2 = "Eylül"
    elif(wcd3_2=="10"):
        wcd3_2 = "Ekim"
    elif(wcd3_2=="11"):
        wcd3_2 = "Kasım"
    elif(wcd3_2=="12"):
        wcd3_2 = "Aralık"

    wdc_4 = wcd3_1+" "+wcd3_2+" "+wcd3_3+" "+wcd2_2
    return wdc_4

def get_viewcount(id):
    query = f"SELECT * FROM articles WHERE id = %s"
    
    with connection.cursor() as cursor:
        cursor.execute(query,[id])
        data = cursor.fetchone()
        json_data = {
            "view_count":data[2],
        }
    return json_data

def mostliked_list():
    data_list = []
    query = "SELECT * FROM articles"
    
    with connection.cursor() as cursor:
        cursor.execute(query)
        rows = cursor.fetchall()

    for data in rows:
        json_data = {
            "name_slug":data[11],
            "name":data[10],
            "created_date":data[9],
            "category_slug":data[8],
            "category_name":data[7],
            "image":data[6],
            "slug":data[5],
            "content":data[4],
            "description":data[3],
            "view_count":data[2],
            "title":data[1],
        }
        data_list.append(json_data)
    return data_list


def get_articles_list():
    data_list = []
    query = "SELECT * FROM articles ORDER BY view_count DESC"
    
    with connection.cursor() as cursor:
        cursor.execute(query)
        rows = cursor.fetchall()

    for data in rows:
        json_data = {
            "name_slug":data[11],
            "name":data[10],
            "created_date":data[9],
            "category_slug":data[8],
            "category_name":data[7],
            "image":data[6],
            "slug":data[5],
            "content":data[4],
            "description":data[3],
            "view_count":data[2],
            "title":data[1],
        }
        data_list.append(json_data)
    return data_list


def articles_list_json():
    data_list = []

    query = "SELECT * FROM articles ORDER BY id DESC"

    with connection.cursor() as cursor:
        cursor.execute(query)
        rows = cursor.fetchall()

    for data in rows:
        json_data = {
            "name_slug":data[11],
            "name":data[10],
            "created_date":data[9],
            "category_slug":data[8],
            "category_name":data[7],
            "image":data[6],
            "slug":data[5],
            "content":data[4],
            "description":data[3],
            "view_count":data[2],
            "title":data[1],
            "id":data[0],
        }
        data_list.append(json_data)
    return data_list