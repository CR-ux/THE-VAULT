<%*
const today = tp.date.now("dddd, MMMM Do YYYY");

// Tarot Pull Prompt
const tarotType = await tp.system.suggester(["Major", "Minor"], ["major", "minor"]);
let tarotOutput = "";

if (tarotType === "minor") {
  const suit = await tp.system.suggester(["Wands", "Cups", "Swords", "Pentacles"], ["Wands", "Cups", "Swords", "Pentacles"]);
  const number = await tp.system.prompt("Card number (1–10, Page, Knight, Queen, King)");

  const elementMap = {
    "Wands": "🜂 Fire",
    "Cups": "🜄 Water",
    "Swords": "🜁 Air",
    "Pentacles": "🜃 Earth"
  };
  const element = elementMap[suit];

  tarotOutput = `Minor Arcana — ${number} of ${suit} (${element})`;

} else {
  const majorName = await tp.system.prompt("Name of Major Arcana card (e.g., The Tower)");
  const majorList = [
    "The Fool", "The Magician", "The High Priestess", "The Empress", "The Emperor",
    "The Hierophant", "The Lovers", "The Chariot", "Strength", "The Hermit",
    "Wheel of Fortune", "Justice", "The Hanged Man", "Death", "Temperance",
    "The Devil", "The Tower", "The Star", "The Moon", "The Sun",
    "Judgement", "The World"
  ];
  const majorNumber = majorList.findIndex(c => c.toLowerCase() === majorName.toLowerCase());
  tarotOutput = `Major Arcana — ${majorName} (#${majorNumber >= 0 ? majorNumber : "??"})`;
}

const symbolRaw = await tp.system.prompt("Enter symbols (comma-separated)");
const symbols = symbolRaw.split(",").map(s => `#${s.trim().replace(/\s+/g, "-")}`).join(" ");
-%>

# <%= today %>

---

## SINGLE CARD PULL

<%= tarotOutput %>

---

## LAST NIGHT'S DREAM

---

**SYMBOLS:**  
<%= symbols %>

---

## GOALS FOR TODAY

- [ ] 
- [ ] 
- [ ] 

---