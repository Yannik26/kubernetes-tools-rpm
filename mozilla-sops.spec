Name:           sops
Version:        3.9.1
Release:        1%{?dist}
Summary:        sops is an editor of encrypted files that supports YAML, JSON, ENV, INI and BINARY formats and encrypts with AWS KMS, GCP KMS, Azure Key Vault, age, and PGP

License:        MPL-2.0
Source0:        https://github.com/mozilla/sops/archive/refs/tags/v%{version}.tar.gz
URL:            https://github.com/mozilla/sops

BuildRequires:  golang
BuildRequires: rubygems
# BuildRequires:  systemd-rpm-macros

Provides:       %{name} = %{version}

%description
sops is an editor of encrypted files that supports YAML, JSON, ENV, INI and BINARY formats and encrypts with AWS KMS, GCP KMS, Azure Key Vault, age, and PGP.

%global debug_package %{nil}

%prep
%autosetup


%build
# rm -rf tmppkg
# mkdir -p tmppkg/usr/local/bin
GOPROXY=https://proxy.golang.org go mod tidy
GOPROXY=https://proxy.golang.org go mod vendor

CGO_ENABLED=1 GOPROXY=https://proxy.golang.org go build -mod vendor -ldflags=-linkmode=external -o %{name} github.com/getsops/sops/v3/cmd/sops


%install
install -Dpm 0755 %{name} %{buildroot}%{_bindir}/%{name}

%check
# go test should be here... :)

%post


%preun


%files
%{_bindir}/%{name}
%license LICENSE
%doc README.rst


%changelog
* Fri August 16 2024 Yannik Müller - 3.9.0-1
- Updated to upstream version 3.9.0
- changes build command to reflect ustream changes in go build command
* Wed June 14 2023 Yannik Müller - 3.7.3-1
- Initial release
