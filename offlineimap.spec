Summary: Disconnected Universal IMAP Mail Synchronization/Reader Support
Name: offlineimap
Version: 6.5.5_rc2
Release: 2%{?dist}
Source0: offlineimap-6.5.5_rc2.tgz
License: GPLv2
Group: Applications/Internet
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildArch: noarch

Vendor: John Goerzen <john@complete.org>
Url: http://offlineimap.org

BuildRequires: python-docutils

%description
OfflineIMAP is a tool to simplify your e-mail reading. With OfflineIMAP, you can
read the same mailbox from multiple computers. You get a current copy of your
messages on each computer, and changes you make one place will be visible on all
other systems. For instance, you can delete a message on your home computer, and
it will appear deleted on your work computer as well. OfflineIMAP is also useful
if you want to use a mail reader that does not have IMAP support, has poor IMAP
support, or does not provide disconnected operation. It's homepage at
http://offlineimap.org contains more information, source code, and online
documentation.



%prep
%setup -q

%build
python setup.py build

%install
rm -rf %{buildroot}
python setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES
cd docs
make man
mkdir -p %{buildroot}%{_mandir}/man1/
cp -f offlineimap.1 %{buildroot}%{_mandir}/man1/

%clean
rm -rf %{buildroot}

%files -f INSTALLED_FILES
%defattr(-,root,root)
%{_mandir}/man1/offlineimap.1.gz

