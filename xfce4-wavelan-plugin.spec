Summary:	A wavelan plugin for the XFce panel
Summary(pl):	Wtyczka sieci radiowych dla panelu XFce
Name:		xfce4-wavelan-plugin
Version:	0.4.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://download.berlios.de/xfce-goodies/%{name}-%{version}.tar.gz
# Source0-md5:	ef10846b21996a9f420b06ed2cb38e4c
URL:		http://xfce-goodies.berlios.de/
BuildRequires:	pkgconfig
BuildRequires:	xfce4-panel-devel >= 4.0.0
Requires:	xfce4-panel >= 4.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This plugin is used to display stats from a wireless LAN interface
(signal state, signal quality, network name (SSID)).

%description -l pl
Wtyczka ta wy¶wietla statystyki interfejsów sieci radiowych (stan
sygna³u, jako¶æ sygna³u, nazwa sieci (SSID)).

%prep
%setup -q

%build
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xfce4/panel-plugins/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/*.so
