#encoding: utf-8

import sys

def handle(srcf,rsif,rstf,kfreq):
	fid={}
	ts=set()
	with open(srcf) as frd:
		for line in frd:
			tmp=line.strip()
			if tmp:
				tmp=tmp.decode("utf-8").split()
				for tmpu in tmp[1:]:
					tt=tmpu.strip()
					if tt:
						fid[tt]=fid.get(tt,0)+1
				tmp=tmp[0]
				if not tmp in ts:
					ts.add(tmp)
	tmp=["<unk>"]
	for k, v in fid.iteritems():
		if v>kfreq:
			k=k.strip()
			if k:
				tmp.append(k)
	print("get:"+str(len(tmp))+" words")
	with open(rsif,"w") as fwrt:
		tmp="\n".join(tmp)
		fwrt.write(tmp.encode("utf-8"))
	with open(rstf,"w") as fwrt:
		tmp="\n".join(ts)
		fwrt.write(tmp.encode("utf-8"))

if __name__=="__main__":
	handle(sys.argv[1].decode("utf-8"),sys.argv[2].decode("utf-8"),sys.argv[3].decode("utf-8"),int(sys.argv[4].decode("utf-8")))
