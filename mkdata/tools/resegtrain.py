#encoding: utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from pynlpir import nlpir

def segline(strin):
	try:
		rs=nlpir.ParagraphProcess(strin.encode("utf-8","ignore"), 0)
	except:
		rs=""
	return rs.decode("utf-8","ignore")

def filine(tmp):
	rs=[]
	for tmpu in tmp:
		tt=tmpu.strip()
		if tt:
			rs.append(tt)
	return "".join(rs)

def handle(srcf, rsf):
	with open(srcf) as frd:
		with open(rsf, "w") as fwrt:
			for line in frd:
				tmp=line.strip()
				if tmp:
					tmp=tmp.decode("utf-8")
					tmp=tmp.split()
					rs=[tmp[0]]
					rs.extend(segline(filine(tmp[1:])).split())
					tmp=[]
					for tmpu in rs:
						tt=tmpu.strip()
						if tt:
							tmp.append(tt)
					rs=" ".join(tmp)
					fwrt.write(rs.encode("utf-8"))
					fwrt.write("\n")

if __name__=="__main__":
	nlpir.Init(nlpir.PACKAGE_DIR,nlpir.UTF8_CODE,None)
	handle(sys.argv[1].decode("utf-8"),sys.argv[2].decode("utf-8"))
	nlpir.Exit()
