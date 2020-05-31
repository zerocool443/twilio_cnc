from twilio.rest import Client
import sys

account_sid = '<twilio account id>'
auth_token = '<twilio api creds>'
client = Client(account_sid, auth_token)

message = client.messages.create(from_="whatsapp:" + sys.argv[2],body=sys.argv[1],to="whatsapp:"+sys.argv[3])

print(message.sid)

