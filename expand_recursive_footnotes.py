import re
from pathlib import Path

def expand_recursive_footnotes(md_text, max_depth=5):
    footnote_pattern = r'\[\^([^\]]+)\]:\s*(.*?)(?=(?:\n\[\^)|\Z)'
    footnotes = {m[0]: m[1].strip() for m in re.findall(footnote_pattern, md_text, re.DOTALL)}

    def resolve(label, depth=0):
        if depth > max_depth:
            return f"\\textbf{{[max recursion reached for {label}]}}"
        if label not in footnotes:
            return f"\\textbf{{[missing {label}]}}"
        content = footnotes[label]
        return re.sub(r'\[\^([^\]]+)\]', lambda m: f"\\footnote{{{resolve(m.group(1), depth+1)}}}", content)

    def replace_footnote_calls(text):
        return re.sub(r'\[\^([^\]]+)\]', lambda m: f"\\footnote{{{resolve(m.group(1))}}}", text)

    stripped_md = re.sub(footnote_pattern, '', md_text, flags=re.DOTALL).strip()
    return replace_footnote_calls(stripped_md)

# === CUSTOMIZED PATH ===
input_path = Path("/Users/callierosepetal/vaults/notBorges-backup/lexDict.md")
output_path = Path("/Users/callierosepetal/vaults/notBorges-backup/lexDict_expanded.md")

# Read input, expand, write output
md_input = input_path.read_text(encoding="utf-8")
expanded = expand_recursive_footnotes(md_input)
output_path.write_text(expanded, encoding="utf-8")

print(f"✅ Recursive footnotes expanded: {output_path}")
