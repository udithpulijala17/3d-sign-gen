import bpy
import math

# Select the armature
armature = bpy.data.objects['Armature']  # Name of the armature

# Ensure the armature is in pose mode
bpy.context.view_layer.objects.active = armature
bpy.ops.object.mode_set(mode='POSE')

# Access the parent bone and its child bones
parent_bone = armature.pose.bones["Bone002"]  # Name of the parent bone
child_bone1 = armature.pose.bones["Bone001"]  # Name of the first child bone
child_bone2 = armature.pose.bones["Bone003"]  # Name of the second child bone

# Set the desired angle between the child bones (in radians)
desired_angle = math.radians(160)  # Example angle

# Calculate the initial angles between the parent and child bones
initial_angle1 = parent_bone.matrix.to_3x3().inverted().normalized().to_euler()[0] - child_bone1.matrix.to_3x3().inverted().normalized().to_euler()[0]
initial_angle2 = parent_bone.matrix.to_3x3().inverted().normalized().to_euler()[0] - child_bone2.matrix.to_3x3().inverted().normalized().to_euler()[0]

# Calculate the difference in angles
angle_diff1 = initial_angle1 - desired_angle
angle_diff2 = initial_angle2 - desired_angle

# Apply the difference to rotate the child bones
child_bone1.rotation_euler[0] -= angle_diff1
child_bone2.rotation_euler[0] -= angle_diff2

# Update the scene to apply the changes
bpy.context.view_layer.update()
