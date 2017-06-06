starterate=math.huge--warning:only used as init erate, not asigned to criterion

runid="170606_grcnnstd_pembd_50"
--runid="debug"
logd="logs"

ieps=1
warmcycle=0
expdecaycycle=1
gtraincycle=32

modlr=1/8192--1024

earlystop=gtraincycle

csave=3

lrdecaycycle=1

recyclemem=0.05

storedebug=true--store model every epoch or not

cntrain=nil--"modrs/"..runid.."/devnnmod3.asc"

partrain=20000

if cntrain then
	warmcycle=0
end
