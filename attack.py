import requests
import time
import base64
import MySQLdb
s = requests.Session()
flags=[]


conn = MySQLdb.connect(
    host="172.25.2.2",
    user="redcadet",
    passwd="secretpass",
    db="redcadet",
)

query = 'SELECT id, username, money FROM users WHERE id=%s'
curs = conn.cursor()
curs.execute(query, "1")
def decode_base32(encoded_data):
    padding = len(encoded_data) % 8
    if padding != 0:
        encoded_data += '=' * (8 - padding)
    decoded_data = base64.b32decode(encoded_data)
    return decoded_data.decode()


encoded_method = base64.b32encode(b"a_item_list")

addr='http://172.25.16.2:7000'
r = requests.request(method=encoded_method.decode('utf-8'), url=addr+'/register/' )
text=r.text
print(text)
