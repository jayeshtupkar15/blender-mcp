import bpy
import os

def handle_prompt(prompt):
    print(f"🔍 Handling prompt: {prompt}")

    # --- 1. Generate or map prompt to model path ---
    # Simulate logic here or call your LLM pipeline / downloader
    model_path = f"/absolute/path/to/Assets/Models/{prompt.replace(' ', '_')}.glb"

    if not os.path.exists(model_path):
        print(f"❌ Model not found: {model_path}")
        return

    # --- 2. Load .glb file into Blender ---
    bpy.ops.import_scene.gltf(filepath=model_path)
    print(f"✅ Imported {model_path} into scene.")
