# normalize_crazy_mac_unicode

Script Python per normalizzare i nomi di file e cartelle nel formato Unicode **NFD**, compatibile con i sistemi macOS.

## 📌 Contesto

macOS utilizza la normalizzazione Unicode **NFD** (Normalization Form Decomposed) per i nomi dei file. Tuttavia, molti filesystem (es. exFAT, NTFS) e sistemi operativi usano **NFC** (composed). Questo mismatch può causare problemi durante:

- l'uso di `rsync`, `find`, `git`, ecc.;
- la ricerca o copia di file con caratteri accentati;
- l'accesso da Terminale a file che “esistono ma non si trovano”.

## ⚙️ Funzionalità

- Normalizza i nomi dei file e delle directory in Unicode NFD.
- Opera ricorsivamente su tutta la struttura della directory indicata.
- Supporta solo file system accessibili da Python (via `os.walk` e `os.rename`).

## 🧱 Requisiti

- Python 3.x (presente di default su macOS)
- Nessuna dipendenza esterna

## 🚀 Utilizzo

```bash
python3 normalize_crazy_mac_unicode.py /path/to/target_directory
```

---

# 🇬🇧 English

# normalize_crazy_mac_unicode

Python script to normalize file and folder names to Unicode **NFD**, ensuring compatibility with macOS filesystems.

## 📌 Context

macOS uses Unicode **NFD** (Normalization Form Decomposed) for filenames, while many filesystems (e.g., exFAT, NTFS) and operating systems use **NFC** (composed). This mismatch can lead to issues when:

- using `rsync`, `find`, `git`, etc.;
- searching or copying files with accented characters;
- accessing files from Terminal that “exist but cannot be found”.

## ⚙️ Features

- Recursively normalizes file and directory names to Unicode NFD.
- Operates directly on the provided directory.
- Uses only standard Python (`os.walk`, `os.rename`).

## 🧱 Requirements

- Python 3.x (pre-installed on macOS)
- No external dependencies

## 🚀 Usage

```bash
python3 normalize_crazy_mac_unicode.py /path/to/target_directory
