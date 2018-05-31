default : local_search
	
.PHONY : local_search
local_search :
	python localsearch.py ${file} ${neighbors}
