import nmap # This library doesn't works right
import optparse

def nmapScan(host, port):
	nScan = nmap.PortScanner()
	nScan.scan(host, port)
	state = nScan[host]['tcp'][int(port)]['state']
	print('[*]' + ' ' + host + ' tcp/' + port + ' ' + state)

def main():
	parser = optparse.OptionParser('usage%prog' + '-H <host>' + '-p <port>')

	parser.add_option('-H', dest='host', type="string", help="Specify Host")
	parser.add_option('-p', dest='port', type="string", help="Specify Port")

	(options, args) = parser.parse_args()

	host = options.host
	ports = str(options.port).split(',')

	#if (host == None | ports[0] == None):
	#	print(parser.usage)
	#	exit(0)
	for port in ports:
		nmapScan(host, port)
if __name__ == '__main__':
	main()		

