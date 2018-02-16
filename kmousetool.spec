%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)

Name:		kmousetool
Version:	 17.12.2
Release:	1
Epoch:		2
Summary:	Automatic Mouse Click
Group:		Graphical desktop/KDE
License:	GPLv2 and GFDL
URL:		http://www.kde.org/applications/utilities/kmousetool/
Source0:	http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5Config) cmake(KF5CoreAddons) cmake(KF5DBusAddons) cmake(KF5I18n) cmake(KF5IconThemes) cmake(KF5Notifications) cmake(KF5WidgetsAddons) cmake(KF5XmlGui) cmake(Qt5Core) cmake(Qt5Gui) cmake(Qt5Widgets)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	pkgconfig(xi)
BuildRequires:	pkgconfig(xt)
BuildRequires:	pkgconfig(xtst)

%description
KMouseTool is a Linux-based KDE program. It clicks the mouse for you,
so you don't have to. KMouseTool works with any mouse or pointing device.

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING COPYING.DOC README TODO
%{_bindir}/kmousetool
%{_datadir}/applications/org.kde.kmousetool.desktop
%{_datadir}/kmousetool
%{_datadir}/icons/hicolor/*/*/kmousetool*
%{_mandir}/man1/*.1*

%prep
%setup -q

%build
%cmake_kde5
%ninja

%install
%ninja_install -C build
%find_lang %{name} --all-name --with-html --with-man
