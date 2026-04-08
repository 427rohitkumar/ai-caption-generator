import os
from .frame_extractor import extract_frames
from .audio_extractor import extract_audio
from .caption_generator import generate_captions
from .speech_to_text import transcribe_audio
from .context_builder import build_context
from .llm_nvidia import generate_content

def cleanup(frames, audio_path, original_input):
    """Removes temporary frames and audio files, but keeps the original input."""
    print("\n[4] Cleaning up temporary files...")
    
    # Remove frames
    for f in frames:
        # DO NOT remove if it is the original input file
        if f != original_input and os.path.exists(f):
            os.remove(f)
            
    # Remove audio
    if audio_path and os.path.exists(audio_path):
        os.remove(audio_path)
    
    print("✅ Cleanup complete")

def run_pipeline(input_path):
    frames = []
    audio = ""
    
    # Check if input is an image
    is_image = input_path.lower().endswith((".jpg", ".jpeg", ".png", ".webp"))
    
    try:
        if is_image:
            print("📸 Mode: Image Detected")
            frames = [input_path]
            transcript = "No audio available (Statical Image)"
        else:
            print("🎥 Mode: Video Detected")
            frames = extract_frames(input_path)
            audio = extract_audio(input_path)
            transcript = transcribe_audio(audio)

        captions = generate_captions(frames)
        context = build_context(captions, transcript)

        result = generate_content(context)
        return result

    finally:
        cleanup(frames, audio, input_path)