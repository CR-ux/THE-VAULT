import json

# Load the original JSON
with open("notBorges_vault_index.json", "r", encoding="utf-8") as infile:
    data = json.load(infile)

# New flat KV dictionary
kv_data = {}

for filename, contents in data.items():
    body = contents.get("body", "")
    lexdefs = contents.get("lexdefs", [])
    exits = contents.get("exits", [])

    kv_data[f"{filename}:body"] = body
    kv_data[f"{filename}:lexdefs"] = lexdefs
    kv_data[f"{filename}:exits"] = exits

# Save the flattened output
with open("notBorges_kv_ready.json", "w", encoding="utf-8") as outfile:
    json.dump(kv_data, outfile, indent=2, ensure_ascii=False)

print("✔ KV-ready JSON written to 'notBorges_kv_ready.json'")
