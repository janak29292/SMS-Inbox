from celery import Celery

app = Celery('tasks', broker='redis://127.0.0.1:6379/0')

@app.task
def send_sms(sender, receiver, text):
    print(f"""
        folowing message sent from {sender} to {receiver}

        {text}
        """
          )
