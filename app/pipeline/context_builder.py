def build_context(captions, transcript="N/A"):
    """Aggregates visual and auditory information."""
    return f"""
[Visual Content - Image Analysis]
{' | '.join(captions)}

[Auditory Content - Transcript]
{transcript if transcript else 'No audio/transcript available for this file.'}
"""