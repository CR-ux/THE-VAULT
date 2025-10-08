import json
import re

# Load your JSON
with open("lexDict_output_with_lexDefs.json", "r") as f:
    data = json.load(f)

# List of valid usage types for fuzzy matching
valid_alleles = ["Noen", "Croen", "Wyrb", "Prodverb", "Ripture", "Lacronym", "Adjecture", "Badverb"]

# Ultra-fuzzy parser
for entry in data:
    if entry.get("lexDefs"):
        continue  # skip already-filled entries

    body = entry.get("body", "")
    lines = body.splitlines()
    lexDefs = []

    for line in lines:
        if "lexDef" not in line:
            continue
        
        # Find curly braces and < delimiter
        brace_match = re.search(r'\{([^{}]+)\}', line)
        angle_match = re.search(r'<(.*)', line)

        if brace_match and angle_match:
            usages_raw = brace_match.group(1)
            defs_raw = angle_match.group(1)

            usages = [u.strip() for u in usages_raw.split("||")]
            defs = [d.strip() for d in defs_raw.split("||")]

            for i, usage in enumerate(usages):
                for known in valid_alleles:
                    if known.lower() in usage.lower():
                        definition = defs[i] if i < len(defs) else ""
                        lexDefs.append({
                            "lexAllele": known,
                            "definition": definition
                        })
                        break  # one match per usage

    if lexDefs:
        entry["lexDefs"] = lexDefs
        entry["abundance"] = len(lexDefs)
        entry["potency"] = sum(1 for d in lexDefs if d.get("definition"))

# Write out new file
with open("lexDict_output_fuzzy_simple.json", "w") as f:
    json.dump(data, f, indent=2)

print("✅ Super-simple fuzzy LexDef parsing complete!")
