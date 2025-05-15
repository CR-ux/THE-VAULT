---
permalink: App ideas list
---

| this.todo        | Scala CRUD todo app w/ kanbans for tags & charting functionality                                                                                                                                                                                                                                                                                                |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Enigma           | Generates sigils for magickal practice                                                                                                                                                                                                                                                                                                                          |
| Seraphina        | Personalised reading app which integrates context for own decks and self-designed spreads                                                                                                                                                                                                                                                                       |
| newMood          | Daily mood journal entries, mood scales plotted against moon phase                                                                                                                                                                                                                                                                                              |
| Scrabblr         | Scrabble app written in multiple languages (please suggest stack usage)                                                                                                                                                                                                                                                                                         |
| anchorPallette   | ‘Anchoring’ app, which rotates through user-defined arrays of assets, providing a time-based context for meditation/presence                                                                                                                                                                                                                                    |
| ariadn.e         | Generative music app which takes the user on a journey into a labyrinth, with tone.js instruments being manipulated by NLP algorithms determining the sentiment of user answers to open questions posed in a sequence of increasing vulnerability - themed like a text based game ; produces a merged mp3 output that can be bounced and downloaded by the user |
| cleanSlate       | Encourages cessation of bad habits/addictions                                                                                                                                                                                                                                                                                                                   |
| CCPHNY           | Using tone.js library , integrate with this.todo / todos  mongodb collection to create an audio context per tag, a note per subtag populated with todos, and an effect per todo within each subtag, resulting in more and more layers of cacophonous sounds depending on how full the user’s todo list is                                                       |
| xLibre / upScale | ED-fighting app which gamifies healthy eating habits / sufficient nutrition, with a retro user interface & LVLups etc                                                                                                                                                                                                                                           |
| SYMPHNY          | Creates a small audio sample of set time from user inputted daily entry using Tone.js library of pre-prepared instruments                                                                                                                                                                                                                                       |
Parameters such as instrument, octave, note, effects, are determined by sentiment of entry 
Collects samples over time, leading to a ‘symphony’ |
| HERALD | see |





| <p style="text-align:center;margin:0"><b>Project</b></p> | <p style="text-align:center;margin:0"><b>Description</b></p> | <p style="text-align:center;margin:0"><b>Tech Stack</b></p> | <p style="text-align:center;margin:0"><b>Approach</b></p> |
| -- | -- | -- | -- |



| Priority matrix / this.todo | Scala CRUD todo app w/ kanbans for tags & charting functionality | Scala, Play Framework, React, MongoDB, D3.js | Develop backend with Play Framework and MongoDB for CRUD operations. Use React for the frontend with D3.js for charting. Implement kanban boards. |
| -- | -- | -- | -- |



| Sigil maker | Generates sigils for magickal practice | Python, Flask, React, OpenCV | Create backend with Flask to handle sigil generation logic. Use OpenCV for image processing and React for the frontend. Integrate user inputs. |
| -- | -- | -- | -- |



| Tarot reader | Personalised reading app which integrates context for own decks and self-designed spreads | Node.js, Express, React, MongoDB | Develop backend with Node.js and Express for handling tarot reading logic. Store user decks and spreads in MongoDB. Use React for frontend. |
| -- | -- | -- | -- |



| Mood journal + New mood (moon phase vs mood) | Daily mood journal entries, mood scales plotted against moon phase | Python, Django, React, PostgreSQL, Plotly | Build backend with Django and PostgreSQL for storing entries. Use React for frontend and Plotly for visualizing mood vs moon phase data. |
| -- | -- | -- | -- |



| Scrabblr | Scrabble app written in multiple languages | Java, Spring Boot, React, WebSockets, MySQL | Develop backend with Spring Boot and MySQL for game logic and data storage. Use React for frontend and WebSockets for real-time game interaction. |
| -- | -- | -- | -- |



| Anchor palette | ‘Anchoring’ app, rotates through user-defined arrays of assets, providing a time-based context for meditation/presence | Node.js, Express, React, MongoDB | Create backend with Node.js and Express for asset management. Use MongoDB for data storage and React for frontend. Implement timers and rotations. |
| -- | -- | -- | -- |



| Ariadne | Generative music app with tone.js instruments, NLP algorithms for sentiment analysis, themed like a text-based game | Python, Flask, React, tone.js, NLTK, ffmpeg | Develop backend with Flask and NLP processing using NLTK. Use tone.js for music generation and React for frontend. Generate and merge mp3 files. |
| -- | -- | -- | -- |



| cleanSlate | Encourages cessation of bad habits/addictions | Ruby on Rails, React, PostgreSQL | Build backend with Ruby on Rails and PostgreSQL for tracking habits. Use React for frontend. Implement motivational features and progress tracking. |
| -- | -- | -- | -- |



| Cacophony | Integrates with this.todo/todos MongoDB collection to create an audio context per tag using tone.js | Node.js, Express, React, tone.js, MongoDB | Create backend with Node.js and Express to fetch todo data. Use tone.js for audio generation and React for frontend. Implement layered audio effects. |
| -- | -- | -- | -- |



| xLibre / upScale | ED-fighting app which gamifies healthy eating habits with a retro user interface & LVLups | Unity, C#, Node.js, Express, MongoDB | Develop frontend with Unity for a retro game interface. Use Node.js and Express for backend logic and MongoDB for data storage. Implement gamification. |
| -- | -- | -- | -- |



Assets / datastores



| Instrument components | Pre-made tone.js components |
| -- | -- |
| Composition algorithms | Pre-made algorithms to process signals from tone.js components and other sources |
| todos | MongoDB collection of todo objects |
| AZOTHAPI | API endpoints for each knot of the system |