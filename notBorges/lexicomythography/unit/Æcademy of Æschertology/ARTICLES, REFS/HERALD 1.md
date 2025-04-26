---
permalink: HERALD 1
---
<p style="text-align:justify;margin:0"> **(error reading attachment)**
<b>HERALD is the prismatic flagship project of CR.ux</b> - designed as a vehicle that attempts to interface the ineffable. Guiding users on a pilgrimage of alchemical self-transformation through personal data analysis*.
-    At its heart, a captivating musical framework to regularly connect with one’s own inner awareness. An interactive tool to observe how our surroundings (above) are mirrored in our internal state (below), and connected to the collective resonance of us all (and of course the Moon).
-    A distillation of emotional states, menial tasks, and habit transmutation statistics into a personal ‘Resonance’ – downloadable audio procedurally generated; its resultant waveform transformed into an interactive 2D sidescroller by the Herald Orchestral Leviathan Interpretive Engine. HOLIE is an intricately composed tapestry of algorithms, whose inputs are split into <i>Yin data</i> and <i>Yang data</i> categories; all of which is transparently visible within the app and is expanded upon <u>here</u>, should you be interested to peek under the veil
-    Within Stave View, traverse the sound of your memories as a stunning 2D sidescroller, from daily ‘Phrases’, to Monthly ‘Cycles’, Quarterly ‘Movements’ and Annual ‘Symphonies’ of procedurally generated music based on your personal state of Being throughout that period, encountering entities and transformations depending on the user’s data at that particular Measure of the Resonance.
-    An elegant home for your scramblings, todos, and progress with sobriety or habit cessation goals.
o    A strategy to eliminate addictive or harmful behaviours (base metals) by transmuting them into constructive, restful, playful, mindful habits (gold).
o    Motivation to complete tasks (should the SALT ingredient be toggled) as the HOLIE chaos ensues with a fuller, more neglected tasklist.
o    Motivation to adhere to habit goals (should the SULPHUR ingredient be toggled, which sets HOLIE to generate more and more joyful melodic Resonances for every day quit / sober / doing the thing. Only defaulting back to a dull boring drone for the measure the slip-up was recorded, before blooming back into beautiful complexity, to remind you of your resilience, and to encourage you not to beat yourself up for simply being so wonderfully human.  
o    Motivation to input journal entries (should the MERCURY ingredient be toggled in your concoction config) as rests (silence) are introduced into the HOLIE Resonance and Stave View with every day skipped in the journal.
*HERALD functions with the artful integration and algorithmic interpretation of users’ data. Various markers of progress, peace and productivity and its correlation with NASA lunar phase data to create procedurally generated Symphonies with the Herald Orchestral Leviathan Interpretive Engine that runs its own magick in the highly secure backend. Rooted in the AZOTH [Alchemical Zephyr of Tarot Heuristics] magick system, HERALD provides a contemplative space where users can transmute their everyday experiences, tasks, inmost emotions and inanest thoughts into fruitful observations of behavioural trends and personal triumphs in an immersive, interactive experience.
</p>
 
 
 
**Dev Roadmap**
**Phase 1: Foundation & Audio Signal Production**
 
<u>Getting Started with Audio Signal Production</u>
Learn SuperCollider: Set up a basic SuperCollider server and experiment with generating audio.  
**Project:** Create a basic server-side audio synthesizer that generates tones based on user input.
<u>Crucible Design & Basic UI</u>
React & Redux Basics: Build a simple form UI with React and manage state with Redux.
**Project:** Develop the CRUCIBLE form with basic fields (journal entry, mood, habits, tarot).
<u>Basic Data Handling</u>
Scala & Play Framework: Integrate with your existing this.todo project to handle form submissions and store data in MongoDB.
**Project:** Implement basic CRUD operations for the CRUCIBLE entries.
**Phase 2: Expanding SALT Module**
 
<u>Extend SALT Functionality</u>
Add Edit Functionality: Implement edit operations for the SALT module in Scala & Play.
**Project:** Complete the SALT module with full CRUD operations.
<u>Integrate SALT with Audio Synthesis</u>
Connect SALT Data to SuperCollider: Map task list state, tags, and subtags to audio parameters in SuperCollider.
**Project:** Generate audio based on task list data, with specific sounds for tags and subtags.
<u>UI Enhancements</u>
Improve Task Management UI: Enhance the task list interface with better UX and visualizations.
**Project:** Create a more user-friendly interface for the SALT module.
 
 
 
 
 
**Phase 3: Developing Other Modules**
 
<u>SULPHUR Module (Habit State)</u>
Habit Tracking System: Build a habit tracking interface and logic to measure success over time.
**Project:** Implement the SULPHUR module, affecting audio based on habit data.
<u>MERCURY Module (Journal)</u>
Sentiment Analysis Integration: Use Python (spaCy or TextBlob) for analyzing journal entries.
**Project:** Generate corresponding tones using SuperCollider based on journal sentiment.
<u>ALEMBIC Module (newMood)</u>
Mood Tracking Interface: Develop a mood tracking interface and visualize mood vs moon phase.
**Project:** Implement the ALEMBIC module, affecting audio amplitude and correlation with moon phase.
<u>ATHANOR Module (AZOTH-Informed Tarot Spread Interpretation Data)</u>
Tarot Reading Interface: Create an interface for tarot readings and map them to the alchemical system.
**Project:** Implement the ATHANOR module, generating audio based on tarot spread history.
 
 
**Phase 4: Stave View & Collective Resonance**
 
<u>Stave View Development</u>
Unity Basics: Learn Unity and C# to develop the side-scroller game.
**Project:** Create a basic version of the Stave View where users can traverse their waveform.
<u>Integrate Audio with Unity</u>
Sync Audio with Unity: Connect the audio generated by SuperCollider to the Unity game.
**Project:** Enhance the Stave View with various time period staves and user interactions.
<u>Collective Resonance</u>
Global Data Handling: Learn to manage and aggregate data for collective resonance.
**Project:** Implement the Collective Resonance feature, visualizing global and personal waveforms.
<u>Final Integration & Polishing</u>
End-to-End Testing: Test the complete application, ensuring all modules work seamlessly together.
**Project:** Refine and polish the user interface, user experience, and performance.
 
**Phase 5: Deployment & Scalability**
 
<u>Deployment</u>
AWS & EC2 Basics: Learn to deploy your application using AWS.
**Project:** Deploy HERALD to a cloud server, ensuring it is scalable and accessible.
<u>Performance Optimization</u>
Optimize Audio Processing: Ensure SuperCollider scales well with increased user data.
**Project:** Optimize data handling, storage, and retrieval for performance.
<u>User Authentication & Security</u>
Implement Security Measures: Secure user data with authentication and encryption.
**Project:** Add robust user authentication and ensure data privacy.
 
**Simulated Streaming Implementation**
 
<u>Pre-Download Audio Data</u>
Generate and store audio files on the server during **the Witching Hour**.
Allow users to download these files when they open the app after the Witching Hour.
<u>Download Audio Data in Unity</u>
Use Unity's audio handling capabilities to manage the playback.
<u>Simulate Real-Time Playback</u>
Use Unity's timeline and scripting to control the playback of the audio files, simulating a streaming experience.
Sync the audio playback with the visual representation in the stave view.