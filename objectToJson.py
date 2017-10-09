import json

class BlenderObject:
	def __init__(self):
		self.vertex = []
		self.faces = [1,3,4,2,1,4,2]
		self.polygons = [1.3232,0.13244,5.3121,23.2323]
		self.name = 'book'
		self.description = 'testclass'


bObject = BlenderObject()
bObjectAsJson = json.dumps(bObject.__dict__, indent=4, sort_keys=True)
print(bObject.name)
print('Object as JSON:\n' + bObjectAsJson)