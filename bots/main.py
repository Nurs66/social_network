import json
import random
import os
import requests
import telebot
from faker import Faker

fake = Faker()

bot = telebot.TeleBot('1828576704:AAH_f16knXZRqP_7WaQRduLlyaa9mWiWZ6Q')
BASE_URL = 'http://0.0.0.0:8000/api/{}'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/50.0.2661.102 Safari/537.36',
    'Content-Type': 'application/json',
}

user_data = []


@bot.message_handler(commands=["start"])
def get_text_message(message):
    if message.text == '/start':
        bot.send_message(message.from_user.id, 'Welcome Social Network')
        bot.send_message(message.from_user.id, 'Select commands')
        bot.send_message(message.from_user.id, "/signup -- Register")
        bot.send_message(message.from_user.id, "/number_of_users -- Count all user on database")
        bot.send_message(message.from_user.id, "/max_posts_per_user -- Create posts")
        bot.send_message(message.from_user.id, "/max_likes_per_user -- Add like to posts randomly")
    else:
        bot.send_message(message.from_user.id, 'Напиши /start чтобы начать')


@bot.message_handler(commands=["signup"])
def get_social_network_signup(message):
    with open('configs.json', 'r') as configs:
        config_data = json.load(configs)
    if message.text == '/signup':
        for i in range(config_data['user_count']):
            data = {
                "email": f"{fake.first_name_male()}@qwe.qwe",
                "first_name": f"{fake.first_name_male()}",
                "last_name": f"{fake.last_name()}",
                "password": f"Bvu5S^;:?^y$7@bQ{random.randint(1, 100)}"
            }
            user_data.append(data)
            response = requests.post(BASE_URL.format('users/signup/'), json=data, headers=headers)
            bot.send_message(message.from_user.id, f"Created all user -- Email: {data['email']} - "
                                                   f"Status code: {response.status_code}")


@bot.message_handler(commands=["number_of_users"])
def get_social_network_num_of_user(message):
    if message.text == '/number_of_users':
        bot.send_message(message.from_user.id, 'Запрос обрабатывается...')
        user_json = user_data[1]
        json_data = {
            "email": user_json['email'],
            "password": user_json['password']
        }
        response = requests.post(BASE_URL.format('token/'), json=json_data, headers=headers)
        response_result = response.json()
        headers.update({'Authorization': f'Bearer {response_result["access"]}'})
        get_all_user = requests.get(BASE_URL.format('users/users/'), headers=headers)
        response_result_of_user = get_all_user.json()
        bot.send_message(message.from_user.id, f"Number_of_users -- {response_result_of_user['count']}")



@bot.message_handler(commands=["max_posts_per_user"])
def get_social_network_max_posts_per_user(message):
    with open('configs.json', 'r') as configs:
        config_data = json.load(configs)
    if message.text == '/max_posts_per_user':
        bot.send_message(message.from_user.id, 'Запрос обрабатывается...')
        for i in range(config_data['user_posts']):
            user_json = random.choice(user_data)
            json_data = {
                "email": user_json['email'],
                "password": user_json['password']
            }
            response = requests.post(BASE_URL.format('token/'), json=json_data, headers=headers)
            response_result = response.json()
            headers.update({'Authorization': f'Bearer {response_result["access"]}'})
            post_data = {
                "title": f"{user_json['email']}",
                "description": f"Description {i}"
            }
            created_post = requests.post(BASE_URL.format('posts/posts/'), json=post_data, headers=headers)
            bot.send_message(message.from_user.id, f"Created post: {post_data} "
                                                   f"Status code: {created_post.status_code}"
                             )


def response_post_obj():
    id_of_product = []
    user_json_data = user_data[1]
    json_data = {
        "email": user_json_data['email'],
        "password": user_json_data['password']
    }
    response = requests.post(BASE_URL.format('token/'), json=json_data, headers=headers)
    response_result = response.json()
    headers.update({'Authorization': f'Bearer {response_result["access"]}'})
    all_products = requests.get(BASE_URL.format('posts/posts/'), headers=headers)
    response_result_of_product = all_products.json()
    for i in response_result_of_product["results"]:
        id_of_product.append(i['id'])
    return id_of_product


@bot.message_handler(commands=["max_likes_per_user"])
def get_social_network_max_likes_per_user(message):
    with open('configs.json', 'r') as configs:
        config_data = json.load(configs)
    if message.text == '/max_likes_per_user':
        bot.send_message(message.from_user.id, 'Запрос обрабатывается...')
        get_all_posts = response_post_obj()
        for i in range(config_data['user_likes']):
            user_json = random.choice(user_data)
            random_id_of_post = random.choice(get_all_posts)
            json_data = {
                "email": user_json['email'],
                "password": user_json['password']
            }
            response = requests.post(BASE_URL.format('token/'), json=json_data, headers=headers)
            response_result = response.json()
            headers.update({'Authorization': f'Bearer {response_result["access"]}'})
            post_like = {
                "post": random_id_of_post
            }
            get_posts = requests.post(BASE_URL.format('posts/likes/'), json=post_like, headers=headers)
            response_result_of_user = get_posts.json()
            bot.send_message(message.from_user.id, f"Like data -- {response_result_of_user} "
                                                   f"Status code: {get_posts.status_code}"
                             )


bot.polling(none_stop=True, interval=0)
