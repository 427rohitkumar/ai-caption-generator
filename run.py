from app.pipeline.orchestrator import run_pipeline
from app.main import save_output

video_path = "media/DhanmantiGeneralStore.png"

result = run_pipeline(video_path)
output_path = save_output(result)

print(f"Output saved to: {output_path}")