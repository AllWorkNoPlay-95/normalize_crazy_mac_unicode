#!/usr/bin/env python3
# normalize_crazy_mac_unicode.py
#
# MacOS e gli accenti strani non vanno d’accordo.
# Questo script normalizza i nomi dei file in formato NFD.
# Utile quando nemmeno il Terminale trova i file.

import os
import unicodedata


def normalize(path):
    # Rinomina ricorsivamente file e directory in NFD
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files + dirs:
            old_path = os.path.join(root, name)
            new_name = unicodedata.normalize("NFD", name)
            new_path = os.path.join(root, new_name)

            if new_path != old_path:
                try:
                    os.rename(old_path, new_path)
                    print(f"✅ {old_path} -> {new_path}")
                except Exception as e:
                    print(f"⚠️  Errore su {old_path}: {e}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:  # Ci serve almeno un argomento
        print("Usage: python3 normalize_unicode_mac.py <path>")
        sys.exit(1)

    normalize(sys.argv[1])
