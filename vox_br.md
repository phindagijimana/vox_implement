# Builder Review — voxTool (intracranial localization on CT)

Evaluation of the **pennmem/voxTool** stack and this repository’s **modernized implementation** (Python 3, conda-forge environment, `vox` CLI, code fixes). The review follows a consistent set of dimensions (usability, reproducibility, performance, generalization, clinical relevance, interpretability and trust, comparison to alternatives, limitations, integration potential, builder insight) in a single linear document—without grouping labels or use-case rhetorical prompts.

**Primary reference:** [pennmem/voxTool](https://github.com/pennmem/voxTool) (GUI for interactive SEEG/ECoG-style contact localization on post-implant CT; JSON coordinate export).

**Local kit:** this repository (`voxTool/` sources, `environment.yml`, `implementation.md`, `./vox`).

---

## Context

voxTool is an interactive desktop application: load CT, threshold for contact visibility, define leads (geometry and naming), click contacts in 3D/slice views, optional seeding/interpolation, save coordinates (and optional bipolar midpoints). Upstream targets a legacy **Python 2.7 / PyQt4 / old VTK** stack; that environment is no longer practical on current Linux distributions. This repo vendors upstream code with a **Python 3.10 + VTK/Mayavi/PySide6-via-pyface** path, a reproducible `environment.yml`, and operational helpers (`install`, `check`, `start`, `stop`, `logs`).

---

## Usability

**Published / upstream**

- README documents workflow, shortcuts, and Conda-based setup (`setup_env.sh`, env name `vt`).
- Code is compact and readable; MIT license.

**This implementation**

- `./vox install` bootstraps micromamba (if needed) and creates `voxtool-env/` from pinned conda-forge specs.
- `./vox check` verifies Python and that `PylocControl` imports under an offscreen Qt platform.
- `./vox start -f` is the straightforward path on a workstation with a display; background mode writes `.vox/voxtool.log`.

**Friction**

- **Display and OpenGL:** Mayavi/VTK need a real graphics stack; headless or broken GL produces warnings or blank 3D views—not a “pip install and go” web app.
- **Operator skill:** users must understand lead layouts, CT quality, and when seeding/interpolation is unreliable (upstream README already flags duplicate locations and ordering issues).

---

## Reproducibility

**What aligns with upstream behavior**

- Same entrypoint conceptually: `launch_pyloc.py`, `config.yml`, lead/contact model and save semantics described in upstream README.

**What changed in this fork**

- Interpreter, Qt bindings, VTK major version, and matplotlib backends differ; behavior should be validated on representative CTs after any upgrade.
- `view/slice_viewer.py` dropped an unused Traits/Mayavi scene hook on a matplotlib canvas that **segfaulted** on import with modern stacks; slice views remain matplotlib-based.

**Sensitivity**

- Threshold choice, CT acquisition, and manual clicking dominate repeatability across operators; the tool does not automate contact detection.

---

## Performance

- Latency and responsiveness depend on volume size, GPU/CPU, and VTK scene complexity; no formal benchmarks ship with upstream or this repo.
- Expectation for a builder: **interactive** performance on typical clinical CT volumes on a normal workstation, not batch HPC scaling.

---

## Generalization

- **Scanners, kernels, implants, and reconstruction** vary; threshold and visualization settings are study-specific.
- **No pretrained model** assigns contacts automatically; cross-site harmonization is manual QC and operator judgment.
- Seeding and interpolation are **heuristics**; failure modes increase with unusual grid geometries or artifact-heavy CTs.

---

## Clinical relevance

- Outputs are **research and surgical-planning adjuncts** in typical use: named contacts and coordinates (and optional bipolar midpoints) for downstream registration or analysis.
- The workflow assumes **research-grade** interaction with NIfTI (or supported) CT and time for expert review—not a silent clinical device.

---

## Interpretability and trust

- **Strength:** Every contact placement is **explicit** (user click + submit); the state is inspectable in the UI and in exported JSON.
- **Trust depends on:** CT artifact review, consistency of lead definitions, and double-checking seeding/interpolation results (upstream documents known pitfalls).

---

## Comparison to existing methods

- Alternatives include other commercial or in-house localization tools, atlas-based pipelines, and fully manual coordinate logging. voxTool’s niche is **open-source, CT-centric, interactive** localization with a small codebase.
- This implementation’s differentiator versus stock upstream is **runnable modern dependency pins** plus a small **CLI** for environment lifecycle—not new segmentation algorithms.

---

## Limitations and failure modes

- Legacy upstream `conda_env.yml` is **not** reproduced; only the modern `environment.yml` path is supported here.
- **Background GUI start** without a proper `DISPLAY` (and sometimes even with it) is unreliable; foreground use on a desktop session is the robust pattern.
- **Incomplete / stub files** in upstream (e.g. `pointcloud_viewer` references undefined widgets) remain unaddressed unless extended locally.
- **Signed installers, auto-update, and enterprise packaging** are out of scope in this repo unless added separately.

---

## Integration potential

- **Natural adjacencies:** BIDS layouts, FreeSurfer/SVG brains, MNE-Python or other tools consuming contact JSON; containerized neuroimaging environments for preprocessing before CT load.
- **Format boundaries:** exports are driven by voxTool’s JSON convention; downstream tools must map fields and coordinate frames explicitly.

---

## Builder insight

The scientific value of voxTool is **workflow capture** (structured leads + saved coordinates), not fully automated localization. The highest-leverage engineering work is **keeping the GUI stack viable** (Python, Qt, VTK, Mayavi) and documenting **display/OpenGL prerequisites**. A practical roadmap for a maintainer: pin versions in CI with `vox check`, add one or two **smoke tests** on tiny synthetic NIfTI volumes where legal, and optionally contribute the Python 3 delta **upstream** so the community shares one fork line.

---

## References (selected)

- [pennmem/voxTool](https://github.com/pennmem/voxTool) — upstream application and README.
- `implementation.md` — environment and patch notes for this repo.

Last updated: 2026-04-14.
