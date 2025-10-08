import json

with open('entries_with_lexdef_only.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

subset_4_6 = [entry for entry in data if 4 <= len(entry.get('lexeme', '')) <= 6]

with open('entries_alt6.json', 'w', encoding='utf-8') as f_out:
    json.dump(subset_4_6, f_out, ensure_ascii=False, indent=2)

print(f"Filtered {len(subset_4_6)} entries with lexeme length 4 to 6")
