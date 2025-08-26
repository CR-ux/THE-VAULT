import os
import re
import json

vault_path = "/Users/callierosepetal/vaults/notBorges-backup"
output_path = os.path.join(vault_path, "lexDict_soft.json")
lexdict = {}
parse_summary = {
    "total_files": 0,
    "total_lexemes": 0,
    "soft_parsed": 0,
    "strict_parsed": 0,
    "entries_with_warnings": 0
}

# Footnote pattern
footnote_pattern = re.compile(r'\[\^([^\]]+)\]:\s+\[\[(.*?)\]\],\s+"(.*?)"')

# Helper to parse allele block
def parse_alleles(allele_block):
    alleles = []
    for part in allele_block.split("||"):
        part = part.strip()
        match = re.match(r'(\w+)\s*\{([^}]*)\}', part)
        if match:
            alleles.append((match.group(1), match.group(2).strip()))
        else:
            alleles.append((part.strip(), None))
    return alleles

# Walk through vault
for root, _, files in os.walk(vault_path):
    for file in files:
        if file.endswith(".md"):
            parse_summary["total_files"] += 1
            with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                content = f.read()

                # Capture footnotes
                footnotes = {}
                for fn in footnote_pattern.findall(content):
                    key, src, meta = fn
                    footnotes[key.strip()] = {"source": src.strip(), "meta": meta.strip()}

                # Find all lexDefs — softened form
                lex_blocks = re.findall(
                    r'lexDef\s*(?:\((.*?)\))?\s*"([^"]+)"\s*\{lexAllele\(s\):::(.*?)\}\s*<\s*(.*?)(?=^lexDef|\Z)',
                    content,
                    re.DOTALL | re.MULTILINE
                )

                for block in lex_blocks:
                    layer, lexeme, allele_block, def_block = block
                    parse_summary["total_lexemes"] += 1
                    layer = layer.strip() if layer else None
                    lexeme = lexeme.strip()

                    alleles = parse_alleles(allele_block)
                    definitions = [d.strip() for d in def_block.strip().split("||")]

                    soft_parsed = False
                    warning = None

                    if len(definitions) < len(alleles):
                        definitions += [""] * (len(alleles) - len(definitions))
                        warning = "Definition count < allele count"
                        parse_summary["entries_with_warnings"] += 1
                        soft_parsed = True

                    entry = {
                        "lexeme": lexeme,
                        "layer": layer,
                        "lexAlleles": {},
                    }

                    if warning:
                        entry["parse_warning"] = warning

                    for idx, (allele, note) in enumerate(alleles):
                        usage_text = definitions[idx] if idx < len(definitions) else ""
                        key = f"{lexeme}{allele}"
                        allele_entry = {}

                        # Handle dual ARIA/DNE case
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
                                warning = "Could not parse ARIA/DNE split"
                                entry["parse_warning"] = warning
                                parse_summary["entries_with_warnings"] += 1
                                soft_parsed = True
                        else:
                            allele_entry["usage"] = usage_text
                            if allele == "Croen":
                                allele_entry["note"] = note  # can be None

                        # Attach footnotes if available
                        if key in footnotes:
                            allele_entry.update(footnotes[key])
                        else:
                            # Try fallback fuzzy match
                            alt_key = next((k for k in footnotes if k.lower() == key.lower()), None)
                            if alt_key:
                                allele_entry.update(footnotes[alt_key])
                                soft_parsed = True
                            else:
                                allele_entry["source"] = None
                                allele_entry["meta"] = None
                                soft_parsed = True

                        entry["lexAlleles"][allele] = allele_entry

                    lexdict[lexeme] = entry
                    if soft_parsed:
                        parse_summary["soft_parsed"] += 1
                    else:
                        parse_summary["strict_parsed"] += 1

# Write to JSON
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(lexdict, f, indent=2, ensure_ascii=False)

# Print parse summary
print("\n✅ LexDict saved to:", output_path)
print("\n📊 Parse Summary:")
for k, v in parse_summary.items():
    print(f"  {k}: {v}")
