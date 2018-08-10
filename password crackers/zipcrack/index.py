import zipfile;
import optparse;

def crack(zFile, dictionary):
	dic = open(dictionary)
	zFile = zipfile.ZipFile(zFile)
	for line in dic.readlines():
		try:
			zFile.extractall(pwd=str.encode(line))
			print('Password FOUND: ' + line)	
		except Exception as e:
			print('///[+] Bas Password: ' + line)
		
def main():
	parser = optparse.OptionParser("usage%prog " + "-f <zipfile> -d <dictionary>")
	parser.add_option('-f', dest = 'zname', type = 'string',help = 'specify zip file')
	parser.add_option('-d', dest = 'dname', type = 'string', help = 'specify dictionary file')
	(options, args) = parser.parse_args()
	if (options.zname == None) | (options.dname == None):
		print(parser.usage)
		exit(0)
	else:
		zname = options.zname
		dname = options.dname

	crack(zname, dname)
if __name__ == '__main__':
	main()