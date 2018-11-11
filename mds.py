#!/usr/bin/python
import sys
import shutil
import webbrowser
import argparse
import json
insdir='/home/jwhj/test/mdslider/'
rvjs_prefix='file://'+insdir+'reveal.js/'
tpl_name='tpl.html'
def view(rvjs_prefix,fn):
	f=open(tpl_name,'r')
	s=f.read()
	f.close()
	s=s.replace('<!--rvjs-->',rvjs_prefix)
	s=s.split('<!--insert here-->')
	s1=[s[0]]
	f=open(fn,'r')
	s2=f.read()
	f.close()
	s2=s2.split('---\n<!--slide-->')
	s2=s2[1:]
	for s3 in s2:
		s3=s3.split('<!--config-->',maxsplit=1)
		if (len(s3)==1): s3=['']+s3
		attr='data-markdown'
		try:
			conf=json.loads(s3[0])
			if ('html' in conf):
				attr=attr.replace('data-markdown','')
		except:
			pass
		s1.append('<section %s>'%attr)
		s1.append(s3[1])
		s1.append('</section>')
	s1.append(s[1])
	tmpf=fn+'.tmp.html'
	f=open(tmpf,'w')
	f.write('\n'.join(s1))
	f.close()
	webbrowser.open(tmpf)
if __name__=='__main__':
	parser=argparse.ArgumentParser(description='blablabla')
	parser.add_argument('-i',type=str)
	parser.add_argument('-p',action='store_true')
	parser.add_argument('--init',action='store_true')
	args=parser.parse_args()
	if (args.init):
		shutil.copy(insdir+'tpl.html','./tpl.html')
	elif (args.p):
		view(rvjs_prefix,args.i)
