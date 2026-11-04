%global debug_package %{nil}

Name:		sysc-clipboard
Version:	0.1.5
Release:	1
Summary:	Clipboard history daemon for sysc-shell
License:	BSD-3-Clause
Group:		Window Manager/Bar
URL:		https://github.com/Nomadcxx/sysc-clipboard
Source0:	https://github.com/Nomadcxx/sysc-clipboard/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:	%{name}-%{version}-vendor.tar.xz

BuildRequires:	golang

%description
Clipboard history for sysc-shell, with encrypted storage and a Go client.
Captures Wayland clipboard selections; sysc-shell draws the history panel.

%prep
%autosetup -p1
tar -xf %{S:1}

%build
go build -o %{name} ./cmd/%{name}/

%install
install -Dm644 contrib/sysc-clipboard.service %{buildroot}%{_userunitdir}/%{name}.service

%post
%systemd_user_post %{name}.service

%preun
%systemd_user_preun %{name}.service

%files
%license LICENSE NOTICE
%doc README.md
%{_userunitdir}/%{name}.service
