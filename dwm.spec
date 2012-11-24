Name:	dwm	
Version:  6.0	
Release:	2%{?dist}
Summary:	dynamic window manager

Group:		User Interface/Desktops
License:	MIT/X
URL:		dwm.org
Source0:	dwm-6.0-gjp1120_patched.tgz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:  gcc	
#Requires:	

%description
dwm is an extremely fast, small, and dynamic window manager for X.

%prep
%setup -q


%build
make -j2

cd dwmstatus
make -j2

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
cd dwmstatus
make install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc README
/usr/bin/dwm
/usr/bin/dwmstatus
/usr/share/man/man1/dwm.1.gz
/usr/bin/dwm-session
/usr/share/fonts/bitmap/stlarch.pcf
/usr/share/xsessions/dwm.desktop

%exclude
/usr/share/fonts/bitmap/fonts.scale
/usr/share/fonts/bitmap/fonts.dir

%post
mkfontscale /usr/share/fonts/bitmap/
mkfontdir /usr/share/fonts/bitmap/
mkfontscale /usr/share/fonts/bitmap/

%postun
mkfontscale /usr/share/fonts/bitmap/
mkfontdir /usr/share/fonts/bitmap/
mkfontscale /usr/share/fonts/bitmap/


%changelog

