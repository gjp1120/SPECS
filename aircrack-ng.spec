# these bits are constant across distributions
#
Name:           aircrack-ng
Version:        1.1
Release:        1%{?dist}
Summary:        Reliable 802.11 (wireless) sniffer and WEP/WPA-PSK key cracker
License:        GPL
Source:         http://dl.aircrack-ng.org/%{name}-%{version}.tar.gz
URL:            http://www.aircrack-ng.org/
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires: openssl-devel glibc >= 2
Group: Productivity/Networking/Other



%description
aircrack-ng is a set of tools for auditing wireless networks. It's an
enhanced/reborn version of aircrack. It consists of airodump-ng (an 802.11
packet capture program), aireplay-ng (an 802.11 packet injection program),
aircrack (static WEP and WPA-PSK cracking), airdecap-ng (decrypts WEP/WPA
capture files), and some tools to handle capture files (merge, convert,
etc.).

%prep
%setup -q

%build
make %{?_smp_mflags} sqlite=true unstable=true

%install

rm -rf $RPM_BUILD_ROOT
mkdir $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT prefix=%{_prefix} mandir=%{_mandir}/man1 sqlite=true unstable=true

cd $RPM_BUILD_ROOT
find . -type d | sed '1,2d;s,^\.,\%attr(-\,root\,root) \%dir ,' > %{_builddir}/file.list.%{name}
find . -type f | sed 's,^\.,\%attr(-\,root\,root) ,' | grep -v /man/ >> %{_builddir}/file.list.%{name}
find . -type l | sed 's,^\.,\%attr(-\,root\,root) ,' >> %{_builddir}/file.list.%{name}

%files -f %{_builddir}/file.list.%{name}
%doc ChangeLog INSTALLING README LICENSE AUTHORS VERSION
%doc test
%doc patches
%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Sun Jan 29 2009 Xury <xury@poczta.onet.pl> aircrack-ng-1.0-rc3
- small fix and update spec file
* Mon Jun 26 2006 David Bolt <davjam@davjam.org> aircrack-ng-0.6
- Removed patch as no longer needed for SUSE 10.1 (GCC 4.1.2)
* Fri Jun  2 2006 David Bolt <davjam@davjam.org> aircrack-ng-0.5
- Patched source to build properly on SUSE 10.1 (GCC 4.1.2)
* Thu Mar 30 2006 David Bolt <davjam@davjam.org>
- First package built for SUSE
