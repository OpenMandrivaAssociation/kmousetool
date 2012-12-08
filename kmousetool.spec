Name:		kmousetool
Version:	4.9.4
Release:	1
Epoch:		2
Summary:	Automatic Mouse Click
Group:		Graphical desktop/KDE
License:	GPLv2 and GFDL
URL:		http://www.kde.org/applications/utilities/kmousetool/
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
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

%changelog
* Wed Dec 05 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.9.4-1
- New version 4.9.4

* Wed Nov 07 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.9.3-1
- New version 4.9.3

* Thu Oct 04 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.9.2-1
- New version 4.9.2

* Sat Sep 08 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.9.1-1
- New version 4.9.1

* Tue Aug 14 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.9.0-1
- New version 4.9.0

* Fri Jul 20 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.8.97-1
- New version 4.8.97

* Sat Jul 07 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.8.95-1
- New version 4.8.95

* Fri Jun 08 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 2:4.8.4-69.1mib2010.2
- New version 4.8.4
- MIB (Mandriva International Backports)

* Fri May 04 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 2:4.8.3-69.1mib2010.2
- New version 4.8.3
- MIB (Mandriva International Backports)

* Wed Apr 04 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 2:4.8.2-69.1mib2010.2
- New version 4.8.2
- MIB (Mandriva International Backports)

* Wed Mar 07 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 2:4.8.1-69.1mib2010.2
- New version 4.8.1
- MIB (Mandriva International Backports)

* Mon Feb 20 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 2:4.8.0-69.1mib2010.2
+ Revision: 198336
- Backport from Mageia to Mandriva 2010.2 for MIB users
- Merge handbook back into main package
- MIB (Mandriva International Backports)

* Thu Jan 19 2012 mikala <mikala> 2:4.8.0-1.mga2
+ Revision: 198336
- Updating tarball to KDE 4.8.0

* Thu Jan 05 2012 mikala <mikala> 2:4.7.97-1.mga2
+ Revision: 191088
- Update tarball to kde 4.7.97

* Fri Dec 23 2011 mikala <mikala> 2:4.7.95-1.mga2
+ Revision: 186263
- Update tarball to kde 4.7.95
- fix group

* Wed Dec 14 2011 mikala <mikala> 2:4.7.90-1.mga2
+ Revision: 181460
- imported package kmousetool

