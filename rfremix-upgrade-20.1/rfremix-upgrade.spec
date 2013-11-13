Name:		rfremix-upgrade
Version:	20.1
Release:	1%{?dist}
Summary:	Upgrade RFRemix to next version using yum upgrade (unofficial tool)

Group:		Applications/System
License:	GPLv2
URL:		https://github.com/xsuchy/rfremix-upgrade
# Sources can be obtained by
# git clone git://github.com/xsuchy/rfremix-upgrade.git
# cd rfremix-upgrade
# tito build --tgz
Source0:	%{name}-%{version}.tar.xz
BuildArch:	noarch

Requires:	yum
Requires:	yum-utils
Requires:	rpmconf
Requires:	libselinux-utils
Requires:	vim-enhanced
BuildRequires: asciidoc
BuildRequires: libxslt

%description
Upgrade RFRemix to next version using yum upgrade.
This is attempt to automatize steps as listed here:
https://fedoraproject.org/wiki/Upgrading_Fedora_using_yum

This is an unofficial tool, for official Fedora-supported
upgrades please see the 'fedup' tool.

%prep
%setup -q

%build
a2x -d manpage -f manpage rfremix-upgrade.8.asciidoc

%install
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_mandir}/man8
mkdir -p %{buildroot}%{_datadir}/%{name}/keys
install -m755 rfremix-upgrade %{buildroot}%{_sbindir}
install -m644 rfremix-upgrade.8 %{buildroot}/%{_mandir}/man8/
cp -a keys/* %{buildroot}%{_datadir}/%{name}/keys

%files
%doc LICENSE README.md
%{_sbindir}/rfremix-upgrade
%doc %{_mandir}/man8/rfremix-upgrade.8*
%{_datadir}/%{name}

%changelog
* Tue Oct 22 2013 Arkady L. Shane <ashejn@russianfedora.ru> - 20.1-1
- initial package based on fedora-upgrade
