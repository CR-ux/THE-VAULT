<%*

let word = await tp.system.prompt("Enter the lexeme (the word)");
let usageInput = await tp.system.prompt("Enter usage types, separated by || (e.g. Noen || Croen)");

let usages = usageInput.split("||").map(u => u.trim());

let definitions = {};
let sources = {};
let metas = {};

// Gather data for each usage
for (let usage of usages) {
  if (usage === "Croen") {
    let croenQuote = await tp.system.prompt(`Enter the Croen quote (e.g. "A Library of Librarys")`);
    definitions[usage] = `N.B. "${croenQuote}"`;
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
tR += `lexDef "${word}" {usage::: ${usageBlock}} < ${definitionBlock}\n\n`;

// Output footnotes
for (let usage of usages) {
  let label = `${word}${usage}`;
  let source = sources[usage];
  let meta = metas[usage];
  tR += `[^${label}]: [[${source}]], ${meta}\n`;
}

%>