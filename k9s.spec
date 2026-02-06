Name:           k9s
Version:        0.50.18
Release:        1%{?dist}
Summary:        K9s provides a terminal UI to interact with your Kubernetes clusters
URL:            https://k9scli.io/
License:        Apache-2.0
Source0:        https://github.com/derailed/k9s/archive/refs/tags/v%{version}.tar.gz
# Source0:        sealed-secrets-0.27.1.tar.gz

BuildRequires: golang
BuildRequires: git

Provides:       %{name} = %{version}

%description
K9s provides a terminal UI to interact with your Kubernetes clusters. The aim of this project is to make it easier to navigate, observe and manage your applications in the wild. K9s continually watches Kubernetes for changes and offers subsequent commands to interact with your observed resources.

%global debug_package %{nil}

%prep
%autosetup


%build
CGO_ENABLED=1 go build -o %{name} -ldflags "-w -s -X github.com/derailed/%{name}/cmd.version=%{version} -linkmode=external" main.go


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}/
cp %{name} %{buildroot}%{_bindir}/




%check
go clean --testcache && go test ./...

# %post


# %preun


%files
%{_bindir}/k9s
%license LICENSE
%doc README.md


%changelog
* Tue August 27 2024 Yannik Mueller - 0.23.5-1
- Initial release
