import itchat
import re
from urllib import request,parse

def Robot(content,toUser):
    api='http://www.tuling123.com/openapi/api'
    apikey='db33db678c254e33abc877db64548fb6'
    data=parse.urlencode([('key',apikey),('info',content),('userid',toUser)])
    req=request.Request(api)
    response=request.urlopen(req,data.encode('utf-8'))
    answer=response.read().decode('utf-8')
    results=re.findall('"text":"(.*?)"',answer)
    for result in results:
        return result

@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
	friend=itchat.search_friends(userName=msg['FromUserName'])
	print(friend['NickName']+':'+msg['Text'])
	text_send(msg)

def text_send(msg):
	global words
	text=Robot(msg['Text'],msg['FromUserName'])
	text=text+'\n'+'('+words+')'
	print('Sundae:'+text)
	itchat.send(text, msg['FromUserName'])

words=input('请输入备注留言：')	
itchat.auto_login(hotReload=True)
itchat.run(debug=True)
