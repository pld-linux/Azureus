Summary:	Azureus - Java BitTorrent client
Summary(pl):	Azureus - klient BitTorrenta w Javie
Name:		Azureus
Version:	2.3.0.6
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://dl.sourceforge.net/azureus/%{name}_%{version}_source.zip
# Source0-md5:	d02357ee2917482fee1174a0dc549c5e
Source1:	%{name}.png
Source2:	%{name}.desktop
Source3:	%{name}.sh
Patch0:		%{name}-buildfile.patch
URL:		http://azureus.sourceforge.net/
BuildRequires:	eclipse-swt >= 3.1.1
BuildRequires:	jakarta-commons-cli
BuildRequires:	jakarta-log4j
BuildRequires:	jdk >= 1.4
BuildRequires:	unzip
Requires:	eclipse-swt >= 3.1.1
Requires:	jakarta-commons-cli
Requires:	jakarta-log4j
Requires:	jre >= 1.4
BuildArch:	noarch
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
%patch0 -p0

%build
rm -rf org/gudy/azureus2/platform/macosx/access
rm -rf org/gudy/azureus2/ui/swt/{osx,test}
##export ANT_OPTS=-Xmx128M
ant jar

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/Azureus,%{_pixmapsdir},%{_desktopdir},%{_bindir}}

install %{SOURCE1} $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE3} $RPM_BUILD_ROOT%{_bindir}/Azureus
install dist/Azureus2.jar $RPM_BUILD_ROOT%{_datadir}/Azureus/Azureus.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/Azureus
%{_desktopdir}/Azureus.desktop
%{_pixmapsdir}/Azureus.png
%{_datadir}/Azureus
