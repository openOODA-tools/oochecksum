# oochecksum: Sovereign HASH VERIFIER

<div align="center">

```
================================================================================
                                oochecksum
               Sovereign openOODA HASH VERIFIER
================================================================================
```

**Sovereign HASH VERIFIER**  
*Unified integrity checking utility verifying BSD and GNU style checksum manifests.*  
*Two Faces, One Engine:* Modern terminal ergonomics for humans • Zero-leakage MCP for AI agents  
Written in 100% pure [openOODA](https://github.com/openOODA).

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![openOODA](https://img.shields.io/badge/openOODA-1.0-emerald.svg)](https://openooda.org)
[![Architecture: x86_64 | aarch64](https://img.shields.io/badge/Arch-x86__64%20%7C%20aarch64-lightgrey.svg)]()

</div>

---

## 1. Quick Install

### Automated Installer (Linux x86_64 & aarch64)
```bash
curl -fsSL https://openooda-tools.github.io/oochecksum/install.sh | bash
```

### Native Package Managers
```bash
# Arch Linux (AUR / PKGBUILD)
yay -S oochecksum-bin
# Or manual PKGBUILD:
cd packaging/arch && makepkg -si

# Debian / Ubuntu (.deb)
curl -fsSL https://openooda-tools.github.io/oochecksum/install.sh | bash -s -- --deb

# Fedora / RHEL (.rpm)
curl -fsSL https://openooda-tools.github.io/oochecksum/install.sh | bash -s -- --rpm
```

### Uninstallation
```bash
oochecksum-uninstall
# or: curl -fsSL https://openooda-tools.github.io/oochecksum/uninstall.sh | bash
```

---

## 2. CLI Usage

```
usage: oochecksum [options] [FILE]...

Unified integrity checking utility verifying BSD and GNU style checksum manifests.

Options:
  -c, --check <FILE>   read checksums from manifest file and verify
  -a, --algorithm <A>  algorithm override: sha256, sha512, md5, crc32 [default: auto]
      --tag            create BSD-style checksum manifest
      --status         don't output anything, status code shows success
  -q, --quiet          don't print OK for each successfully verified file
      --ignore-missing don't fail or report status for missing files
      --strict         exit non-zero for improperly formatted checksum lines
      --demo           verify sample embedded manifest
      --json           output formatted as JSON Lines
  -h, --help           display this help and exit
  -v, --version        output version information and exit
      --mcp            run as Model Context Protocol stdio server
```

---

## 3. Theming Integration (`oote`)

`oochecksum` synchronizes visual styles and status colors with [oote](https://github.com/openOODA-tools/oote):
* **Configuration:** Reads active palette from `~/.openooda/theme.oot`.
* **Environment Overrides:** Respects `$OODA_THEME` and `$NO_COLOR`.

---

## 4. Model Context Protocol (MCP)

When invoked with `--mcp`, `oochecksum` runs a JSON-RPC 2.0 stdio server providing structured tools for AI coding agents:

```bash
oochecksum --mcp
```

### Available Tools

* **`checksum_verify`**: Verify a BSD or GNU checksum manifest string against local files.
  * Parameters: `manifest` (string, required)
* **`checksum_generate`**: Generate BSD or GNU style manifest lines for file paths.
  * Parameters: `path` (string, required), `algorithm` (string, optional), `format` (string, optional)
* **`checksum_detect_format`**: Parse and classify a manifest line (detects algorithm and BSD vs GNU syntax).
  * Parameters: `line` (string, required)
* **`checksum_audit_tree`**: Audit a manifest file or directory for missing or failed checksums.
  * Parameters: `path` (string, optional)
* **`checksum_hash`**: Compute SHA-256 or CRC32 digest for string content.
  * Parameters: `content` (string, required), `algorithm` (string, optional)

---

## 5. Security & Zero Ambient Authority

* **Pure Capability Bounded:** Operates strictly with explicit tokens (&FsReadCap, &StreamCap, &McpCap). Physical absence of ambient disk/net leakage.
* **Negative-Trust Architecture:** Strict input validation and operational limits.
* **Hermetic Binary:** Standalone zero-dependency executable.

---

## 6. License

Apache License, Version 2.0. See [LICENSE](LICENSE) for details.
