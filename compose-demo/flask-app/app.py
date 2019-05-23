# coding=utf-8
"""
    Created by prakash on 23/05/19
"""
import time

import redis
from flask import Flask

__author__ = 'Prakash14'

app = Flask(__name__)
cache = redis.Redis(host="redis-service", port=6379)


def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)


@app.route('/')
def hello():
    count = get_hit_count()
    return 'Hello World! I have been seen {} times.\n'.format(count)


@app.after_request
def after_request(response):
    print("========================================")
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
