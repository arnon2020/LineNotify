import requests

class notify:
	def __init__(self, token):
		self.headers =  {'Authorization': 'Bearer ' + token,}
		
	def message(self,msg=' '):
		data = {'message':msg}
		return self._post_(data)

	def file(self,path=' '):
		data = {'message':' '}
		file = {'imageFile': (path, open(path, 'rb')),}
		return self._post_(data,file)

	def sticker(self,stickerID,stickerPackageID):
		data = {'message':" ",'stickerPackageId':stickerPackageID,'stickerId':stickerID}
		return self._post_(data)

	def _post_(self,data,file=None):
		return requests.post('https://notify-api.line.me/api/notify', headers=self.headers,data=data,files=file)


#example
line = notify('line token')
line.message('hello world')
line.file('./images/main.png')
line.sticker(113,1)