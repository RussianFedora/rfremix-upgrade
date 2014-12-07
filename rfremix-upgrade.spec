Name:		rfremix-upgrade
Version:	21.3
Release:	1%{?dist}
Summary:	Upgrade Fedora to next version using yum upgrade (unofficial tool)

Group:		Applications/System
License:	GPLv2
URL:		https://github.com/xsuchy/fedora-upgrade
# Sources can be obtained by
# git clone git://github.com/xsuchy/fedora-upgrade.git
# cd fedora-upgrade
# tito build --tgz
Source0:	fedora-upgrade-%{version}.tar.gz
Patch0:		fedora-upgrade-21.3-rfremix.patch
BuildArch:	noarch

Requires:	yum
Requires:	yum-utils
Requires:	rpmconf
Requires:	libselinux-utils
Requires:	vim-enhanced
Requires:	wget
BuildRequires: asciidoc
BuildRequires: libxslt

%description
Upgrade Fedora to next version using yum upgrade.
This is attempt to automatize steps as listed here:
https://fedoraproject.org/wiki/Upgrading_Fedora_using_yum

This is an unofficial tool, for official Fedora-supported
upgrades please see the 'fedup' tool.

%prep
%setup -q -n fedora-upgrade-%{version}
%patch0 -p1 -b .rfremix

%build
a2x -d manpage -f manpage fedora-upgrade.8.asciidoc

%install
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_mandir}/man8
mkdir -p %{buildroot}%{_datadir}/%{name}/keys
install -m755 fedora-upgrade %{buildroot}%{_sbindir}/%{name}
install -m644 rfremix-upgrade.8 %{buildroot}/%{_mandir}/man8/
cp -a keys/* %{buildroot}%{_datadir}/%{name}/keys

%files
%doc LICENSE README.md
%{_sbindir}/rfremix-upgrade
%doc %{_mandir}/man8/rfremix-upgrade.8*
%{_datadir}/%{name}

%changelog
* Sun Dec  7 2014 Arkady L. Shane <ashejn@russianfedora.pro> - 21.3-1.R
- sync with upstream

* Mon Nov 13 2013 Arkady L. Shane <ashejn@russianfedora.ru> - 20.1-2.R
- fix russianfedora keys name

* Tue Oct 22 2013 Arkady L. Shane <ashejn@russianfedora.ru> - 20.1-1.R
- initial package based on fedora-upgrade
