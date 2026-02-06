Name:           helm
Version:        4.1.0
Release:        1%{?dist}
Summary:        Helm helps you manage Kubernetes applications — Helm Charts help you define, install, and upgrade even the most complex Kubernetes application.
URL:            https://github.com/helm/helm
License:        Apache-2.0
Source0:        https://github.com/helm/helm/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  golang
BuildRequires:  git

Provides:       %{name} = %{version}

%description
Helm helps you manage Kubernetes applications — Helm Charts help you define, install, and upgrade even the most complex Kubernetes application.

%global debug_package %{nil}

%prep
%autosetup


%build
%make_build


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}/
cp bin/%{name} %{buildroot}%{_bindir}/




%check
# go test should be here... :)

# %post


# %preun


%files
%{_bindir}/%{name}
%license LICENSE
%doc README.md


%changelog
* Fri August 16 2024 Yannik Mueller - 3.15.4-1
- Initial release
