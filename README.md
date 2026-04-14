# vox_implement

Modernized, runnable packaging of **[pennmem/voxTool](https://github.com/pennmem/voxTool)** (interactive intracranial electrode localization on post-implant CT). Upstream targets Python 2.7 and a Conda stack that is difficult to reproduce today; this repo provides **Python 3.10**, a **conda-forge** environment spec, code fixes, and a small **`./vox` CLI**.

## Quick start

```bash
git clone git@github.com:phindagijimana/vox_implement.git
cd vox_implement
./vox install    # micromamba + voxtool-env/
./vox check
./vox start -f   # foreground GUI; needs DISPLAY + working OpenGL for Mayavi/VTK
```

Run from repo root. On a desktop session, set `DISPLAY` if needed (e.g. `export DISPLAY=:0`).

## Repository layout

| Path | Purpose |
|------|---------|
| `voxTool/` | Application source (derived from upstream; see `voxTool/LICENSE.txt`) |
| `environment.yml` | Conda-forge env for Python 3.10 + VTK/Mayavi/Qt stack |
| `vox` | CLI: `install`, `check`, `start`, `stop`, `logs` |
| `implementation.md` | Patch notes, headless behavior, env recreation |
| `vox_br.md` | Builder-style review of the tool and this fork |
| `vox.md` | Short summary of what voxTool does (workflow) |

## Requirements

- **Linux x86_64** (aarch64 supported for micromamba bootstrap in `vox`; env may need verification).
- **Graphical session** for real use: X11/Wayland and GPU/Mesa adequate for VTK 9 / Mayavi.
- Network for first-time `install` (package download).

## License

Upstream code in `voxTool/` remains under **MIT** (`voxTool/LICENSE.txt`). Other files in this repository are contributed under the same spirit unless noted.
