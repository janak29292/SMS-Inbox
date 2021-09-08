import json

from framework.query import create_query, list_query
from tasks import send_sms


def send_sms_api(request):
    post = json.loads(request.rfile.read(
        int(request.headers['Content-length'])
    ))
    sender = post.get('senderPhone')
    receiver = post.get('receiverPhone')
    text = post.get('messageText')
    create_query(sender, receiver, text)
    send_sms.delay(sender, receiver, text)
    return {
        "details": "sent"
    }


def get_sms_hook(request):
    post = json.loads(request.rfile.read(
        int(request.headers['Content-length'])
    ))
    sender = post.get('senderPhone')
    receiver = post.get('receiverPhone')
    text = post.get('messageText')
    timestamp = post.get('timestamp')
    uuid = post.get('uuid')
    create_query(sender, receiver, text, timestamp, uuid)
    return {
        "details": "received"
    }


def list_sms(request):
    param_path = request.path.split('?')[1] if len(request.path.split('?')) > 1 else ''
    query_params = {i.split('=')[0]: i.split('=')[1] for i in list(filter(None, param_path.split('&')))}
    sender = query_params.get('sender')
    response = []
    if sender:
        response = list_query(sender)
    return {
        "response": response
    }
