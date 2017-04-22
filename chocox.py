import cgi

print "Content-Type: text/html"     # HTML is following
print                               # blank line, end of headers

print "<TITLE>CGI script output</TITLE>"
print "<body>\n"
print "<H1>This is my first CGI script</H1>"
print "Hello, world!"

form = cgi.FieldStorage()
if "name" not in form:
    print "<H1>Error</H1>"
    print "Please fill in the name fields"
else:
    print "<p>name:", form["name"].value
print "</body>"
