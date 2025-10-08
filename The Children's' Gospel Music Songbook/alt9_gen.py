import json

with open('entries_with_lexdef_only.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

subset_7_9 = [entry for entry in data if 7 <= len(entry.get('lexeme', '')) <= 9]

with open('entries_alt9.json', 'w', encoding='utf-8') as f_out:
    json.dump(subset_7_9, f_out, ensure_ascii=False, indent=2)

print(f"Filtered {len(subset_7_9)} entries with lexeme length 7 to 9")
