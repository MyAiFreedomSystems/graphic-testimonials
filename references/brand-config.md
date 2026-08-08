# brand.json Schema

Place a `brand.json` in the project root so any agent can run the pipeline without re-asking. All fields optional — ask the user for whatever is missing.

```json
{
  "brand": {
    "navy": "#1B3A5C",
    "cream": "#F1EFE9",
    "yellow": "#FFF066",
    "script_font": "<your script font>",
    "script_font_path": "/abs/path/to/font.ttf"
  },
  "canva": {
    "template_design_id": "DXXXXXXXXXX",
    "card_size": [1080, 1080],
    "element_suffixes": { "quote": "…", "name": "…", "role": "…" },
    "photo_slot": { "left": 420, "top": 55, "size": 240 }
  },
  "site": {
    "dir": "/abs/path/to/site",
    "repo": "https://github.com/OWNER/REPO.git",
    "grid_class": "trio",
    "overflow_heading": "More Client Wins"
  },
  "copy_rules": {
    "framing": "money + time + energy",
    "banned": ["words", "not", "allowed"],
    "section_heading": "What Clients Say",
    "real_clients_only": true
  }
}
```

- `element_suffixes`: stable element-ID suffixes in the user's template, read from a `start-editing-transaction` response (page prefix + suffix = full element ID). Capture them on first run and write them back into the config.
- `photo_slot`: where the circular photo sits on the card (match the template's existing photo card).
- `copy_rules.real_clients_only` should always stay `true`.
