
from twilio.rest import Client

account_sid = 'AC1515c031e3333369b204c6d7de071c70'
auth_token = '7eb60f36cf8598daa668a4da800063e4'
client = Client(account_sid, auth_token)

call = client.calls.create(
                        to="+639437057481",
                        from_="+12019493856",
                        url="http://demo.twilio.com/docs/voice.xml"
                    )

print(call.sid)
 
