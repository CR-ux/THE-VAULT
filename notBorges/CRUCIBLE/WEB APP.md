---
permalink: WEB APP
---
Use tone.js to actually generate the music in the browser / use ‘samples’ of pre-recorded material and trigger using tone.js:
const player = new Tone.Player("https://tonejs.github.io/audio/berklee/gong_1.mp3").toDestination();
Tone.loaded().then(() => {
    player.start();
});

https://tonejs.github.io/