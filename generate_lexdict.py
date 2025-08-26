import os
import re
import json

# Path to your Obsidian vault
vault_path = "/Users/callierosepetal/vaults/notBorges-backup"
output_path = os.path.join(vault_path, "lexDict.json")
lexdict = {}

# Regex patterns
lexdef_pattern = re.compile(
    r'lexDef\s*(?:\((.*?)\))?\s*"([^"]+)"\s*\{lexAllele\(s\):::\s*(.*?)\}\s*<\s*(.*)',
    re.DOTALL
)
footnote_pattern = re.compile(
    r'\[\^(\w+)\]:\s+\[\[(.*?)\]\],\s+"(.*?)"'
)

# Parse lexAllele(s) block like: Noen || Croen {post-reannealment}
def parse_alleles(allele_block):
    alleles = []
    for part in allele_block.split("||"):
        part = part.strip()
        match = re.match(r'(\w+)\s*\{([^}]*)\}', part)
        if match:
            alleles.append((match.group(1), match.group(2).strip()))
        else:
            alleles.append((part, None))
    return alleles

# Walk through vault
for root, _, files in os.walk(vault_path):
    for file in files:
        if file.endswith(".md"):
            with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                content = f.read()

                # Gather footnotes first
                footnotes = {}
                for fn in footnote_pattern.findall(content):
                    key, src, meta = fn
                    footnotes[key.strip()] = {
                        "source": src.strip(),
                        "meta": meta.strip()
                    }

                # Process all lexDefs
                for match in lexdef_pattern.findall(content):
                    layer, lexeme, allele_block, def_block = match
                    layer = layer.strip() if layer else None
                    lexeme = lexeme.strip()

                    alleles = parse_alleles(allele_block)
                    definitions = [d.strip() for d in def_block.strip().split("||")]

                    if len(definitions) < len(alleles):
                        definitions += [""] * (len(alleles) - len(definitions))

                    entry = {
                        "lexeme": lexeme,
                        "layer": layer,
                        "lexAlleles": {}
                    }

                    for idx, (allele, note) in enumerate(alleles):
                        usage_text = definitions[idx] if idx < len(definitions) else ""
                        key = f"{lexeme}{allele}"
                        allele_entry = {}

                        # Dual-variant Croen (ARIA + DNE)
                        if "ARIA" in usage_text and "DNE" in usage_text and allele == "Croen":
                            split_match = re.search(
                                r'ARIA.*?=\s*"(.*?)"\s*\|\s*DNE.*?=\s*"(.*?)"', usage_text)
                            if split_match:
                                allele_entry = {
                                    "ARIA": split_match.group(1).strip(),
                                    "DNE": split_match.group(2).strip()
                                }
                            else:
                                allele_entry["usage"] = usage_text
                        else:
                            allele_entry["usage"] = usage_text
                            if allele == "Croen":
                                allele_entry["note"] = note

                        # Add footnote metadata
                        if key in footnotes:
                            allele_entry.update(footnotes[key])
                        else:
                            allele_entry["source"] = None
                            allele_entry["meta"] = None

                        entry["lexAlleles"][allele] = allele_entry

                    lexdict[lexeme] = entry

# Save the result
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(lexdict, f, indent=2, ensure_ascii=False)

print(f"✅ lexDict saved to {output_path}")
