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
# we need SWT (whatever is it), not whole eclipse...  do we?
BuildRequires:	eclipse
BuildRequires:	jakarta-commons-cli
BuildRequires:	jakarta-log4j
BuildRequires:	jdk
BuildRequires:	SEDA
Requires:	jre
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
blah, NFY

#%description -l pl

%prep
%setup -q -c -n %{name}-%{version}

%build
# if ac/am/* rebuilding is necessary, do it in this order and add
# appropriate BuildRequires
#%%{__gettextize}
#%%{__aclocal}
#%%{__autoconf}
#%%{__autoheader}
#%%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
#install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
