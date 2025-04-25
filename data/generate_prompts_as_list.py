# Step 1: Read every 10th line
prompts = []
with open("facts/factsall.txt", "r") as file:
    lines = file.readlines()

    for i in range(0, len(lines), 6):
        chunk = lines[i : i + 5]
        prompt = "".join(chunk).strip()
        prompts.append(prompt)

# Step 2: Save as a Python list in a .py file
with open("facts/facts_list.py", "w") as f:
    f.write("prompts = [\n")
    for prompt in prompts:
        f.write(f"    {repr(prompt)},\n")
    f.write("]\n")

