# graphic-testimonials

An agent skill (SKILL.md + scripts) that works with Kimi, Claude Code, and other agents that support skill folders.

**See example cards and the full pipeline: https://myaifreedomsystems.github.io/testimonial-skills-site/**

## Install

Copy this folder into your agent's skills directory (e.g. `~/.config/agents/skills/` or your runtime's managed skills root), restart the agent, and ask for it by name: `graphic-testimonials`.

## Contents

- `SKILL.md` — the workflow and rules
- `scripts/` — tested helper scripts
Create branded testimonial card images from quotes and photos — via a Canva template (Canva MCP editing transactions) or the bundled standalone HTML template rendered with headless Chrome. Recolors to your brand color, composites circular client photos, and wires cards into a web page. Configure via a project-level `brand.json` (schema in `references/brand-config.md`). Pair with **harvest-testimonials** for sourcing.
