import json

with open('entries_with_lexdef_only.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

subset_10_plus = [entry for entry in data if len(entry.get('lexeme', '')) >= 10]

with open('entries_alt10plus.json', 'w', encoding='utf-8') as f_out:
    json.dump(subset_10_plus, f_out, ensure_ascii=False, indent=2)

print(f"Filtered {len(subset_10_plus)} entries with lexeme length 10 or more")
