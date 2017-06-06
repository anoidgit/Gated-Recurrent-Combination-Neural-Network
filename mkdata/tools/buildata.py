#encoding: utf-8

import sys
import h5py,numpy

from random import shuffle

def shufflepair(srcm1, srcm2):
	bsize=srcm1.shape[0]
	if bsize == 1:
		return srcm1, srcm2
	else:
		rind = [i for i in xrange(bsize)]
		shuffle(rind)
		rsm1 = numpy.zeros(srcm1.shape, dtype=srcm1.dtype)
		rsm2 = numpy.zeros(srcm2.shape, dtype=srcm2.dtype)
		curid = 0
		for ru in rind:
			rsm1[curid] = srcm1[ru]
			rsm2[curid] = srcm2[ru]
			curid+=1
		return rsm1, rsm2

def ldmap(fname):
	rs={}
	curid=1
	with open(fname) as frd:
		for line in frd:
			tmp=line.strip()
			if tmp:
				tmp=tmp.decode("utf-8")
				if not tmp in rs:
					rs[tmp]=curid
					curid+=1
	return rs

def mapline(ld,mapid,maptd,unkid):
	id=[]
	for lu in ld[1:]:
		lu=lu.strip()
		if lu:
			id.append(mapid.get(lu,unkid))
	return id, maptd.get(ld[0])

def handle(srcf,rsif,rstf,splf,mapif,maptf):
	rsif=h5py.File(rsif,"w")
	rstf=h5py.File(rstf,"w")
	curid=1
	mapid=ldmap(mapif)
	maptd=ldmap(maptf)
	unkid=mapid["<unk>"]
	with open(srcf) as frd:
		with open(splf) as spl:
			for line in spl:
				tmp=line.strip()
				if tmp:
					tmp=int(tmp.decode("utf-8"))
					tid=[]
					ttd=[]
					for i in xrange(tmp):
						lini,lint=mapline(frd.readline().strip().decode("utf-8").split(),mapid,maptd,unkid)
						tid.append(lini)
						ttd.append(lint)
					tid=numpy.array(tid,dtype=numpy.int32)
					ttd=numpy.array(ttd,dtype=numpy.int32)
					#tid, ttd=shufflepair(tid,ttd)
					wrtkey=str(curid)
					rsif[wrtkey]=tid.T
					rstf[wrtkey]=ttd
					curid+=1
	rsif.close()
	rstf.close()

if __name__=="__main__":
	handle(sys.argv[1].decode("utf-8"),sys.argv[2].decode("utf-8"),sys.argv[3].decode("utf-8"),sys.argv[4].decode("utf-8"),sys.argv[5].decode("utf-8"),sys.argv[6].decode("utf-8"))
