
from twilio.rest import Client

account_sid = 'ACcf1318a402be1d709edf69783888f986'
auth_token = '7d65cd5377b5c50a1ee9da8aaa2e94af'
client = Client(account_sid, auth_token)

call = client.calls.create(
                        to="+639437057481",
                        from_="+16504194114",
                        url="http://demo.twilio.com/docs/voice.xml"
                    )

print(call.sid)
 

