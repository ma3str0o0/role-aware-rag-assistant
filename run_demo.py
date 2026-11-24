"""Start the whole demo with one command (macOS, Linux and Windows).

    python run_demo.py                 # Dubai corpus (31 real documents, 11 universities)
    python run_demo.py --corpus mock   # 13 mock documents only: no downloads, starts in seconds
    python run_demo.py --api-port 8010 --ui-port 8511   # if 8000/8501 are already in use

What it does:
1. downloads the public university documents if they are not there yet (dubai/real corpus only);
2. builds the search index for the chosen corpus;
3. starts the API (port 8000) with the demo controls on and the web page (port 8501);
4. opens http://localhost:8501 in your browser. Press Ctrl+C to stop both.

The same file is the entry point of the Windows/macOS app built with PyInstaller (packaging/build_exe.py).
A frozen app has no separate Python, so it starts copies of itself with an internal role flag
(--serve-api, --serve-ui, --fetch, --ingest) instead of `python -m ...`.
"""
import argparse
import os
import signal
import subprocess
import sys
import time
import urllib.request
import webbrowser
from pathlib import Path

FROZEN = getattr(sys, "frozen", False)
# In the built app the project files sit next to the bundled libraries (sys._MEIPASS).
ROOT = Path(getattr(sys, "_MEIPASS", Path(__file__).resolve().parent))
ROLES = ("--serve-api", "--serve-ui", "--fetch", "--ingest")


def command(role, *args):
    """How to start one part of the demo: `python -m ...` from source, the app itself when frozen."""
    if FROZEN:
        return [sys.executable, role, *args]
    py = sys.executable
    return {"--serve-api": [py, "-m", "uvicorn", "api:app", "--port", *args],
            "--serve-ui": [py, "-m", "streamlit", "run", "app.py", "--server.headless", "true",
                           "--server.port", *args, "--server.address", "localhost",
                           "--browser.gatherUsageStats", "false"],
            "--fetch": [py, "-m", "src.fetch_real"],
            "--ingest": [py, "-m", "src.ingest"]}[role]


def serve(role, args):
    """Runs one part in this process (only used by the built app)."""
    os.chdir(ROOT)
    sys.path.insert(0, str(ROOT))
    if role == "--serve-api":
        import uvicorn
        from api import app
        uvicorn.run(app, host="127.0.0.1", port=int(args[0]))
    elif role == "--serve-ui":
        from streamlit.web import cli as stcli
        sys.argv = ["streamlit", "run", str(ROOT / "app.py"), "--server.headless", "true",
                    "--server.port", args[0], "--server.address", "localhost",
                    "--browser.gatherUsageStats", "false", "--global.developmentMode", "false"]
        sys.exit(stcli.main())
    elif role == "--fetch":
        from src import fetch_real
        sys.argv = ["fetch_real"]
        fetch_real.main()
    elif role == "--ingest":
        from src.ingest import ingest
        from src import config
        _, n = ingest()
        print(f"Stored {n} chunks in {config.CHROMA_DIR} (mode={config.MODE})")


def run(cmd, env):
    print("$", " ".join(cmd), flush=True)
    subprocess.run(cmd, cwd=ROOT, env=env, check=True)


def wait_for(url, seconds=90):
    for _ in range(seconds):
        try:
            urllib.request.urlopen(url, timeout=2)
            return True
        except Exception:
            time.sleep(1)
    return False


def _stop_on_signal(*_):
    raise KeyboardInterrupt  # closing the terminal or `kill` stops the servers too, not only Ctrl+C


def main():
    if len(sys.argv) > 1 and sys.argv[1] in ROLES:
        return serve(sys.argv[1], sys.argv[2:])
    for sig in ("SIGTERM", "SIGHUP"):
        if hasattr(signal, sig):
            signal.signal(getattr(signal, sig), _stop_on_signal)
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--corpus", choices=["dubai", "real", "mock"], default="dubai")
    ap.add_argument("--no-browser", action="store_true", help="do not open the browser")
    ap.add_argument("--api-port", type=int, default=8000)
    ap.add_argument("--ui-port", type=int, default=8501)
    args = ap.parse_args()

    api_url = f"http://localhost:{args.api_port}"
    ui_url = f"http://localhost:{args.ui_port}"
    env = {**os.environ, "RAG_CORPUS": args.corpus, "DEMO_MODE": "1", "PYTHONUTF8": "1", "API_URL": api_url,
           "PYTHONUNBUFFERED": "1"}

    if args.corpus != "mock":
        docs = ROOT / "data" / "real" / "docs"
        if not docs.exists() or len(list(docs.glob("*.md"))) < 31:
            print("\n[1/3] Downloading the public university documents (about a minute)...")
            run(command("--fetch"), env)
        else:
            print("\n[1/3] University documents already downloaded.")
    else:
        print("\n[1/3] Mock corpus: nothing to download.")

    print(f"\n[2/3] Building the search index for the '{args.corpus}' corpus...")
    run(command("--ingest"), env)

    print(f"\n[3/3] Starting the API (port {args.api_port}) and the web page (port {args.ui_port})...")
    procs = [
        subprocess.Popen(command("--serve-api", str(args.api_port)), cwd=ROOT, env=env),
        # Only reachable from this computer, and no usage statistics sent to Streamlit.
        subprocess.Popen(command("--serve-ui", str(args.ui_port)), cwd=ROOT, env=env),
    ]
    try:
        if wait_for(f"{api_url}/health") and wait_for(ui_url):
            print(f"\n  UniAssist is running:  {ui_url}   (Ctrl+C to stop)\n", flush=True)
            if not args.no_browser:
                webbrowser.open(ui_url)
        else:
            print("\n  The servers did not start. Check the messages above.")
        while all(p.poll() is None for p in procs):
            time.sleep(1)
    except KeyboardInterrupt:
        pass
    finally:
        print("\nStopping...")
        for p in procs:
            if p.poll() is None:
                if os.name == "nt":
                    p.terminate()
                else:
                    p.send_signal(signal.SIGINT)
        for p in procs:
            try:
                p.wait(timeout=10)
            except subprocess.TimeoutExpired:
                p.kill()


if __name__ == "__main__":
    import multiprocessing
    multiprocessing.freeze_support()
    main()
