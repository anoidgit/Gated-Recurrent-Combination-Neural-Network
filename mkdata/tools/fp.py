#encoding: utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

def handle(srcf, ansf):
	sum=0
	match=0
	with open(srcf) as frdg:
		with open(ansf) as frda:
			for g, a in zip(frdg, frda):
				g=g.strip()
				a=a.strip()
				if g and a:
					g=g.decode("utf-8")
					a=a.decode("utf-8")
					a=a[:a.find(" ")]
					g=g[9:]
					if g == a:
						match+=1
					sum+=1
	print(float(match)/sum)

if __name__=="__main__":
	handle(sys.argv[1].decode("utf-8"),sys.argv[2].decode("utf-8"))
