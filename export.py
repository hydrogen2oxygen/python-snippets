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
            new_matrix = []
            old_matrix = list(ob.matrix_world)
            for line in old_matrix:
                vector = []
                vector.append(line[0])
                vector.append(line[1])
                vector.append(line[2])
                new_matrix.append(vector)
            return new_matrix

def create_object(ob, i, bObjectsArray):
    bObject = BlenderObject()
    bObject.name = str(ob.name)
    
    vert_coords = [(ob.matrix_world * v.co) for v in ob.data.vertices]
    for c in vert_coords:
        vertex = []
        vertex.append(c[0])
        vertex.append(c[1])
        vertex.append(c[2])
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
print('Exporting finished!')