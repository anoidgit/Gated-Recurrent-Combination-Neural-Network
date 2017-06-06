require "cutorch"

local DataContainer = torch.class('DataContainer')

function DataContainer:__init(dset, ndata)
	self.dset = dset
	self.ndata = ndata or #dset
end

local function iter(dset, curid)
	curid = curid + 1
	local data = dset[curid]
	if data then
		return curid, unpack(data)
	else
		return
	end
end

function DataContainer:subiter()
	return iter, self.dset, 0
end
