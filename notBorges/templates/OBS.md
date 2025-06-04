<%*
const letter = await tp.system.prompt("Which letter is N for?");
const lexDefs = [];

lexDefs.push(await tp.system.prompt("Pawn?"));
lexDefs.push(await tp.system.prompt("Knight (1)?"));
lexDefs.push(await tp.system.prompt("Knight (2)?"));
lexDefs.push(await tp.system.prompt("Knight (3)?"));
lexDefs.push(await tp.system.prompt("Rook?"));
lexDefs.push(await tp.system.prompt("Bishop?"));
lexDefs.push(await tp.system.prompt("Final Pawn?"));

tR += `
**LOCH: INNER**
**KEY:  ∈ | t | {const}**
**var N = ${letter}** 

**🜁  / ♙ | OBS: 12:00 | Q=10⁻⁵**
**{REDACTED}**
**Isn't N for** 
![[${lexDefs[0]}]]

**🜂 / ♞  | OBS: 15:00 | ε=0.007**
**{REDACTED}**
**But I am that N is for**
![[${lexDefs[1]}]]

**🜂 / ♞  | OBS: 15:00 | ε=0.007**
**{REDACTED}**
**Scratch that. N is for**
![[${lexDefs[2]}]]

**🜂 / ♞  | OBS: 15:00 | ε=0.007**
**{REDACTED}**
**Or actually, yes N is for**
![[${lexDefs[3]}]]

**🜃 / ♜  | OBS: 18:00 | N=10³⁶**
**{REDACTED}**
**No. N must be for**
![[${lexDefs[4]}]]

**🜄 / ♝ | OBS: 21:00 | D=3**
**{REDACTED}**
**whtifNfor**
![[${lexDefs[5]}]]

**🜁  / ♙ | OBS: 12:00 | Q=10⁻⁵**
**{REDACTED}**
**Now I am I sure. That N is for** 
![[${lexDefs[6]}]]
`
%>