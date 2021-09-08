from views import list_sms, send_sms_api, get_sms_hook

url_patterns = (
    ('/messages/', list_sms),
    ('/send/', send_sms_api),
    ('/get-hook/', get_sms_hook)
)
