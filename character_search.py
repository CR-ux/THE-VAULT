import os
import re
import json

# Config: Set the root directory of your vault and the character list
VAULT_DIR = "/Users/callierosepetal/vaults/notBorges-backup"
CHARACTERS = ["RA", "Aria", "Selena", "Myo", "⧖eno" "Hildr", "D&E", "Dot Code", "Tod Code", "Ed. O.", "Oleander", "NoetBorges"]

# Function to search for character mentions
def search_mentions(vault_dir, characters):
    results = {}
    
    for root, dirs, files in os.walk(vault_dir):
        for file in files:
            if file.endswith(".md"):
                path = os.path.join(root, file)
                with open(path, 'r', encoding='utf-8') as f:
                    text = f.read()
                    for name in characters:
                        if re.search(rf"\b{name}\b", text):
                            if name not in results:
                                results[name] = []
                            results[name].append(path)
    
    return results

# Run the search
if __name__ == "__main__":
    mentions = search_mentions(VAULT_DIR, CHARACTERS)
    
    # Save or print results
    with open("character_mentions.json", "w", encoding='utf-8') as f:
        json.dump(mentions, f, indent=4)

    print("Search complete. Results saved to character_mentions.json")
