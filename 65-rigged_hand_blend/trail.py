import bpy
import math

# Select the armature
print(bpy.data)
armature = bpy.data.objects['Armature']  # Name of the armature

# Ensure the armature is in pose mode
bpy.context.view_layer.objects.active = armature
bpy.ops.object.mode_set(mode='POSE')

# Access a specific bone in pose mode
pose_bone = armature.pose.bones["Bone"]  # Name of the bone

dir(pose_bone)
# Set the bone location (relative to its parent)
pose_bone.location = ( 0.0, 0.0, 0.5)  # Example coordinates

# Set the bone rotation (Euler angles in radians)
pose_bone.rotation_euler = (math.radians(45), math.radians(30), math.radians(60))  # Example rotation angles

# Update the scene to apply the changes
bpy.context.view_layer.update()
