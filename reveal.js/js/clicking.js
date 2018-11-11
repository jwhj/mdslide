function go()
{
	a=document.createEvent('HTMLEvents');
	a.initEvent('click',false,true);
	b=document.getElementsByClassName('navigate-down enabled');
	if (b.length) b[0].dispatchEvent(a);
	else
	{
		b=document.getElementsByClassName('navigate-right enabled');
		b[0].dispatchEvent(a);
	}
}
