Name: kmousetool
Summary: Kmousetool - automatic mouse click
Version: 4.8.2
Release: 1
Epoch: 2
Group: Graphical desktop/KDE
License: LGPLv2
URL: http://utils.kde.org/projects/kmousetool
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/%{name}-%version.tar.xz
BuildRequires: kdelibs4-devel >= 2:%{version}
BuildRequires: libxt-devel
BuildRequires: libxi-devel

Obsoletes: kde4-kmousetool < 4.0.68
Provides: kde4-kmousetool = %version

%description
KMouseTool is a Linux-based KDE program. It clicks the mouse for you, 
so you don't have to. KMouseTool works with any mouse or pointing device.

%files 
%_kde_bindir/kmousetool
%_kde_iconsdir/*/*/apps/kmousetool.*
%_kde_iconsdir/*/*/actions/*.png
%_kde_datadir/applications/kde4/kmousetool.desktop
%_kde_docdir/HTML/*/kmousetool
%_kde_datadir/apps/kmousetool/sounds/*.wav
%_mandir/man1/*

%prep
%setup -q

%build
%cmake_kde4

%make

%install
%makeinstall_std -C build

