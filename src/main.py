import bpy

filepath = "C:\\Users\\dachu\\AppData\\Roaming\\.minecraft\\replay_videos\\DDMSG30_A.glb"

# Import File
bpy.ops.import_scene.gltf(filepath=filepath, files=[{"name": "DDMSG30_A.glb", "name": "DDMSG30_A.glb"}], loglevel=50)
camera = bpy.context.active_object
# Copy Animation
bpy.ops.action.copy()

# Add Sphere
bpy.ops.mesh.primitive_uv_sphere_add(radius=1, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
sphere = bpy.context.active_object
# Add Key Frame
# Past Animation
bpy.ops.action.paste()

