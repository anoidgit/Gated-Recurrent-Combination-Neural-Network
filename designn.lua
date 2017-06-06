require "nn"
require "cutorch"
require "cunn"
require "cudnn"

local function getonn()
	require "nn"
	require "nn.Decorator"
	require "dpnn"
	require "models.gru"
	wvec = nil
	local lmod = torch.load(cntrain).modules[1]
	return lmod
end

local function getnnn()

	local buildM=require "models.grcnn"
	return buildM(18, nil, nil, true)
end

function getnn()
	if cntrain then
		return getonn()
	else
		return getnnn()
	end
end

function getcrit()
	return nn.MultiMarginCriterion();
end
