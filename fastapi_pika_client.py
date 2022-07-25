import json
import aio_pika as pika
from aio_pika import connect, connect_robust, IncommingMessage, ExchangeType, Message, Exchange
import uuid
import ssl
from os import getenv as env

RMQ_HOST = env('RMQ_HOST')
RMQ_PORT = env('RMQ_PORT')
RMQ_VHOST = env('RMQ_VHOST')
RMQ_USERNAME = env('RMQ_USERNAME', None)
RMQ_PASSWORD = env('RMQ_PASSWORD', None)


class PikaClient:
  
  def __init__(self, callback, host=RMQ_HOST, port=RMQ_PORT, vhost=RMQ_VHOST, ssl_enabled=RMQ_SSL, **kwargs):
    
    self.host = host
