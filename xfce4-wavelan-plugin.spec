Summary:	A wavelan plugin for the Xfce panel
Summary(pl.UTF-8):	Wtyczka sieci radiowych dla panelu Xfce
Name:		xfce4-wavelan-plugin
Version:	0.5.12
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-wavelan-plugin/0.5/%{name}-%{version}.tar.bz2
# Source0-md5:	3ba5ee0626612942d249d4a80a1a67b7
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-wavelan-plugin
BuildRequires:	gettext-tools
BuildRequires:	libxfce4ui-devel
BuildRequires:	perl-XML-Parser
BuildRequires:	perl-modules
BuildRequires:	pkgconfig
BuildRequires:	xfce4-dev-tools >= 4.12.0
BuildRequires:	xfce4-panel-devel >= 4.12.0
Requires:	xfce4-panel >= 4.12.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This plugin is used to display stats from a wireless LAN interface
(signal state, signal quality, network name (SSID)).

%description -l pl.UTF-8
Wtyczka ta wyświetla statystyki interfejsów sieci radiowych (stan
sygnału, jakość sygnału, nazwa sieci (SSID)).

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

%{__rm} $RPM_BUILD_ROOT%{_libdir}/xfce4/panel/plugins/*.la
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/ur_PK

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/xfce4/panel/plugins/libwavelan.so
%{_datadir}/xfce4/panel/plugins/wavelan.desktop
