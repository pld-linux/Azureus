Summary:	Azureus - Java BitTorrent blient
Summary(pl):	Azureus - klient BitTorrenta w Javie
Name:		Azureus
Version:	2.1.0.4
Release:	0.1
License:	GPL
Group:		Applications/Networking
Source0:	http://dl.sourceforge.net/azureus/%{name}_%{version}_source.zip
# Source0-md5:	372fd6920f490ad3bc696c3ac23b0fb2
# Source0-size:	2688856
URL:		http://azureus.sourceforge.net/
BuildRequires:	someone-who-will-finish-this-spec
BuildRequires:	SEDA
# we need SWT (whatever is it), not whole eclipse...  do we?
BuildRequires:	eclipse
BuildRequires:	jakarta-commons-cli
BuildRequires:	jakarta-log4j
BuildRequires:	jdk
Requires:	jre
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Azureus provides a BitTorrent protocol implementation using Java
language. It offers multiple torrent downloads, queuing/priority
systems (on torrents and files), start/stop seeding options and
instant access to numerous pieces of information about your torrents.
Azureus now features an embedded tracker easily set up and ready to
use.

%description -l pl
Azureus dostarcza implementacjê protoko³u BitTorrent napisan± w jêzyku
Java. Oferuje ¶ciaganie wielopotokowe, systemy kolejkowania i
priorytetów (dla potoków i plików), opcje zatrzymywania i wznawiania
oraz bezpo¶redni dostêp do wielu czê¶ci informacji o potokach. Azureus
zawiera teraz wbudowany tracker ³atwy do skonfigurowania i u¿ywania.

%prep
%setup -q -c

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
