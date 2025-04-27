const fs = require('fs');
const path = require('path');
const index = {};

const vaultRoot = './'; // assuming we're already in the root directory

function walk(dir) {
  const files = fs.readdirSync(dir);
  for (const file of files) {
    const fullPath = path.join(dir, file);
    const stat = fs.statSync(fullPath);

    if (stat.isDirectory()) {
      walk(fullPath); // recursive walk
    } else if (file.endsWith('.md')) {
      const content = fs.readFileSync(fullPath, 'utf8');
      const permalinkMatch = content.match(/permalink:\s*["']?([^"\n]+)["']?/i);

      let slug;
      if (permalinkMatch) {
        slug = permalinkMatch[1].trim();
      } else {
        slug = path.basename(file, '.md'); // fallback to filename
      }

      if (index[slug]) {
        console.warn(`⚠️ Duplicate slug detected: "${slug}" at ${fullPath}. Skipping.`);
        continue;
      }

      const relativePath = path.relative(vaultRoot, fullPath).replace(/\\/g, '/');
      index[slug] = relativePath;
    }
  }
}

walk(vaultRoot);

fs.writeFileSync('index.json', JSON.stringify(index, null, 2));
console.log(`✅ index.json built with ${Object.keys(index).length} entries.`);
