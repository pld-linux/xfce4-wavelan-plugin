Summary:	A wavelan plugin for the Xfce panel
Summary(pl.UTF-8):	Wtyczka sieci radiowych dla panelu Xfce
Name:		xfce4-wavelan-plugin
Version:	0.5.3
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://goodies.xfce.org/releases/xfce4-wavelan-plugin/%{name}-%{version}.tar.bz2
# Source0-md5:	7fb068184b08d6b5bd7bc6d7e4369971
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-wavelan-plugin
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	perl-XML-Parser
BuildRequires:	perl-modules
BuildRequires:	pkgconfig
BuildRequires:	xfce4-panel-devel >= 4.3.90.2
Requires:	xfce4-panel >= 4.3.90.2
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
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xfce4/panel-plugins/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/*
%{_datadir}/xfce4/panel-plugins/*.desktop
