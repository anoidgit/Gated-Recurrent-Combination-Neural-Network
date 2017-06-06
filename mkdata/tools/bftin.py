#encoding: utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

def handle(srcf, rsf):
	with open(srcf) as frd:
		with open(rsf, "w") as fwrt:
			for line in frd:
				tmp=line.strip()
				if tmp:
					tmp=tmp.decode("utf-8")
					tmp=tmp.split()
					tmp=" ".join(tmp[1:])
					fwrt.write(tmp.encode("utf-8"))
					fwrt.write("\n")

if __name__=="__main__":
	handle(sys.argv[1].decode("utf-8"),sys.argv[2].decode("utf-8"))
