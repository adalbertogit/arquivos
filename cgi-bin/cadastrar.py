#!/usr/bin/python

import cgi, cgitb 

form = cgi.FieldStorage() 


nome = form.getvalue('nome')
telefone  = form.getvalue('telefone')
matricula  = form.getvalue('matricula')
curso = form.getvalue('curso')

print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>Hello - Second CGI Program</title>"
print "</head>"
print "<body>"
print "<h2>Hello %s %s</h2>" % (first_name, last_name)
print "</body>"
print "</html>"
"""tirar este corpo de texto e implementar com o cgi e banco de dados"""