# voxTool (pennmem/voxTool)

**What it is:** VoxTool 2.0 is a Python desktop application for **localizing intracranial electrodes** (e.g., SEEG, depth, grid, strip contacts) **on post-implant CT**. You work in 3D image space and export contact coordinates (and optionally derived bipolar midpoints).

**What it is not:** It is not a fully automated detector. Localization is **interactive**: you load the scan, tune display, define leads, and mark contacts on the CT.

**Typical workflow**

1. Load a CT and adjust the **CT threshold** so contacts are visible; update the view.
2. Optionally **load existing coordinates** from a JSON file to continue a prior session.
3. **Define leads**: names, geometry (e.g., grid rows × columns), types, and microcontact layout.
4. Select a lead, **click the CT** to place the next contact, and **Submit** (keyboard shortcut `S` is supported).
5. Use optional helpers:
   - **Seeding:** extrapolates remaining contact positions from points you already picked; results should be verified (duplicate locations can occur).
   - **Interpolate:** after marking ends of a strip/depth or corners of a grid, fills in intermediate contacts; may need another **Interpolate** pass.
6. **Add micro-contacts** where needed for macro/micro leads.
7. **Save** localized coordinates; if **Include Bipolar Pairs** is enabled, midpoints of neighboring pairs are saved too.

**Environment and launch (this repo):** see root **README.md** (`./vox install`, `./vox start -f`). Upstream originally used Conda env `vt` via `setup_env.sh`.

**Reference:** [https://github.com/pennmem/voxTool](https://github.com/pennmem/voxTool)
