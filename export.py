import bpy, json
from collections import namedtuple

filepath = bpy.path.abspath("//")

class BlenderObject:
    def __init__(self):
        self.name = ''
        self.vertices = []
        self.polygons = []
        self.transformation = ''
    
def find_transformation(ob):    
    if ob.type == 'MESH':
            old_matrix = list(ob.matrix_world)
            print (ob.name)
            new_matrix = ''
            for line in old_matrix:
                new_matrix = new_matrix + str(line[0]) + ' ' +  str(line[1]) + ' ' +  str(line[2]) + ' '
            print (new_matrix)
            return new_matrix

def create_object(ob, i, bObjectsArray):
    bObject = BlenderObject()
    bObject.name = str(ob.name)
    
    vert_coords = [(ob.matrix_world * v.co) for v in ob.data.vertices]
    for c in vert_coords:
        vertex = str(c[0]) + ',' + str(c[1]) + ',' + str(c[2])
        bObject.vertices.append(vertex)

    poly_coords = [(p.vertices[:]) for p in ob.data.polygons]
    for c in poly_coords:
        polygon = []
        polygon.append(c[0])
        polygon.append(c[1])
        polygon.append(c[2])
        bObject.polygons.append(polygon)

    new_matrix = find_transformation(ob)
    bObject.transformation = str(new_matrix)
    bObjectsArray.append(bObject)
    
    
def create_ObjectsArray():
    scene = bpy.context.scene

    bObjectsArray = []

    i = 1
    for ob in scene.objects:
        if ob.type == 'MESH':
            create_object(ob, i, bObjectsArray)
            i = i + 1

    return bObjectsArray

bObjectsArray = create_ObjectsArray()

# Export as JSON
for bObject in bObjectsArray:
    f = open(filepath + '/export_' + bObject.name + '.json', 'w')
    bObjectAsJson = json.dumps(bObject.__dict__, indent=4, sort_keys=True)
    f.write(bObjectAsJson)
    f.close()
    #print('Type of bObjectAsJson is = ' + str(type(bObjectAsJson)))
    #print('Object as JSON (bObjectAsJson):\n' + bObjectAsJson)
