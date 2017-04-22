import cgi
formular = cgi.FieldStorage()
name = formular.getfirst('name')
bid = formular.getvalue('bid')
