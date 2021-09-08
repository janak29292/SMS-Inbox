# SMS Inbox

Application for sending and receiving sms messages 

## Prerequisite

Need to have the following services installed and running

```bash
# For database
postgres
# For async message passing for celery worker
redis-server
```

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.

```bash
virtualenv venv -p python3
source venv/bin/activate
pip install -r requirements.txt
```
## Setup Database

```bash
source venv/bin/activate
python setup.py
```
## Running local server and celery worker

```bash
# run server
source venv/bin/activate
python server.py

# run celery worker
source venv/bin/activate
celery -A tasks worker -l INFO

```

## Usage
The Application has 3 APIs namely for sending, receiving and listing messages that can be accessed using POSTMAN

```bash
# Sending message

http://localhost:8000/send/  (POST)
# body
{
"senderPhone": "+14155551234",
"receiverPhone": "+14165559876",
"messageText": "Hello world!",
}

# Receiving message through webhook

http://localhost:8000/get-hook/  (POST)
# body
{
"senderPhone": "+14165559876",
"receiverPhone": "+14155551234",
"messageText": "Hello back!",
"timestamp": 1630003346,
"uuid": "324acba0-88d2-4bec-91cf-56cfd2ef8b89"
}

# Listing sent and received messages chronologically for user with phone number +14155551234

http://localhost:8000/messages/?sender=+14155551234  (GET)
```
