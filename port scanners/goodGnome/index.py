import optparse
from socket import *
def connScan(tgtHost, tgtPort):
	try:
		connSkt = socket(AF_INET, SOCK_STREAM)
		result = connSkt.connect((str(tgtHost), int(tgtPort)))
		if result == None:
			connSkt.send(b'Hello\r\n')
			results = connSkt.recv(100)
			print('Results: ' + str(results))
			print('tcp open: ' + str(tgtPort))
			return
		print('tcp closed: ' + str(tgtPort))
	except:
		print('tcp closed: ' + str(tgtPort))

def portScan(tgtHost, tgtPort):
	try:
		tgtIP = gethostbyname(tgtHost)
	except:
		print('Cannot Resolve: Unknow Host: ' + tgtHost)
		return
	try:
		tgtName = gethostbyaddr(tgtIP)
		print('Scan Results for: ' + tgtName[0])
	except:
		print('Scan Results for: ' + tgtIP)
	setdefaulttimeout(1)
	print('Scanning Port: ' + str(tgtPort))
	connScan(tgtHost, int(tgtPort))

def main():
	parser = optparse.OptionParser('usage %prog -H ' + '<target host>' + '-p ' + '<port>')
	parser.add_option('-H', dest='tgtHost', type="string", help="Specify Target Host")
	parser.add_option('-p', dest='tgtPort', type="int", help="Specify Target Port")		
	(options, args) = parser.parse_args()
	tgtHost = options.tgtHost
	tgtPort = options.tgtPort
	#if(tgtPort == None | tgtHost == None):
	#	print(parser.usage)
	portScan(tgtHost, tgtPort)
if __name__ == '__main__':
		main()
