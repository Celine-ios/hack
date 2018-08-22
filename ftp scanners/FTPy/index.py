import ftplib
def anonLogin(host):
	try:
		ftp = ftplib.FTP(host)
		ftp.login('anonymous', 'me@you.com')
		print(host + ' FTP Anonymous Login Succeeded')
		ftp.quit()
		return True
	except Exception as e:
		print(host + ' FTP Login Failed')
		print(e)
		return False
host = '127.0.0.1'
anonLogin(host)