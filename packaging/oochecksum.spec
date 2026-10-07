Name:           oochecksum
Version:        0.1.0
Release:        1%{?dist}
Summary:        Unified integrity checking utility verifying BSD and GNU style checksum manifests.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oochecksum
Source0:        oochecksum-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oochecksum is a sovereign, capability-bounded HASH VERIFIER written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oochecksum
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oochecksum-uninstall

%files
/usr/bin/oochecksum
/usr/bin/oochecksum-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
