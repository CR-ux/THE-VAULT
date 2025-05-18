
<%*

let layer = await tp.system.prompt("Enter layer (Æ, i|o, U, 1, or 0)");
let word = await tp.system.prompt("Enter the lexeme (the word)");
let usageInput = await tp.system.prompt("Enter lexAllele(s), separated by || (e.g. Noen || Croen(ARIA var|DNE var))");

let usages = usageInput.split("||").map(u => u.trim());

let definitions = {};
let sources = {};
let metas = {};
let croenARIA = "";
let croenDNE = "";

// Gather data for each usage
for (let usage of usages) {
  if (usage.startsWith("Croen")) {
    croenARIA = await tp.system.prompt(`Enter ARIA var (e.g. A ${word} of <Noens>)`);
    croenDNE = await tp.system.prompt(`Enter DNE var (e.g. A <Croen> of ${word}s)`);
    definitions[usage] = `N.B. ARIA var = "${croenARIA}" | DNE var = "${croenDNE}"`;
  } else {
    definitions[usage] = await tp.system.prompt(`Enter definition for ${usage}`);
  }
  sources[usage] = await tp.system.prompt(`Enter source document title for ${usage}`);
  metas[usage] = await tp.system.prompt(`Enter author/publication info for ${usage} (in quotes)`);
}

// Build usage block and joined definitions
let usageBlock = usages.join(" || ");
let definitionBlock = usages.map(u => `${definitions[u]}[^${word}${u}]`).join(" || ");

// Output main lexDef line
tR += `lexDef (${layer}) "${word}" {lexAllele(s)::: ${usageBlock}} < ${definitionBlock}\n\n`;

// Output footnotes
for (let usage of usages) {
  let label = `${word}${usage}`;
  let source = sources[usage];
  let meta = metas[usage];
  tR += `[^${label}]: [[${source}]], ${meta}\n`;
}

%>