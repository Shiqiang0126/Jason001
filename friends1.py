#friends1.py @shiqiang oct.29
import cgi
reshtml='''Content-type:text/html\n
<HTML><HEAD><TITLE>
Friends CGI Demo (Dynamic screen)
</TITLE></HEAD>
<BODY><H3>Friends list for:<I>%s</I></H3>
Your name is:<B>%s</B><P>
You have <B>%s</B> friends.
</BODY></HTML> '''

form=cgi.FieldStorage()
who=form['person'].value
howmany=form['howmanu'].value
print (reshtml % (who,who,howmany))