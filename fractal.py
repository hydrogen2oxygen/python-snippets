# Challenge #748 on https://blenderartists.org/forum

import bpy

print('------------------------------------------------')
print('=== Create Hypercube ===')

def delete_scene():
    bpy.ops.object.select_all(action='TOGGLE')
    bpy.ops.object.delete(use_global=True)
    bpy.ops.object.select_all(action='TOGGLE')
    bpy.ops.object.delete(use_global=True)

# Build a Tesseract

# The base of fractals is phi, self-similarity
# https://en.wikipedia.org/wiki/Golden_ratio
phi = 1.6180339887498948482

# The number of iterations (eternity is incomprensible even for a computer)
max_iteration = 7

# First build a simple cube and add wireframe modifier
def create_cube(r,x,y,z,t):
    cube = bpy.ops.mesh.primitive_cube_add(radius=r,location=(x,y,z))
    bpy.ops.object.modifier_add(type='WIREFRAME')
    bpy.context.object.modifiers["Wireframe"].thickness = t
    mat = bpy.data.materials.get("Emission")
    ob = bpy.context.active_object
    ob.data.materials.append(mat)

# Second build a hypercube (tesseract) represented as a fractal construct in our 3D space
def create_hypercube(r,x,y,z,iteration):
    
    if iteration >= max_iteration:
        return
    
    print('iteration = ', iteration)

    thickness_factor = 100    
    t = r / thickness_factor
    
    create_cube(r,x,y,z,t)

    # the golden ratio injects order
    inner_radius = r / phi
    print('inner_radius = ', inner_radius)
    t2 = inner_radius / thickness_factor
    
    # here occurs self-similarity in form of a recursive function (a function calls itself)
    iteration += 1
    create_hypercube(inner_radius,x,y,z,iteration)

    inner_radius2 = (inner_radius / phi) / 2
    # Note that both inner_radius 1 and 2 equals original radius
    print('inner_radius2 = ', inner_radius2)
    print('inner_radius + inner_radius2 = ', (inner_radius + inner_radius2))
    t3 = inner_radius2 / thickness_factor
    
    x2 = inner_radius + inner_radius2
    inner_radius3 = inner_radius2 / phi
    iteration += 1
    
    if iteration < 4:
        create_cube(inner_radius2,x2,x2,x2,t3)
        create_cube(inner_radius2,-x2,x2,x2,t3)
        create_cube(inner_radius2,x2,-x2,x2,t3)
        create_cube(inner_radius2,-x2,-x2,x2,t3)
    
    create_hypercube(inner_radius3,x2,x2,x2,iteration)
    create_hypercube(inner_radius3,-x2,x2,x2,iteration)
    create_hypercube(inner_radius3,x2,-x2,x2,iteration)
    create_hypercube(inner_radius3,-x2,-x2,x2,iteration)

    if iteration < 4:
        create_cube(inner_radius2,x2,x2,-x2,t3)
        create_cube(inner_radius2,-x2,x2,-x2,t3)
        create_cube(inner_radius2,x2,-x2,-x2,t3)
        create_cube(inner_radius2,-x2,-x2,-x2,t3)
    
    create_hypercube(inner_radius3,x2,x2,-x2,iteration)
    create_hypercube(inner_radius3,-x2,x2,-x2,iteration)
    create_hypercube(inner_radius3,x2,-x2,-x2,iteration)
    create_hypercube(inner_radius3,-x2,-x2,-x2,iteration)
    
    
delete_scene()
create_hypercube(5,0,0,0,1)

bpy.ops.object.select_all(action='TOGGLE')
bpy.ops.object.select_all(action='TOGGLE')
bpy.ops.object.parent_set(type='OBJECT', keep_transform=False)
