from twilio.rest import Client


account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+12058988926',
                     to='+40720075757'
                 )

print(message.sid)