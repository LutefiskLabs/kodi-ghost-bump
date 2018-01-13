#
#	Module:	bumpme.py
#
#	key authentication module to be run on ghost worker machines.
#
#	lutefisk	1.13.2018  accessing with SSH keys
#
from bottle import route, run, template
import json


config_file = open( 'config.json' )
config_data = json.load( config_file )


@route('/dump')
def config_dump():
    return template('<b>Config data {{cc}}</b>!', cc=config_data)

@route('/echo/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

run(host='0.0.0.0' , port=8085)
