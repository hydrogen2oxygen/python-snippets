import bpy, json
from collections import namedtuple
from mathutils import Matrix

filepath = bpy.path.abspath("//")

# Import as dictionary
def _json_object_hook(d): return namedtuple('X', d.keys())(*d.values())
def json2obj(data): return json.loads(data, object_hook=_json_object_hook)

with open(filepath + '/export_book.json', 'r') as bookFile:
    bookData=bookFile.read()

importedData = json2obj(bookData)
print('As a decoded object:',importedData.name, importedData.vertices, importedData.polygons)

#creating object in blender
name = 'test'
bMesh = bpy.data.meshes.new(name)
bObject = bpy.data.objects.new(name, bMesh)
scn = bpy.context.scene
scn.objects.link(bObject)	
scn.objects.active = bObject
bObject.select = True

# insert vertices and faces into the new object
bMesh.from_pydata(importedData.vertices, [], importedData.polygons)
bMesh.update(calc_edges=True)