#!/usr/bin/env python
def Max(a,b):
	if a>b:
		print a
	elif a==b:
		print '=='
	else:
		print b

Max(5,5)
def update(*args,**kwargs):
	p=''
	for i,t in kwargs.items():
		p = p+ '%s=%s,' %(i,str(t))
	sql = "update  'user' set (%s) where (%s)" %(args[0],p)
	print sql
update('aaa',uu='uu',id=3)
