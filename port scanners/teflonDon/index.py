import optparse
from socket import *

def connScan(tgtHost, tgtPort):
	tgtPortS = int(tgtPort)
	try: 
		socket = socket(AF_INET, SOCK_STREAM)
		socket.connect((tgtHost, tgtPortS))
		print('TCP Open: ' + str(tgtPortS))
	except:
		print('TCP Closed: ' + str(tgtPortS))

def portScan(tgtHost, tgtPort):
	try:
		tgtIP = gethostbyname(tgtHost)
	except:
		print('Cannot Resolve: Unknow Host: ' + tgtIP)
		return
	try: 
		tgtName = gethostbyaddr(tgtIP)
		print('Scan Results for: ' + tgtName[0])
	except:
		print('Scan Results for: ' + tgtIP)
	setdefaulttimeout(1)
	print('Scanning Port: ' + tgtPort)
	connScan(tgtHost, int(tgtPort))

def main():
	parser=optparse.OptionParser('usage %prog –H '+'<target host> -p <target port>')
	parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
	parser.add_option('-p', dest='tgtPort', type ='int', help='specify target port')
	(options, args) = parser.parse_args()
	tgtHost = options.tgtHost
	tgtPort = options.tgtPort
	if(tgtHost == None) | (tgtPort == None):
		print(parser.usage)
		exit(0)
	portScan(tgtHost, str(tgtPort))
if __name__ == '__main__':
	main()