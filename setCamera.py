import sys
import bpy

argv = sys.argv
argv = argv[argv.index("--")+1:]

bpy.context.scene.camera = bpy.data.objects[argv[0]]
