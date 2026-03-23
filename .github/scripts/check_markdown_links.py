#!/usr/bin/env python3

from __future__ import annotations

import concurrent.futures
import pathlib
import re
import ssl
import sys
import urllib.error
import urllib.request

URL_RE = re.compile(r"https?://[^\s)>\"']+")
SKIP_PREFIXES = (
    "https://example.com",
    "https://github.com/example/",
    "https://huggingface.co/example/",
)
SKIP_EXACT = {
    "https://github.com",
    "https://arxiv.org",
}


def extract_urls(path: pathlib.Path) -> set[str]:
    text = path.read_text(encoding="utf-8")
    urls: set[str] = set()
    in_fence = False

    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        for url in URL_RE.findall(line):
            if url in SKIP_EXACT or any(url.startswith(prefix) for prefix in SKIP_PREFIXES):
                continue
            if "2401.xxxxx" in url:
                continue
            urls.add(url.rstrip(".,"))

    return urls


def check_url(url: str) -> tuple[str, str]:
    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE
    headers = {"User-Agent": "Mozilla/5.0 (compatible; awesome-arabic-ai-link-checker/1.0)"}

    for method in ("HEAD", "GET"):
        try:
            request = urllib.request.Request(url, method=method, headers=headers)
            with urllib.request.urlopen(request, timeout=20, context=context) as response:
                return ("ok", f"{response.getcode()} {url} -> {response.geturl()}")
        except urllib.error.HTTPError as error:
            if error.code == 429:
                return ("warn", f"rate-limited {url}")
            if method == "GET":
                return ("fail", f"{error.code} {url}")
        except Exception as error:
            last_error = f"{type(error).__name__} {url}"

    return ("fail", last_error)


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print("usage: check_markdown_links.py <path> [<path> ...]", file=sys.stderr)
        return 2

    all_urls: set[str] = set()
    for raw_path in argv[1:]:
        all_urls.update(extract_urls(pathlib.Path(raw_path)))

    failures: list[str] = []
    warnings: list[str] = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=12) as executor:
        futures = {executor.submit(check_url, url): url for url in sorted(all_urls)}
        for future in concurrent.futures.as_completed(futures):
            status, message = future.result()
            if status == "fail":
                failures.append(message)
            elif status == "warn":
                warnings.append(message)
            print(message)

    if warnings:
        print("\nWarnings:", file=sys.stderr)
        for warning in warnings:
            print(f"- {warning}", file=sys.stderr)

    if failures:
        print("\nBroken links:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
