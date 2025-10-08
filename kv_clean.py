import json

with open("notBorges_vault_index.json", "r", encoding="utf-8") as f:
    data = json.load(f)

cleaned_kv = {}

for file_name, entry in data.items():
    base_key = file_name.strip()

    # Clean usages
    lexdefs = entry.get("lexdefs", [])
    for d in lexdefs:
        d["usages"] = [u.strip().rstrip("}") for u in d.get("usages", [])]

    # Populate flat key-value pairs
    cleaned_kv[f"{base_key}:body"] = entry.get("body", "")
    cleaned_kv[f"{base_key}:lexdefs"] = lexdefs
    cleaned_kv[f"{base_key}:exits"] = entry.get("exits", [])

# Save clean output
with open("notBorges_kv_ready.json", "w", encoding="utf-8") as out_file:
    json.dump(cleaned_kv, out_file, indent=2, ensure_ascii=False)

print("✔ Cleaned and flattened JSON saved as 'notBorges_kv_ready.json'")
