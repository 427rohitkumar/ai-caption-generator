import os
from datetime import datetime

from app.pipeline.orchestrator import run_pipeline


# ✅ VALIDATE INPUT (Video or Image)
def validate_input(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")

    valid_extensions = (".mp4", ".mov", ".avi", ".mkv", ".jpg", ".jpeg", ".png", ".webp")
    if not path.lower().endswith(valid_extensions):
        raise ValueError(f"Unsupported format. please use: {', '.join(valid_extensions)}")


# ✅ SAVE OUTPUT AS TEXT FILE
def save_output(result_text, output_dir="app/outputs/results"):
    os.makedirs(output_dir, exist_ok=True)

    file_name = f"result_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    file_path = os.path.join(output_dir, file_name)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(result_text)

    return file_path


# ✅ MAIN PROCESS
def process_content(input_path):
    print("\n[1] Validating input...")
    validate_input(input_path)

    print("[2] Running AI pipeline...")
    result_text = run_pipeline(input_path)

    print("[3] Saving output...")
    saved_path = save_output(result_text)

    print("\n✅ DONE")
    print(f"Saved at: {saved_path}")

    return result_text


# 🔥 ENTRY POINT
if __name__ == "__main__":
    video_path = input("Enter video path: ").strip()

    try:
        process_video(video_path)

    except Exception as e:
        print(f"\n❌ ERROR: {str(e)}")