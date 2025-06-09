#!/usr/bin/python3
"""
task_02_requests

this module contains 2 functions
to fetch a posts
"""
import requests
import csv


def fetch_and_print_posts():
    """
    this method print the posts
    """
    f = requests.get('https://jsonplaceholder.typicode.com/posts')
    print("Status Code: {}".format(f.status_code))
    if f.status_code == 200:
        API_data = f.json()
        for key in API_data:
            print(key['title'])


def fetch_and_save_posts():
    """
    this method write in to
    csv file the contente of the posts
    """
    f = requests.get('https://jsonplaceholder.typicode.com/posts')
    if f.status_code == 200:
        API_data = f.json()
        posts = [{"id": key["id"], "title": key["title"], "body": key["body"]}
                 for key in API_data]
        with open("posts.csv", "w", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(posts)
