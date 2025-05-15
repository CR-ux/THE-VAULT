import os
import re
from pathlib import Path
from datetime import datetime, timedelta
from collections import defaultdict

# === CONFIGURATION ===
VAULT_PATH = Path("~/Library/Mobile Documents/iCloud~md~obsidian/Documents/").expanduser()
LEXDICT_PATH = VAULT_PATH / "lexDict.md"
DAYS_BACK = 7

# === SETUP ===
link_pattern = re.compile(r"\[\[([^\[\]|]+)")
cutoff_time = datetime.now() - timedelta(days=DAYS_BACK)
alpha_sections = defaultdict(set)  # Dict of { 'A': set([entries...]), etc. }

# === STEP 1: Find all [[links]] from recently edited files ===
# STEP 1: Find all [[links]] from recently edited files
for file in VAULT_PATH.rglob("*.md"):
    if file == LEXDICT_PATH or file.is_dir():
        continue
    if datetime.fromtimestamp(file.stat().st_mtime) < cutoff_time:
        continue

    with open(file, "r", encoding="utf-8") as f:
        matches = link_pattern.findall(f.read())
        for word in matches:
            first_letter = word[0].upper()
            if not first_letter.isalpha():
                first_letter = "{"  # Non-alpha symbols
            alpha_sections[first_letter].add(word.strip())
# === STEP 2: Load current lexDict ===
with open(LEXDICT_PATH, "r", encoding="utf-8") as f:
    lines = f.readlines()

# === STEP 3: Process line-by-line and inject sorted entries ===
output_lines = []
current_letter = None
collected_section = []

for line in lines:
    match = re.match(r"^## (\w|\{) is for...", line)
    if match:
        # Splice previous section if needed
        if current_letter and current_letter in alpha_sections:
            # Extract existing entries
            existing = set(re.findall(r"\[\[(.*?)\]\]", ''.join(collected_section)))
            to_add = sorted(alpha_sections[current_letter] - existing)
            for term in to_add:
                collected_section.append(f"[[{term}]]\n")
            alpha_sections.pop(current_letter)  # We've handled this letter
        output_lines.extend(collected_section)
        collected_section = []
        current_letter = match.group(1)
    if current_letter:
        collected_section.append(line)
    else:
        output_lines.append(line)

# Final section
if current_letter and current_letter in alpha_sections:
    existing = set(re.findall(r"\[\[(.*?)\]\]", ''.join(collected_section)))
    to_add = sorted(alpha_sections[current_letter] - existing)
    for term in to_add:
        collected_section.append(f"[[{term}]]\n")
    alpha_sections.pop(current_letter)

output_lines.extend(collected_section)

# === STEP 4: Write back to file ===
with open(LEXDICT_PATH, "w", encoding="utf-8") as f:
    f.writelines(output_lines)

print("✅ lexDict updated alphabetically with new [[entries]] from recent files.")
