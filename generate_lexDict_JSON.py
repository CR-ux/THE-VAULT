import os
import re
import json

vault_path = "/Users/callierosepetal/vaults/notBorges-backup"
output_path = "lexDict_output.json"

def extract_outgoing_links(text):
    return re.findall(r'!?\[\[([^\]]+)\]\]', text)

def extract_lexdefs_fuzzy(text):
    # Fuzzy match: allows for whitespace, variations in 'usage', and optional [^footnotes]
    pattern = re.compile(
        r'lexDef\s*{[^}]*?(?:lexAllele\(s\)|usage\(s\)|usages|usage)?\s*:::+\s*(.*?)\s*}.*?<\s*(.*?)\n',
        re.IGNORECASE | re.DOTALL
    )
    matches = pattern.findall(text)
    cleaned = []
    for alleles, definition in matches:
        allele_list = [a.strip() for a in alleles.split("||")]
        cleaned.append({
            "alleles": allele_list,
            "definition": definition.strip()
        })
    return cleaned

def is_one_word_name(filename):
    name = filename.replace('.md', '')
    return bool(re.match(r'^[\w\-]+$', name))  # Allow hyphens/underscores as okay for now

data = []

for root, dirs, files in os.walk(vault_path):
    for file in files:
        if file.endswith(".md") and is_one_word_name(file):
            filepath = os.path.join(root, file)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()[:144000]
                    lexDefs = extract_lexdefs_fuzzy(content)
                    links = extract_outgoing_links(content)
                    data.append({
                        "filename": file,
                        "lexeme": file.replace(".md", ""),
                        "body": content,
                        "lexDefs": lexDefs,
                        "abundance": len(lexDefs),
                        "potency": sum(len(ld["alleles"]) for ld in lexDefs),
                        "outgoing_links": links
                    })
            except Exception as e:
                print(f"Failed to read {filepath}: {e}")

with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Saved {len(data)} entries to {output_path}")
