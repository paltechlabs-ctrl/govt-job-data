import openai
import json
from datetime import datetime

# ✅ Your actual API key
openai.api_key = "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"

def summarize_job(text):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": f"""
Summarize this government job post. Extract:
- Job Title
- Department
- Qualification
- Last Date to Apply

Return result in JSON format:
{{"title": "...", "department": "...", "qualification": "...", "last_date": "YYYY-MM-DD"}}

Job Post:
{text}
"""
            }
        ],
        temperature=0.3,
        max_tokens=200
    )
    return response.choices[0].message.content

# Example job post
job_posts = [
    {
        "source": "SarkariResult",
        "link": "https://www.sarkariresult.com/job123",
        "posted_date": str(datetime.today().date()),
        "content": """
SSC CGL 2025 Notification Released.
Apply online for Group B and Group C posts.
Eligibility: Graduate candidates.
Last date to apply: 15 September 2025.
Apply at: https://ssc.nic.in
"""
    }
]

results = []

for job in job_posts:
    try:
        summary = summarize_job(job["content"])
        summary_data = json.loads(summary)
        job.update(summary_data)
        results.append(job)
    except Exception as e:
        print("Error summarizing job:", e)

# Save to jobs.json
with open("jobs.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

print("✅ jobs.json file created successfully.")
