import json
import subprocess

from openai import OpenAI


def get_openai_key_from_bitwarden(field_name="login", item_name="OpenAI API Key"):
    # Get session key (assumes you've already run `bw unlock` and exported BW_SESSION)
    session = subprocess.check_output(["bw", "unlock", "--raw"]).decode("utf-8").strip()

    # Get item by name
    item_json = subprocess.check_output(
        ["bw", "get", "item", item_name, "--session", session]
    ).decode("utf-8")

    item = json.loads(item_json)
    return item["login"]["password"]


# Securely get API key from Bitwarden
api_key = get_openai_key_from_bitwarden()
client = OpenAI(api_key=api_key)

# File paths
# prompt_file_path = "prompt_math.txt"
prompt_file_path = "prompt_dilemma.txt"
response_file_path = "response.txt"

# Read prompt
with open(prompt_file_path, "r", encoding="utf-8") as f:
    prompt = f.read()

# Query OpenAI
response = client.chat.completions.create(
    model="gpt-4o-mini", messages=[{"role": "user", "content": prompt}], temperature=0.7
)


# Save response
reply = response.choices[0].message.content
with open(response_file_path, "w", encoding="utf-8") as f:
    f.write(reply)

print("Response saved to", response_file_path)
