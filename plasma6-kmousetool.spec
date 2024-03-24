#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)

Name:		plasma6-kmousetool
Version:	24.02.1
Release:	%{?git:0.%{git}.}1
Summary:	Automatic Mouse Click
Group:		Graphical desktop/KDE
License:	GPLv2 and GFDL
URL:		https://www.kde.org/applications/utilities/kmousetool/
%if 0%{?git:1}
Source0:	https://invent.kde.org/accessibility/kmousetool/-/archive/%{gitbranch}/kmousetool-%{gitbranchd}.tar.bz2#/kmousetool-%{git}.tar.bz2
%else
Source0:	https://download.kde.org/%{stable}/release-service/%{version}/src/kmousetool-%{version}.tar.xz
%endif
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6Config) cmake(KF6CoreAddons) cmake(KF6WidgetsAddons)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6QmlCore)
BuildRequires:  cmake(Qt6QmlNetwork)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6StatusNotifierItem)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6WindowSystem)
BuildRequires:	cmake(Phonon4Qt6)
BuildRequires:	pkgconfig(xi)
BuildRequires:	pkgconfig(xt)
BuildRequires:	pkgconfig(xtst)
BuildRequires:  qt6-qtbase-theme-gtk3
BuildRequires:	qt6-qtmultimedia-gstreamer

%description
KMouseTool is a Linux-based KDE program. It clicks the mouse for you,
so you don't have to. KMouseTool works with any mouse or pointing device.

%files -f %{name}.lang
%{_bindir}/kmousetool
%{_datadir}/applications/org.kde.kmousetool.desktop
%{_datadir}/kmousetool
%{_datadir}/icons/hicolor/*/*/kmousetool*
%{_datadir}/metainfo/org.kde.kmousetool.appdata.xml
%{_mandir}/man1/*.1*

%prep
%autosetup -p1 -n kmousetool-%{?git:%{gitbranchd}}%{!?git:%{version}}

%build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja
%ninja

%install
%ninja_install -C build
%find_lang %{name} --all-name --with-html --with-man
