from bottle import route, run, template, response
import json
import psutil
import socket

@route('/health')

def health(): 
    data = {socket.gethostname():[{'RAM':psutil.virtual_memory()._asdict()},{'CPU':psutil.cpu_stats()._asdict()}]}
    response.content_type = 'application/json'
    return json.dumps(data, indent=4)

run(host='localhost', port=8080)
