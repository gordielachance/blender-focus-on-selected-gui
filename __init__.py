bl_info = {
    "name": "Focus on Selected (GUI)",
    "author": "Benoît G.",
    "version": (1, 1, 0),
    "blender": (4, 2, 0),
    "location": "3D Viewport header, Outliner header",
    "description": (
        "Adds buttons to frame/reveal selected objects in the 3D Viewport and in the Outliner.  Emulates the Numpad Period (.) shortcut."
    ),
    "category": "Interface",
}
import bpy
class VIEW3D_OT_frame_selected_button(bpy.types.Operator):
    """Frame selected objects in the 3D viewport"""
    bl_idname = "view3d.frame_selected_button"
    bl_label = "Focus on Selected"
    bl_options = {'REGISTER', 'UNDO'}
    def execute(self, context):
        bpy.ops.view3d.view_selected()
        return {'FINISHED'}
class OUTLINER_OT_reveal_selected_button(bpy.types.Operator):
    """Scroll to and reveal the active item in the outliner"""
    bl_idname = "outliner.reveal_selected_button"
    bl_label = "Focus on Active"
    bl_options = {'REGISTER', 'UNDO'}
    def execute(self, context):
        bpy.ops.outliner.show_active()
        return {'FINISHED'}
def draw_viewport_button(self, context):
    """Draw button in 3D viewport header"""
    self.layout.operator("view3d.frame_selected_button", text="", icon='PIVOT_BOUNDBOX')
def draw_outliner_button(self, context):
    """Draw button in outliner header"""
    self.layout.separator()
    self.layout.operator("outliner.reveal_selected_button", text="", icon='PIVOT_BOUNDBOX')
classes = (
    VIEW3D_OT_frame_selected_button,
    OUTLINER_OT_reveal_selected_button,
)
def refresh_ui():
    """Refresh all UI areas"""
    for window in bpy.context.window_manager.windows:
        for area in window.screen.areas:
            area.tag_redraw()
def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.VIEW3D_HT_header.append(draw_viewport_button)
    bpy.types.OUTLINER_HT_header.append(draw_outliner_button)
    refresh_ui()
def unregister():
    bpy.types.VIEW3D_HT_header.remove(draw_viewport_button)
    bpy.types.OUTLINER_HT_header.remove(draw_outliner_button)
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    refresh_ui()
if __name__ == "__main__":
    register()
