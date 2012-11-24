Name:	rxvt-unicode	
Version:	9.15
Release:	1%{?dist}
Summary:	URxvt is a heavily modified version of xvt, a VT102 emulator for the X window system

Group:		X11/Terminal
License:  GPLv2
URL:	http://software.schmorp.de/pkg/rxvt-unicode.html	
Source0:	  rxvt-unicode-9.15.tar.bz2
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:	gcc perl-devel
Requires:	perl 

%description
rxvt-unicode, version 9.15, is a colour vt102 terminal
emulator intended as an xterm(1) replacement for users who do not
require features such as Tektronix 4014 emulation and toolkit-style
configurability. As a result, rxvt-unicode uses much less swap space --
a significant advantage on a machine serving many X sessions.


%prep
%setup -q


%build
%configure --enable-everything --enable-256-color
make -j2


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc
%dir /usr/lib/urxvt
%dir /usr/share/man
/usr/bin/urxvt
/usr/bin/urxvtc
/usr/bin/urxvtd

/usr/lib/urxvt/perl/*
/usr/lib/urxvt/urxvt.pm
/usr/share/man/*
#   /usr/share/man/man1/urxvtc.1.gz
#   /usr/share/man/man1/urxvtd.1.gz
#   /usr/share/man/man3/urxvtperl.3.gz
#   /usr/share/man/man7/urxvt.7.gz

%changelog

