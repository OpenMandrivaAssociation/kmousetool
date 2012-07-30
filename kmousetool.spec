Name:		kmousetool
Version:	4.8.97
Release:	1
Epoch:		2
Summary:	Automatic Mouse Click
Group:		Graphical desktop/KDE
License:	GPLv2 and GFDL
URL:		http://www.kde.org/applications/utilities/kmousetool/
Source:		ftp://ftp.kde.org/pub/kde/unstable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs4-devel
BuildRequires:	pkgconfig(xi)
BuildRequires:	pkgconfig(xt)
Requires:	kdebase4-runtime

%description
KMouseTool is a Linux-based KDE program. It clicks the mouse for you,
so you don't have to. KMouseTool works with any mouse or pointing device.

%files
%doc AUTHORS ChangeLog COPYING COPYING.DOC README TODO
%{_kde_bindir}/kmousetool
%{_kde_applicationsdir}/kmousetool.desktop
%{_kde_appsdir}/kmousetool
%{_kde_iconsdir}/hicolor/*/*/kmousetool*
%{_kde_docdir}/HTML/en/kmousetool
%{_kde_mandir}/man1/kmousetool.1.*

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

