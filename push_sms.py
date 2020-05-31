from twilio.rest import Client
import sys

account_sid = '<twilio accound sid>'
auth_token = '<Twilio auth tokens>'
client = Client(account_sid, auth_token)

message = client.messages.create(from_=sys.argv[2],body=sys.argv[1],to=sys.argv[3])

print(message.sid)

