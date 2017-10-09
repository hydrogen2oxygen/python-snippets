import json
from collections import namedtuple

class BlenderObject:
	def __init__(self):
		self.vertex = []
		self.faces = [1,3,4,2,1,4,2]
		self.polygons = [1.3232,0.13244,5.3121,23.2323]
		self.name = 'book'
		self.description = 'testclass'


bObject = BlenderObject()

# Export as JSON
bObjectAsJson = json.dumps(bObject.__dict__, indent=4, sort_keys=True)
print('Type of bObjectAsJson is = ' + str(type(bObjectAsJson)))
print('Object as JSON (bObjectAsJson):\n' + bObjectAsJson)

# Import as dictionary
def _json_object_hook(d): return namedtuple('X', d.keys())(*d.values())
def json2obj(data): return json.loads(data, object_hook=_json_object_hook)
x = json2obj(bObjectAsJson)
print('As a decoded object:',x.name,x.description,x.faces,x.polygons)