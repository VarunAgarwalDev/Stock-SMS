from twilio.rest import Client
from  data_compile import get_data

# Your Account SID from twilio.com/console
account_sid = "AC73fbac12e93b16367e84cd8263d3b9c8"
# Your Auth Token from twilio.com/console
auth_token  = "82203b287d3245185b6c8ea9f3f22bd7"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+14087841112",
    from_="+19713333528",
    body="Check change for AMD")

print(message.sid)
