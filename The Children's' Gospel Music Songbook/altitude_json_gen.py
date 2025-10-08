import json

# Load the master JSON
with open('entries_with_lexdef_only.json', 'r', encoding='utf-8') as f:
    master_data = json.load(f)

# Filter for Alt3: only lexemes with length 1 to 3
alt3_subset = [entry for entry in master_data if 1 <= len(entry.get('lexeme', '')) <= 3]

# Save the Alt3 subset
with open('entries_alt3.json', 'w', encoding='utf-8') as f:
    json.dump(alt3_subset, f, ensure_ascii=False, indent=2)
