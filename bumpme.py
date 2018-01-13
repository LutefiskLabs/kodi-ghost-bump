#
#	Module:	bumpme.py
#
#	key authentication module to be run on ghost worker machines.
#
#	lutefisk	1.13.2018  accessing with SSH keys
#
from bottle import route, run, template

@route('/echo/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

run(host='0.0.0.0' , port=8085)
