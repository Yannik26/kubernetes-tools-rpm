Name:           sealed-secrets
Version:        0.27.1
Release:        1%{?dist}
Summary:        Encrypt your Secret into a SealedSecret, which is safe to store - even inside a public repository. The SealedSecret can be decrypted only by the controller running in the target cluster and nobody else (not even the original author) is able to obtain the original Secret from the SealedSecret.
URL:            https://github.com/bitnami-labs/sealed-secrets
License:        Apache-2.0
# Source0:        https://github.com/bitnami-labs/sealed-secrets/archive/refs/tags/v%{version}.tar.gz
Source0:        sealed-secrets-0.27.1.tar.gz

BuildRequires:  golang

Provides:       kubeseal = %{version}

%description
Encrypt your Secret into a SealedSecret, which is safe to store - even inside a public repository. The SealedSecret can be decrypted only by the controller running in the target cluster and nobody else (not even the original author) is able to obtain the original Secret from the SealedSecret.

%global debug_package %{nil}

%prep
%autosetup


%build
%make_build


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}/
cp kubeseal %{buildroot}%{_bindir}/




# %check
# make test

# %post


# %preun


%files
%{_bindir}/kubeseal
%license LICENSE
%doc README.md


# %changelog
# * Wed January 17 2024 Yannik Mueller - 3.13.3-1
# - Initial release
