---
permalink: permalink
---

<%*
const fileName = tp.file.title;
const fm = await tp.frontmatter;
if (!fm["permalink"]) {
  fm["permalink"] = fileName;
  await tp.frontmatter.update(fm);
}
%>

