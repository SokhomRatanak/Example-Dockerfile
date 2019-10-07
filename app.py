import time

import redis
from flask import Flask
import pytz

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

@app.route('/')
def hello():
    from datetime import datetime, timezone

    utc_dt = datetime.now(timezone.utc)

    mcw = pytz.timezone('Europe/Moscow')

    return 'Moscow time {}\n'.format(utc_dt.astimezone(mcw).isoformat())
