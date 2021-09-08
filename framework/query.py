import uuid
from datetime import datetime

from framework.transaction import run_query


@run_query
def list_query(sender):
    return f"""
    Select * from message
    where
    receiver = '{sender}'
    or
    sender = '{sender}'
    order by timestamp;
    """


@run_query
def create_query(
        sender,
        receiver,
        text,
        timestamp=datetime.timestamp(datetime.now()),
        uuid=uuid.uuid4()):
    return f"""
    INSERT INTO message (sender, receiver, timestamp, text, uuid)
    VALUES ('{sender}', '{receiver}', '{int(timestamp)}', '{text}', '{uuid}');
    """
