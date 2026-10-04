# Flash Arcade

A small Ruffle-powered site for playing SWF games.

## Run it
    python3 serve.py
Then open http://localhost:8000. (Opening index.html directly won't work: browsers block loading games.json and the SWFs from file://.)

## Add a game
1. Drop the .swf into `games/`.
2. Add an entry to `games.json`:

       { "id": "my-game", "title": "My Game", "file": "games/my-game.swf",
         "width": 800, "height": 600, "description": "One line about it.",
         "tags": ["action"], "config": {} }

   - `id` becomes the link: `index.html#my-game`
   - `width`/`height` set the stage shape
   - `config` is optional and passes straight to Ruffle (e.g. `{ "quality": "medium" }`)

No code changes needed. Hosting: upload the whole folder to any static host (GitHub Pages, Netlify, school web space).
