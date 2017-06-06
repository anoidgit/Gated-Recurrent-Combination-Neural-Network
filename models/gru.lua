require "nn"
require "cudnn"
require "deps.vecLookup"

return function (nclass, nlayer,pdrop)
	return nn.Sequential()
		:add(nn.vecLookup(wvec))
		:add(cudnn.GRU(wvec:size(2), wvec:size(2), nlayer or 1,nil, pdrop))
		:add(nn.Select(1, -1))
		:add(nn.Linear(wvec:size(2), nclass))
end
