Summary:	A wavelan plugin for the Xfce panel
Summary(pl.UTF-8):	Wtyczka sieci radiowych dla panelu Xfce
Name:		xfce4-wavelan-plugin
Version:	0.6.4
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	https://archive.xfce.org/src/panel-plugins/xfce4-wavelan-plugin/0.6/%{name}-%{version}.tar.bz2
# Source0-md5:	62c2a962efb519b26303691f52e509b6
URL:		https://goodies.xfce.org/projects/panel-plugins/xfce4-wavelan-plugin
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.50.0
BuildRequires:	gtk+3-devel >= 3.22.0
BuildRequires:	libxfce4ui-devel >= 4.16.0
BuildRequires:	libxfce4util-devel >= 4.16.0
BuildRequires:	perl-XML-Parser
BuildRequires:	perl-modules
BuildRequires:	pkgconfig
BuildRequires:	xfce4-dev-tools >= 4.16.0
BuildRequires:	xfce4-panel-devel >= 4.16.0
Requires:	xfce4-panel >= 4.16.0
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
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{hy_AM,hye,ie,ur_PK}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS
%attr(755,root,root) %{_libdir}/xfce4/panel/plugins/libwavelan.so
%{_datadir}/xfce4/panel/plugins/wavelan.desktop
