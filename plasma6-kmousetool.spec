%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)

Name:		plasma6-kmousetool
Version:	24.01.90
Release:	2
Summary:	Automatic Mouse Click
Group:		Graphical desktop/KDE
License:	GPLv2 and GFDL
URL:		http://www.kde.org/applications/utilities/kmousetool/
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/kmousetool-%{version}.tar.xz
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6Config) cmake(KF6CoreAddons) cmake(KF6WidgetsAddons)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6WindowSystem)
BuildRequires:	cmake(Phonon4Qt6)
BuildRequires:	pkgconfig(xi)
BuildRequires:	pkgconfig(xt)
BuildRequires:	pkgconfig(xtst)

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
%autosetup -p1 -n kmousetool-%{?git:master}%{!?git:%{version}}

%build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja
%ninja

%install
%ninja_install -C build
%find_lang %{name} --all-name --with-html --with-man
