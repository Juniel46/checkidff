import requests
import json

_banner_ = '''
   +=+=+=+=+=+=+=+=+=+=+=+=+=+=+
  +++=== GET Nickname FF ===+++   
 ++== Tools Get Nickname FF ==++
+= Check Nickname Free Fire Via ID =+
+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=

# author : JC0D3
# contact: junieldamal46@gmail.com
'''
id = raw_input('username/email: ')
get = requests.get('https://validation.warriors-media.id/trueid/freefire/?id='+id+'&token=JC0D3')

up = get.content
print(up)
# pu = json.loads(up)
# if "session_key" in up:
#    print
#    print _banner_
#    print 'username:' + pu['identifier']
#    print 'token:' + pu["access_token"]
#    open(user+'-token.txt', 'a').write(pu["access_token"])
#    print
#    print 'saved file to '+user+'-token.txt'
# else:
#    print 'maaf username/password salah'