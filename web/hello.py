#from cgi import parse_qs, escape

def hello_world(environ, start_response):
    parameters = environ.get('QUERY_STRING')
    res = ""
    #print(parameters.split('&'))
    for parameter in parameters.split('&'):
        res+=(parameter+'\n')
    #if 'subject' in parameters:
    #    subject = escape(parameters['subject'][0])
    #else:
    #    subject = 'World'
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return [res]
