---
permalink: "{{title}}"
---
date: XVII_XXIII_ERA_Æ
---

**From:** <%* 
const sender = await tp.system.prompt("Who is sending this email? (e.g., Selena or Myon)");
tR += sender; 
%>

**To:** <%* 
const recipient = await tp.system.prompt("Who is receiving this email? (e.g., Selena or Myon)");
tR += recipient; 
%>

**Subject:** <%* 
const subject = await tp.system.prompt("What is the subject of the email?");
tR += subject; 
%>

---

My Light <%* 
tR += recipient; 
%>,

{{tp_placeholder:Body}}

<%* 
// Determine signature based on sender
const senderType = sender.toLowerCase().includes("selena") ? "S" : sender.toLowerCase().includes("myon") ? "M" : null;

if (senderType === "S") {
    tR += "_“Forever upward moonating toward the tidal-pulling, beautywards.”_ - S";
} else if (senderType === "M") {
    tR += '"O, Lustrous-stillness-shadow-cradled-light, round-airy-light-on-dark, tremulous-orbit-of-night’s-warmth, gentle-pull-of-cedar’s-resin-" - M';
} 
%>

<%* tR += sender; %>