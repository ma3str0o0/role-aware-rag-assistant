"""Build the desktop app (Windows .exe or macOS app folder) with PyInstaller.

    pip install -r requirements.txt pyinstaller==6.16.0
    python packaging/build_exe.py            # -> dist/UniAssist/UniAssist(.exe), zipped to dist/UniAssist-<os>.zip

The app is a folder build (not one single file): the search index and the downloaded university
documents are written next to the program, so they survive restarts. The universities' texts are not
bundled (they are downloaded on first start, as with `python run_demo.py`); the mock documents,
the access registers and the document manifest are.
GitHub Actions builds the Windows version on every version tag (.github/workflows/build-exe.yml).
"""
import os
import platform
import shutil
import sys
from pathlib import Path

import PyInstaller.__main__

ROOT = Path(__file__).resolve().parents[1]
SEP = os.pathsep  # PyInstaller's --add-data separator (";" on Windows, ":" elsewhere)

DATA = [
    ("app.py", "."),
    ("api.py", "."),
    ("src", "src"),
    ("data/docs", "data/docs"),
    ("data/access_register.csv", "data"),
    ("data/real/access_register.csv", "data/real"),
    ("data/real/manifest.csv", "data/real"),
    ("data/real/hashes.csv", "data/real"),
]


def main():
    args = [
        str(ROOT / "run_demo.py"),
        "--name", "UniAssist",
        "--noconfirm", "--clean", "--console",
        "--distpath", str(ROOT / "dist"), "--workpath", str(ROOT / "build"), "--specpath", str(ROOT / "build"),
        "--paths", str(ROOT),
        # Packages that load parts of themselves at run time.
        "--collect-all", "streamlit", "--collect-all", "chromadb", "--collect-all", "chromadb_rust_bindings",
        "--copy-metadata", "streamlit", "--copy-metadata", "chromadb",
        "--hidden-import", "api", "--hidden-import", "uvicorn.logging", "--hidden-import", "uvicorn.loops.auto",
        "--hidden-import", "uvicorn.protocols.http.auto", "--hidden-import", "uvicorn.lifespan.on",
    ]
    for mod in ("src", "src.agents"):
        args += ["--collect-submodules", mod]
    for src, dest in DATA:
        args += ["--add-data", f"{ROOT / src}{SEP}{dest}"]
    PyInstaller.__main__.run(args)

    name = {"Windows": "windows", "Darwin": "macos"}.get(platform.system(), platform.system().lower())
    archive = shutil.make_archive(str(ROOT / "dist" / f"UniAssist-{name}"), "zip", ROOT / "dist", "UniAssist")
    print(f"\nBuilt {ROOT / 'dist' / 'UniAssist'} and {archive}")


if __name__ == "__main__":
    sys.exit(main())
