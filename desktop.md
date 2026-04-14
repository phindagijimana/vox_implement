# Turning voxTool into a “desktop app”

## What you likely already have

Upstream [voxTool](https://github.com/pennmem/voxTool) is started with `python launch_pyloc.py` inside a Conda env (`vt`). That pattern usually means **a GUI already exists** (commonly Qt/PyQt or similar): a normal windowed program, not a headless script. In that sense it may **already be a desktop application** for anyone who can install Python/Conda and dependencies.

What people often mean by “make it a desktop app” is **distribution and polish**, not adding a GUI from scratch.

## What’s typically *remaining* for a packaged desktop product

### 1. One-click install (no Conda for end users)

- **Freeze / bundle** the app and dependencies into a single distributable (e.g. [PyInstaller](https://pyinstaller.org/), cx_Freeze, Nuitka, or Briefcase).
- **Per-platform builds:** Windows (`.exe` / installer), macOS (`.app` / `.dmg`), Linux (AppImage, `.deb`, or Flatpak)—each has its own packaging steps.
- **Pin dependency versions** and test the frozen build; bundled Qt/OpenGL stacks are a common source of “works in dev, fails in the bundle.”

### 2. App identity on the OS

- **Icons:** `.ico` (Windows), `.icns` (macOS), PNG/SVG for Linux desktop entries.
- **Desktop / Start Menu integration:** shortcuts, `Exec=` line, working directory, file associations (optional: open `.json` or CT paths with the app).
- **macOS:** app bundle layout, **code signing**, and **notarization** if you want Gatekeeper-friendly distribution.

### 3. If the GUI is thin or missing pieces (verify in code)

Only after cloning the repo, check whether anything still assumes a **terminal-first** workflow (e.g. paths only via CLI). Remaining work would then be **finishing the GUI** or **wrapping CLI in a small launcher**—but the public README describes a full button-driven workflow, so this may already be done.

## Feels like a *shipped product* (beyond “runs on my machine”)

Use this as a bar for external or clinical users—not only developers.

### Distribution and releases

- **Single artifact per platform** (installer or portable bundle), not “clone repo + conda.”
- **Versioned releases** with a **changelog** (semver or dated tags) and **known-good** dependency pins.
- **Clear upgrade path**: re-download, in-app update, or package-manager story for bundled builds (distinct from `conda env update`).

### First-run and day-to-day UX

- **Obvious launch**: Start Menu / Applications / dock with correct **icon** and **product name**.
- **Sensible defaults** and **recoverable errors**: what failed, what to try, where logs live (optional “open log folder”).
- **Stable paths when launched from a shortcut**: fix **current working directory** assumptions in Python GUIs; normalize resource and config paths.

### Trust and platform hygiene

- **Code signing** on **Windows and macOS** so users are not trained to bypass security warnings.
- **macOS notarization** if you distribute outside a locked-down lab.
- Awareness of **antivirus false positives** on PyInstaller-style bundles; plan for support when binaries get flagged.

### Quality bar

- **Smoke tests on clean machines** (VMs) for every OS you claim to support.
- **Regression checks** on representative CTs and JSON save/load workflows you care about.
- **Crash hygiene**: avoid silent failures; optional “report issue” that includes app version and OS.

### Documentation and support

- **One-page “install + first session”** (screenshots help).
- **Scope statement**: supported formats, known limits, and how to get help (IT, issue tracker, internal contact).

### Legal and packaging hygiene

- **LICENSE** clarity for your app and **third-party notices** (Qt, scientific stack, etc.) shipped with the installer or in an acknowledgments file.

## Practical takeaway

- **For lab/internal use:** Conda + `launch_pyloc.py` may be enough; focus on **documentation and reproducible environments**.
- **For clinicians or external sites:** expect **bundling, installers, OS integration, signing, tested releases, and support-grade docs**—often without much new core application logic.

To refine this list for *your* fork, clone the repo locally and confirm the GUI toolkit, entrypoint, and how assets (icons, `config.yml`) load under PyInstaller-style one-folder layouts.
