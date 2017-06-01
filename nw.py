from bottle import route, run, template, post, get, request
from cryptlib import encrypt, decrypt

@get('/')
def index():
	return '''
		<h1> COMPUTER PROGRAMMING FINAL PROJECT </H1>
		<form action="/crypt" method="POST" >
			message: <input name="message" type="text">
			<br>
			key: <input name="key" type="text">
			<br>
			Would you like to encrypt or decrypt?
			<select name="ct">
				<option value="encrypt">Encrypt</option>
				<option value="decrypt">Decrypt</option>
			</select><br>
			<input type="submit" name="submit" value="Go">
		</form>
		'''

@post('/crypt')
def do_crypt():
	message = request.forms.get('message')
	key = request.forms.get('key')
	ct = request.forms.get('ct')
	if ct == 'encrypt':
		return encrypt(message,key)
	elif ct == 'decrypt':
		return decrypt (message,key)
	elif key or message == '':
		return '<p>You either did not fill in the message or the key. Please try again.<p>'
	elif key and message == '':
		return '<p>You did not fill in anything. Please try again.<p>'


run(host='localhost', port=8070)
