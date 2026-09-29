# pygame_example_tutorial

A tile-based 2D platformer ("Ninja-Game"), built by following a pygame tutorial. Currently implements tilemap rendering and a physics entity with gravity, horizontal/vertical movement, and per-axis tile collision.

## 📁 Code

| File | Content |
|---|---|
| `game.py` | Entry point and main `Game` class: window setup, the asset dictionary, the game loop, input handling |
| `scripts/entities.py` | `PhysicsEntity` — position, velocity, gravity, and tile collision (resolved separately on the x-axis, then the y-axis); currently used for the player |
| `scripts/tilemap.py` | `Tilemap` — stores tiles in a dict keyed by grid position, and returns the handful of tiles around a given point for collision checks; currently seeded with a hardcoded strip of grass and stone tiles rather than loading one of the `data/maps/*.json` files |
| `scripts/utils.py` | `load_image()` / `load_images()` — asset-loading helpers that apply colorkey transparency (pure black is treated as transparent) |

## 🖼️ Assets (`data/`)

The tutorial's full asset pack is included, but the code so far only uses a part of it:

**Currently loaded by the code**

| Asset | Used as |
|---|---|
| `images/entities/player.png` | The player, drawn as a single static image (no animation yet) |
| `images/tiles/grass/` (9 variants), `images/tiles/stone/` (9 variants) | Physics tiles — solid, collidable |
| `images/tiles/decor/` (4 variants), `images/tiles/large_decor/` (3 variants) | Non-solid decoration tiles |

**Included for later, not yet wired into the code**

| Asset | Likely future use |
|---|---|
| `images/entities/player/` (idle: 22, run: 8, jump: 1, slide: 1, wall_slide: 1 frames) | Player animation states |
| `images/entities/enemy/` (idle: 16, run: 8 frames) | An enemy character |
| `images/particles/leaf/` (18 frames), `images/particles/particle/` (4 frames) | Particle effects |
| `images/clouds/` (2 images) | Parallax background clouds |
| `images/tiles/spawners/` (2 variants) | Map markers for spawning the player/enemies |
| `images/gun.png`, `images/projectile.png` | A shooting mechanic |
| `images/background.png` | A proper background (the game currently just fills with a flat blue) |
| `maps/0.json`, `maps/1.json`, `maps/2.json` | Tiled-editor map exports, to eventually replace the hardcoded tilemap in `Tilemap.__init__` |
| `sfx/*.wav`, `music.wav` | Sound effects and background music |

## ⚙️ Requirements

```bash
pip install pygame
```

## 🚀 Running

Run it from inside this folder — assets are loaded using paths relative to here (`data/images/...`):

```bash
cd Py_learning/pygame/pygame_example_tutorial
python3 game.py
```

## 🎮 Controls

| Key | Action |
|---|---|
| `A` / `D` | Move left / right |
| `W` | Jump |

## 📌 Notes

- `self.collision_area` in `Game.__init__` is currently unused.
- There's a `print(self.tilemap.physics_rect_around(self.player.pos))` left in the game loop — handy for debugging collision, but noisy in the console; safe to remove once you're done inspecting it.
