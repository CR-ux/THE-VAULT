import os
import json
import re

# Vault location
VAULT_PATH = "/Users/callierosepetal/vaults/notBorges-backup"

# Updated regex to catch usage:: or lexAllele(s)::: — case-insensitive, up to `<` if present
LEXDEF_PATTERN = re.compile(
    r'lexDef\s+"?([^"]+)"?\s+\{[^}]*?(?:usage|lexAllele\(s\))\s*:::\s*([^<\n\r]+)',
    re.IGNORECASE
)

EXIT_PATTERN = re.compile(r'\[\[([^\]]+)\]\]')

index = {}

for root, _, files in os.walk(VAULT_PATH):
    for file in files:
        if file.endswith(".md"):
            file_path = os.path.join(root, file)
            rel_path = os.path.relpath(file_path, VAULT_PATH)
            
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Parse lexDefs
                lexdefs = []
                for match in LEXDEF_PATTERN.finditer(content):
                    term = match.group(1).strip()
                    usage_raw = match.group(2).strip()
                    # Split on || or | and clean
                    usages = [u.strip() for u in re.split(r'\|\|?', usage_raw) if u.strip()]
                    lexdefs.append({
                        "term": term,
                        "usages": usages
                    })

                # Parse exits
                exits = list(set(EXIT_PATTERN.findall(content)))

                # Add to index
                index[rel_path] = {
                    "body": content,
                    "lexdefs": lexdefs,
                    "exits": exits
                }

            except Exception as e:
                print(f"Error reading {file_path}: {e}")

# Save output
with open("notBorges_vault_index.json", "w", encoding="utf-8") as out_file:
    json.dump(index, out_file, indent=2, ensure_ascii=False)

print("✔ Vault indexed to 'notBorges_vault_index.json'")
