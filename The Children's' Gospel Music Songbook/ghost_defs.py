import re

with open("24GTC.txt", 'r', encoding='utf-8') as f:
    text = f.read()

# All references: [^note]
references = set(re.findall(r'\[\^([^\]]+)\]', text))
# All definitions: [^note]:
definitions = set(re.findall(r'\[\^([^\]]+)\]:', text))

unresolved = references - definitions

print(f"\n--- UNRESOLVED FOOTNOTES ({len(unresolved)} ghosts found) ---")
for ref in sorted(unresolved):
    print(f"[^" + ref + "]")
