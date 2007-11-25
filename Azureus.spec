Summary:	Azureus - Java BitTorrent client
Summary(pl.UTF-8):	Azureus - klient BitTorrenta w Javie
Name:		Azureus
Version:	2.5.0.0
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://dl.sourceforge.net/azureus/%{name}_%{version}_source.zip
# Source0-md5:	f487f75f37674820bd3b2cc6af97ce57
Source1:	%{name}.png
Source2:	%{name}.desktop
Source3:	%{name}.sh
Patch0:		%{name}-buildfile.patch
Patch1:		%{name}-nomacosx.patch
Patch2:		%{name}-swt31.patch
URL:		http://azureus.sourceforge.net/
BuildRequires:	eclipse-swt >= 3.1.1
BuildRequires:	jakarta-commons-cli
BuildRequires:	jdk >= 1.4
BuildRequires:	logging-log4j
BuildRequires:	unzip
Requires:	eclipse-swt >= 3.1.1
Requires:	jakarta-commons-cli
Requires:	jre >= 1.4
Requires:	logging-log4j
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Azureus provides a BitTorrent protocol implementation using Java
language. It offers multiple torrent downloads, queuing/priority
systems (on torrents and files), start/stop seeding options and
instant access to numerous pieces of information about your torrents.
Azureus now features an embedded tracker easily set up and ready to
use.

%description -l pl.UTF-8
Azureus dostarcza implementację protokołu BitTorrent napisaną w języku
Java. Oferuje ściąganie wielopotokowe, systemy kolejkowania i
priorytetów (dla potoków i plików), opcje zatrzymywania i wznawiania
oraz bezpośredni dostęp do wielu części informacji o potokach. Azureus
zawiera teraz wbudowany tracker łatwy do skonfigurowania i używania.

%prep
%setup -q -c
%patch0 -p0
%patch1 -p1
%patch2 -p1

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
