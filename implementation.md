# voxTool implementation notes (this workspace)

## Repository

- Cloned upstream: [pennmem/voxTool](https://github.com/pennmem/voxTool) into `voxTool/`.

## Why the upstream installer no longer works as-is

- `conda_env.yml` pins **Python 2.7**, **PyQt4**, old **VTK**, and the deprecated **`free`** channel. On current Anaconda/conda-forge that environment is **not reproducible** on RHEL 9–class systems, and **system Python is 3.x only**.

## What we did here

1. **Micromamba** (no admin): binary under `.micromamba/micromamba`; env prefix **`voxtool-env/`** (or recreate from `environment.yml`).
2. **Python 3 port (minimal)** in `voxTool/`:
   - `ETS_TOOLKIT`: `qt4` → `qt` (PySide6/PyQt5 via pyface).
   - `yaml.safe_load`, UTF-8 `open(...)`.
   - Package imports: `from model import interpolator`, `from view.slice_viewer import ...`.
   - `xrange` / `.next()` → `range` / `next()`.
   - `matplotlib`: `backend_qt4agg` → `backend_qtagg`; `set_axis_bgcolor` → `set_facecolor`.
   - `scipy.ndimage.morphology.binary_dilation` → `scipy.ndimage.binary_dilation`.
   - **`view/slice_viewer.py`**: removed unused **Traits `Instance(MlabSceneModel)`** on a **matplotlib `FigureCanvas` subclass**. That combination **segfaulted** on import with VTK9 + PySide6; the Mayavi scene hooks there were already commented out and unused.

## CLI wrapper

From the `vox_implemnt` directory:

| Command | Purpose |
|--------|---------|
| `./vox install` | Bootstrap micromamba (if needed) and create `voxtool-env/` from `environment.yml` |
| `./vox check` | Verify env and that `PylocControl` imports |
| `./vox start` | Start in background; stdout/stderr → `.vox/voxtool.log` |
| `./vox start -f` | Foreground (typical on a desktop GUI) |
| `./vox stop` | Stop background process recorded in `.vox/voxtool.pid` |
| `./vox logs` | `tail -f` the log; add `--no-follow` to dump once |

Set `DISPLAY` when needed (e.g. `export DISPLAY=:0`).

## Run (without CLI)

From `voxTool/`:

```bash
/path/to/vox_implemnt/voxtool-env/bin/python launch_pyloc.py
```

Or activate the env with micromamba/conda and run the same command.

You need a working **X11/Wayland display** and **OpenGL** sufficient for VTK/Mayavi (local desktop or GPU-capable VNC; plain SSH without X forwarding is not enough for the 3D pane).

## Headless / CI

- `QT_QPA_PLATFORM=offscreen` allows **import** tests and may show a window stack, but **VTK/Mayavi will warn or fail OpenGL** without GPU/Mesa; this is expected.

## Optional: recreate env

```bash
cd /path/to/vox_implemnt
./.micromamba/micromamba create -y -p ./voxtool-env -f environment.yml
```

## Misc

- `view/pointcloud_viewer.py` references `PointCloudWidget` but does not define it and is **not imported** by the main app; treat as stub/dead code unless you extend it.
