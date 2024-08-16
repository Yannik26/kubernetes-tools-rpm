Name:           helm
Version:        3.13.3
Release:        1%{?dist}
Summary:        Helm helps you manage Kubernetes applications — Helm Charts help you define, install, and upgrade even the most complex Kubernetes application.
URL:            https://github.com/helm/helm
License:        Apache-2.0
Source0:        helm-%{version}.tar.gz


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
cp %{_bindir}/%{name} %{buildroot}%{_bindir}/




%check
# go test should be here... :)

# %post


# %preun


%files
%{_bindir}/%{name}
%license LICENSE
%doc README.md


%changelog
* Wed January 17 2024 Yannik Mueller - 3.13.3-1
- Initial release
