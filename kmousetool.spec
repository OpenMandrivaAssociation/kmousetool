Name:		kmousetool
Version:	15.12.1
Release:	1
Epoch:		2
Summary:	Automatic Mouse Click
Group:		Graphical desktop/KDE
License:	GPLv2 and GFDL
URL:		http://www.kde.org/applications/utilities/kmousetool/
Source:		http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs-devel
BuildRequires:	pkgconfig(xi)
BuildRequires:	pkgconfig(xt)
BuildRequires:	pkgconfig(xtst)
Requires:	kde-runtime

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
%cmake_kde4 \
	-DCMAKE_MINIMUM_REQUIRED_VERSION=3.1
%make

%install
%makeinstall_std -C build
