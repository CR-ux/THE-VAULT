import json

# Load your existing parsed lexDefs
with open("notBorges_vault_index.json", "r", encoding="utf-8") as f:
    data = json.load(f)

enriched_data = {}

for key, entry in data.items():
    usages = entry.get("usages", [])
    exits = entry.get("exits", [])
    
    potency = len(usages)
    valency = len(exits)
    
    enriched_data[key] = {
        "body": entry.get("body", ""),
        "usages": usages,
        "exits": exits,
        "potency": potency,
        "valency": valency
    }

# Save enriched output
with open("lexicon_enriched.json", "w", encoding="utf-8") as f:
    json.dump(enriched_data, f, indent=2, ensure_ascii=False)
