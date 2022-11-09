from cgi import print_arguments
from django.db import connection
from .models import Categories
from users.models import Account

def get_articles_sidebar():
    query = f"SELECT * FROM articles WHERE category_id = %s LIMIT 3"
    data_list = []
    with connection.cursor() as cursor:
        cursor.execute(query,[4])
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
                "title":data[1],
                "id":data[0],
            }
            data_list.append(json_data)
    return data_list


def get_category(id):
    category = Categories.objects.get(id=id)
    category_data ={
        'name':category.name,
        'slug':category.slug
    }
    return category_data

def get_writer(id):
    writer = Account.objects.get(id=id)
    writer_data ={
        'image':writer.image,
        'description': writer.description
        }
    return writer_data

def articles_list(query="All"):
    data_list = []
    if query == "All":
        query = "SELECT * FROM articles"
    elif query == "articles":
        query = "SELECT * FROM articles WHERE kind = 'articles'"
    elif query == "videos":
        query = "SELECT * FROM articles WHERE kind = 'videos'"
    elif query == "news":
        query = "SELECT * FROM articles WHERE kind = 'news'"

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

def category_list(slug):
    data_list = []
    query = f"SELECT * FROM articles WHERE category_slug = %s"
    
    with connection.cursor() as cursor:
        cursor.execute(query,[slug])
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

def get_article(slug):
    query = f"SELECT * FROM articles WHERE slug = %s"
    
    with connection.cursor() as cursor:
        cursor.execute(query,[slug])
        data = cursor.fetchone()
        writer = get_writer(data[17])
        json_data = {
            "name_image":writer['image'],
            "name_description":writer['description'],
            "kind":data[18],
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
    return json_data


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