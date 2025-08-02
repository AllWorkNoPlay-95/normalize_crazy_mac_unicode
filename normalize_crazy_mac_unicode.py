#!/usr/bin/env python3
# normalize_crazy_mac_unicode.py
#
# MacOS e gli accenti strani non vanno d’accordo.
# Questo script normalizza i nomi dei file in formato NFD.
# Utile quando nemmeno il Terminale trova i file.

import os
import unicodedata
import argparse


def normalize(path, strip_accents=False):
    # Rinomina ricorsivamente file e directory in NFD
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files + dirs:
            old_path = os.path.join(root, name)
            new_name = unicodedata.normalize("NFD", name)
            if strip_accents:
                new_name = remove_accents(new_name)
            new_path = os.path.join(root, new_name)

            if new_path != old_path:
                try:
                    os.rename(old_path, new_path)
                    print(f"✅ {old_path} -> {new_path}")
                except Exception as e:
                    print(f"⚠️  Errore su {old_path}: {e}")


def remove_accents(text: str) -> str:
    normalized = unicodedata.normalize("NFD", text)
    return "".join(c for c in normalized if not unicodedata.combining(c))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Normalize file and directory names to NFD (macOS-friendly)."
    )
    parser.add_argument("path", help="Path to target directory")
    parser.add_argument(
        "--no-accents",
        action="store_true",
        help="Remove accents entirely after normalization",
    )

    args = parser.parse_args()

    normalize(args.path, strip_accents=args.no_accents)
