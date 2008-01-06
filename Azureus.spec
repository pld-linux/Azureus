%include	/usr/lib/rpm/macros.java
Summary:	Azureus - Java BitTorrent client
Summary(pl.UTF-8):	Azureus - klient BitTorrenta w Javie
Name:		Azureus
Version:	3.0.4.2
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://dl.sourceforge.net/azureus/%{name}_%{version}_source.zip
# Source0-md5:	fff98b2e2c2006cd71acf10116fc81c6
Source1:	%{name}.png
Source2:	%{name}.desktop
Source3:	%{name}.sh
Source4:	%{name}-build.xml
Patch0:		%{name}-platform.patch
URL:		http://azureus.sourceforge.net/
BuildRequires:	eclipse-swt >= 3.1.1
BuildRequires:	jakarta-commons-cli
BuildRequires:	jdk >= 1.4
BuildRequires:	jpackage-utils
BuildRequires:	logging-log4j
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
BuildRequires:	sed >= 4.0
BuildRequires:	unzip
Requires:	eclipse-swt >= 3.3
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
find '(' -name '*.java' -o -name '*.xml' ')' -print0 | xargs -0 sed -i -e 's,\r$,,'

%patch0 -p1
cp %{SOURCE4} build.xml

find -name 'osx' | xargs rm -r
find -name 'macosx' | xargs rm -r
find -name 'win32*' | xargs rm -r
find -name 'Win32*' | xargs rm -r
# Remove test code
rm org/gudy/azureus2/ui/swt/test/PrintTransferTypes.java

%build
export ANT_OPTS=-Xmx256M
%ant jar

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
