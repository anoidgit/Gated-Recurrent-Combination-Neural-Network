require "hdf5"

local vsize=300

function ldvec(fsrc,vsize)
	local file=io.open(fsrc)
	local num=file:read("*n")
	local rs={}
	while num do
		table.insert(rs,num)
		num=file:read("*n")
	end
	file:close()
	ts=torch.FloatTensor(rs)
	return ts:reshape(#rs/vsize,vsize)
end

ti=hdf5.open("duse/traini.hdf5","r")
tt=hdf5.open("duse/traint.hdf5","r")
di=hdf5.open("duse/devi.hdf5","r")
dt=hdf5.open("duse/devt.hdf5","r")

ntrain=1236
ndev=299

traind={}
devd={}

for i=ntrain,1,-1 do
	local curid=tostring(i)
	table.insert(traind,{ti:read(curid):all(),tt:read(curid):all()})
end
ti:close()
tt:close()
for i=ndev,1,-1 do
	local curid=tostring(i)
	table.insert(devd,{di:read(curid):all(),dt:read(curid):all()})
end
di:close()
dt:close()
torch.save("p"..vsize.."data.asc",{traind,devd,ldvec("duse/wvec_"..vsize..".txt",vsize)})
--torch.save("data.asc",{traind,devd,torch.randn(21123,50):float()})
