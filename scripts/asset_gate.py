#!/usr/bin/env python3
"""FAB Copilot: inspect asset metadata without reading, encoding or uploading data.

Advisory only. No service integration and no automatic human interruption.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ASSET_EXTENSIONS = {
    ".png", ".jpg", ".jpeg", ".webp", ".gif", ".svg", ".bmp", ".ico",
    ".mp3", ".ogg", ".wav", ".mp4", ".webm", ".glb", ".gltf", ".fbx",
    ".ttf", ".otf", ".woff", ".woff2", ".zip", ".apk", ".aab",
}
EXCLUDED_DIRECTORIES = {".git", ".venv", "node_modules", "__pycache__"}


def inspect_assets(
    root: Path,
    transport: str = "auto",
    single_limit: int = 256 * 1024,
    batch_limit: int = 2 * 1024 * 1024,
    count_limit: int = 12,
) -> dict:
    """Return only metadata and a context-dependent *advisory* decision."""
    if transport not in {"auto", "binary", "json-base64"}:
        raise ValueError("transport must be auto, binary or json-base64")
    if min(single_limit, batch_limit, count_limit) < 1:
        raise ValueError("limits must be positive")
    root = root.expanduser().resolve()
    if not root.is_dir():
        raise ValueError(f"not an accessible directory: {root}")

    entries = []
    for path in root.rglob("*"):
        if any(part in EXCLUDED_DIRECTORIES for part in path.relative_to(root).parts):
            continue
        if path.is_symlink() or not path.is_file():
            continue
        if path.suffix.lower() not in ASSET_EXTENSIONS:
            continue
        size = path.stat().st_size  # No file content read.
        entries.append({"path": path.relative_to(root).as_posix(), "bytes": size})

    entries.sort(key=lambda item: (-item["bytes"], item["path"]))
    total = sum(item["bytes"] for item in entries)
    # Base64 encodes each file separately. JSON/protocol overhead is not included.
    b64_estimate = sum(4 * ((item["bytes"] + 2) // 3) for item in entries)
    heavy = bool(entries) and (
        entries[0]["bytes"] >= single_limit
        or total >= batch_limit
        or len(entries) > count_limit
    )

    if not entries:
        decision, why = "continue", "No recognized assets in this directory."
    elif not heavy:
        decision, why = "continue", "Small batch; Base64 is acceptable if required."
    elif transport == "binary":
        decision, why = "continue", "A native binary transport is available; verify its actual limits."
    elif transport == "json-base64":
        decision, why = "human-handoff", (
            "Large batch with JSON/Base64-only transport: evaluate a direct "
            "binary route or an actionable handoff before starting the upload."
        )
    else:
        decision, why = "check-transport", (
            "Large batch: establish real transport capabilities before uploading."
        )
    return {
        "root": str(root),
        "transport": transport,
        "asset_count": len(entries),
        "total_bytes": total,
        "base64_estimated_bytes": b64_estimate,
        "base64_estimate_excludes": "JSON, protocol overhead and retries",
        "thresholds_are_advisory": True,
        "decision": decision,
        "reason": why,
        "largest_files": entries[:5],
        "other_files_count": max(0, len(entries) - 5),
        "no_bytes_read_or_uploaded": True,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", type=Path, help="Directory to inspect")
    parser.add_argument(
        "--transport", choices=("auto", "binary", "json-base64"), default="auto"
    )
    parser.add_argument("--single-kib", type=int, default=256)
    parser.add_argument("--batch-mib", type=int, default=2)
    parser.add_argument("--max-files", type=int, default=12)
    args = parser.parse_args()
    try:
        report = inspect_assets(
            args.directory,
            transport=args.transport,
            single_limit=args.single_kib * 1024,
            batch_limit=args.batch_mib * 1024 * 1024,
            count_limit=args.max_files,
        )
    except (ValueError, OSError) as exc:
        parser.error(str(exc))
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
