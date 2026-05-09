from pathlib import Path


def scan_assets(path: Path):
    return [p for p in path.rglob("*") if p.is_file()]