# (c) 2005 Ian Bicking and contributors; written for Paste (http://pythonpaste.org)
# Licensed under the MIT license: http://www.opensource.org/licenses/mit-license.php

def dump_environ(environ, start_response):
    """
    Application which simply dumps the current environment
    variables out as a plain text response.
    """
    output = []
    keys = environ.keys()
    keys.sort()
    for k in keys:
        v = str(environ[k]).replace("\n","\n    ")
        output.append("%s: %s\n" % (k, v))
    output.append("\n")
    content_length = environ.get("CONTENT_LENGTH", '')
    if content_length:
        output.append(environ['wsgi.input'].read(int(content_length)))
        output.append("\n")
    output = "".join(output)
    headers = [('Content-Type', 'text/plain'),
               ('Content-Length', str(len(output)))]
    start_response("200 OK", headers)
    return [output]
