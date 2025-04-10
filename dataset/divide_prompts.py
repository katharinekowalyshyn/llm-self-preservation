# File paths
file_path = "promptsTOT_math.txt"  # The file containing all prompts
output_folder = "MathPrompts"  # Folder where individual prompt files will be saved

# Number of lines per prompt
lines_per_prompt = 10

# Read the input file with all prompts
with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

# Create output folder if it doesn't exist
import os
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Split the lines into chunks of 10 (or the specified number of lines per prompt)
for i in range(0, len(lines), lines_per_prompt):
    prompt_lines = lines[i:i + lines_per_prompt]  # Get the next 10 lines

    # Generate output file path for each prompt
    output_file_path = os.path.join(output_folder, f"math_{(i // lines_per_prompt) + 1}.txt")

    # Write the prompt to the corresponding file
    with open(output_file_path, "w", encoding="utf-8") as f:
        f.writelines(prompt_lines)  # Write the 10 lines as one prompt

    print(f"Prompt {(i // lines_per_prompt) + 1} saved to {output_file_path}")
