Name:	ranger	
Version:	1.5.4
Release:	3%{?dist}
Summary:	Vim-like file manager

Group:		System Environment/Shells
License:	GPLv3
URL:		http://savannah.nongnu.org/projects/ranger
Source0:	ranger-stable.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:	python-setuptools
Requires:	python-chardet atool mediainfo

%description
A console file manager with VI key bindings.

It provides a minimalistic and nice curses interface with a view on the
directory hierarchy.  The secondary task of ranger is to figure out which
program you want to use to open your files with.


%prep
%setup -q
echo "video/realmedia    rmvb" >> ranger/data/mime.types


%build
python setup.py build

%install
rm -rf %{buildroot}
python setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES
sed -i -e 's/ranger\.1/ranger.1.gz/' INSTALLED_FILES

%clean
rm -rf %{buildroot}


%files -f INSTALLED_FILES
%defattr(-,root,root,-)
%doc README CHANGELOG COPYING doc/HACKING doc/colorschemes.txt doc/print_colors.py doc/print_keys.py



%changelog

