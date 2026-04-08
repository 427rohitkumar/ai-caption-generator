import requests
from app.config.settings import NVIDIA_API_KEY

API_URL = "https://integrate.api.nvidia.com/v1/chat/completions"


def generate_content(context):

    prompt = f"""
Analyze the provided context and generate optimized social media content for multiple platforms.

[CONTEXT]
{context}

---

[OUTPUT FORMAT]

🎥 YOUTUBE:
- Title: A viral, high-CTR title.
- SEO Description: A detailed description including keywords.

📸 INSTAGRAM / FACEBOOK:
- Caption: Engaging, emoji-rich caption.
- Hashtags: 15 trending and relevant hashtags.

💼 LINKEDIN:
- Post: A professional, insightful post suitable for a professional network.

---
Ensure the tone is appropriate for each platform. If it's a local business, focus on community and services. If it's educational, focus on value.
"""

    response = requests.post(
        API_URL,
        headers={
            "Authorization": f"Bearer {NVIDIA_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "meta/llama3-70b-instruct",
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.7,
            "max_tokens": 1024
        }
    )

    # 🔥 DEBUG START
    print("\n===== NVIDIA DEBUG =====")
    print("STATUS:", response.status_code)
    print("RAW RESPONSE:", response.text)
    print("========================\n")
    # 🔥 DEBUG END

    if response.status_code != 200:
        raise Exception("NVIDIA API FAILED")

    data = response.json()

    # Extract actual text output
    return data["choices"][0]["message"]["content"]