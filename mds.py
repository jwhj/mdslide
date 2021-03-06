#!/usr/bin/python
import sys
import shutil
import webbrowser
import argparse
import json
#__import__('pdb').set_trace()
insdir='/home/jwhj/test/mdslide/' # replace it with your install directory
#rvjs_prefix='file://'+insdir+'reveal.js/'
rvjs_prefix='http://localhost:4000/'
tpl_name='tpl.html'
def view(rvjs_prefix,fn,flag=1):
	f=open(tpl_name,'r')
	s=f.read()
	f.close()
	s=s.replace('<!--rvjs-->',rvjs_prefix)
	s=s.split('<!--insert here-->')
	s1=[s[0]]
	if (fn is not None):
		f=open(fn,'r')
		s2=f.read()
		f.close()
		s2=s2.replace('/a/raw/b/','')
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
	if (fn is not None):
		tmpf=fn+'.tmp.html'
	else: tmpf='tmp.html'
	f=open(tmpf,'w')
	f.write('\n'.join(s1))
	f.close()
	if (flag): webbrowser.open(tmpf)
if __name__=='__main__':
	parser=argparse.ArgumentParser(description='blablabla')
	parser.add_argument('-i',type=str)
	parser.add_argument('-p',action='store_true')
	parser.add_argument('-e',action='store_true')
	parser.add_argument('--init',action='store_true')
	args=parser.parse_args()
	if (args.init):
		shutil.copy(insdir+'tpl.html','./tpl.html')
	elif (args.p):
		view(rvjs_prefix,args.i)
	elif (args.e):
		epath='./'+args.i+'.e/'
		try:
			shutil.rmtree(epath)
		except:
			pass
		shutil.copytree(insdir+'reveal.js',epath)
		view('',args.i,0)
		shutil.copy(args.i+'.tmp.html',epath)
