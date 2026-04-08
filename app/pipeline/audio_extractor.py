import ffmpeg

def extract_audio(video_path, out="app/outputs/audio/audio.wav"):
    (
        ffmpeg
        .input(video_path)
        .output(out)
        .run(overwrite_output=True)
    )
    return out