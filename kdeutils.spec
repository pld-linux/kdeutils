Summary:	K Desktop Environment - utilities
Summary(pl):	K Desktop Environment - narzêdzia
Name:		kdeutils
Version:	1.1.1
Release:	3
#ftp://ftp.kde.org/pub/kde/stable/%{version}/distribution/tar/generic/source/bz2/
Source:		%{name}-%{version}.tar.bz2
Group:		X11/KDE/Utilities
Group(pl):	X11/KDE/Narzêdzia
Copyright:	GPL
Requires:	qt >= 1.44, kdelibs = %{version}
Vendor:		The KDE Team
BuildRoot:	/tmp/%{name}-%{version}-root

%define 	_prefix		/usr/X11R6

%description
KDE utilities.
Package includes:
  KAb - 
  KArm - time tracker
  KCalc - calculator
  KEdit - text editor
  KFloppy - floppy formating tool
  KHexEdit - HEX file editor
  KJots - note taker
  KLipper
  KLJetTool - tool for LaserJet priter users
  KLpq - lpq 
  KNotes - notes
  Kpm - 
  KTop - 
  KWrite - 

%description -l pl
Narzêdzia KDE.
Pakiet zawiera:
  KArm
  KCalc - kalkulator
  KEdit - edytor tekstu
  KFloppy - narzêdzie do formatowania dyskietek
  KHexdit - edytor plików
  KJots - notatnik
  KLJetTool - narzêdzie dla u¿ytkowników drukarek LaserJet
  KNotes - inny notatnik
  KZip

%package ark
Summary:     KDE 
Summary(pl): Time Tracker dla KDE
Group:       X11/KDE/Utilities
Group(pl):   X11/KDE/Narzêdzia
Requires:    qt >= 1.40, kdelibs = %{version}

%description ark

%description -l pl ark

%package kab
Summary:     KDE 
Summary(pl): Time Tracker dla KDE
Group:       X11/KDE/Utilities
Group(pl):   X11/KDE/Narzêdzia
Requires:    qt >= 1.40, kdelibs = %{version}

%description kab

%description -l pl kab

%package karm
Summary:     KDE Time Tracker
Summary(pl): Time Tracker dla KDE
Group:       X11/KDE/Utilities
Requires:    qt >= 1.40, kdelibs = %{version}

%description karm
KArm is a time tracker for busy people who need
to keep track of the amount of time they spend
on various tasks.

%description -l pl karm
Narzêdzie pozwalaj±ce ustaliæ ile czasu siê spêdzi³o robi±c ró¿ne rzeczy.

%package kcalc
Summary:     KDE Calculator	
Summary(pl): Kalkulator KDE
Group:       X11/KDE/Utilities
Requires:    qt >= 1.40, kdelibs = %{version}

%description kcalc
Calculator for KDE.

%description -l pl kcalc
Kalkulator dla KDE.

%package kedit
Summary:     KDE Text Editor	
Summary(pl): Edytor tekstu dla KDE
Group:       X11/KDE/Utilities
Requires:    qt >= 1.40, kdelibs = %{version}

%description kedit
Simple text editor for KDE.

%description -l pl kcalc
Prosty edytor tekstu dla KDE.

%package kfloppy
Summary:     KDE Floppy Formater	
Summary(pl): Formatowanie dyskietek z KDE
Group:       X11/KDE/Utilities
Requires:    qt >= 1.40, kdelibs = %{version}

%description kfloppy
KFloppy formats disks and puts a DOS or ext2fs filesystem on them.

%description -l pl kfloppy
KFloppy formatuje dyskietki i zak³ada na nich system pliku DOS lub ext2.

%package khexdit
Summary:     KDE Hex Editor	
Summary(pl): Edytor szesnastkowy KDE
Group:       X11/KDE/Utilities
Requires:    qt >= 1.40, kdelibs = %{version}

%description khexdit
Hex Editor is a small and simple viewer for binary files.

%description -l pl khexdit
Prosta przegl±darka do plików binarnych.

%package kjots
Summary:     KDE Note taker
Summary(pl): Notatnik KDE
Group:       X11/KDE/Utilities
Requires:    qt >= 1.40, kdelibs = %{version}

%description kjots
kjots is a small note taker program. Name and idea are taken from
the jots program included in the tkgoodstuff package.

%description -l pl kjots
KJots to ma³y program do zbierania notatek.

%package klipper
Summary:     KDE Note taker
Summary(pl): Notatnik KDE
Group:       X11/KDE/Utilities
Group(pl):   X11/KDE/Narzêdzia
Requires:    qt >= 1.40, kdelibs = %{version}

%description klipper

%description -l pl klipper

%package kljettool
Summary:     KDE LaserJet Tool	
Summary(pl): Konfigurator drukarek LaserJet dla KDE
Group:       X11/KDE/Utilities
Requires:    qt >= 1.40, kdelibs = %{version}

%description kljettool
KLJetTool is a program that lets you adjust your Hewlett Packard
Laserjet operating parameters. Some of Hewlet Packards printers such
as the 5L or the 6L do no longer have a hardware control panel and the
printer is controlled completely by software. However this software is
often available only for the Windows platform. KLJetTool seeks to fill
the need for such software on the Unix platform. It should work with
any printer that understands Hewlet Packarts PJL ( Printer Job
Language). However some features may have no effect on your particular
model.
			   
%description -l pl kljettool
KLJetToll to program umo¿liwiaj±cy konfiguracjê drukarek
Hewlett Packard LaserJet.

%package klpq 
Summary:     KDE Notes
Summary(pl): Notes KDE
Group:       X11/KDE/Utilities
Group(pl):   X11/KDE/Narzêdzia
Requires:    qt >= 1.40, kdelibs = %{version}

%description klpq

%description -l pl klpq

%package knotes 
Summary:     KDE Notes
Summary(pl): Notes KDE
Group:       X11/KDE/Utilities
Requires:    qt >= 1.40, kdelibs = %{version}

%description knotes
KNotes is ment to be a really usable and good looking notes
application for the KDE project.

%description -l pl knotes
KNotes to program umo¿liwiaj±cy spisywanie sobie notatek i trzymanie ich na
ekranie komputera.

%package kpm
Summary:     KDE Archive Handling Tool
Summary(pl): Program obs³ugi archiwów KDE
Group:       X11/KDE/Utilities
Group(pl):   X11/KDE/Narzêdzia
Requires:    qt >= 1.40, kdelibs = %{version}

%description kpm

%description -l pl kpm

%package ktop
Summary:     KDE Archive Handling Tool
Summary(pl): Program obs³ugi archiwów KDE
Group:       X11/KDE/Utilities
Group(pl):   X11/KDE/Narzêdzia
Requires:    qt >= 1.40, kdelibs = %{version}

%description ktop

%description -l pl ktop

%package kwrite
Summary:     KDE Archive Handling Tool
Summary(pl): Program obs³ugi archiwów KDE
Group:       X11/KDE/Utilities
Group(pl):   X11/KDE/Narzêdzia
Requires:    qt >= 1.40, kdelibs = %{version}

%description kwrite

%description -l pl kwrite

%prep
%setup -q

%build
export KDEDIR=%{_prefix}
CXXFLAGS="$RPM_OPT_FLAGS -Wall" \
CFLAGS="$RPM_OPT_FLAGS -Wall" \
CCOPTS="$RPM_OPT_FLAGS -Wall" \
./configure %{_target_platform} \
	--prefix=$KDEDIR \
 	--with-install-root=$RPM_BUILD_ROOT \
 	--with-pam="yes"
make KDEDIR=$KDEDIR

%install
rm -rf $RPM_BUILD_ROOT
export KDEDIR=%{_prefix}
make RUN_KAPPFINDER=no prefix=$RPM_BUILD_ROOT$KDEDIR install

%find_lang ark ark.lang
%find_lang kab kab.lang
%find_lang karm karm.lang
%find_lang kcalc kcalc.lang
%find_lang kedit kedit.lang
%find_lang kfloppy kfloppy.lang
%find_lang khexdit khexdit.lang
%find_lang kjots kjots.lang
%find_lang klipper klipper.lang
%find_lang kljettool kljettool.lang
%find_lang klpq klpq.lang
%find_lang knotes knotes.lang

%clean
rm -rf $RPM_BUILD_ROOT

#################################################
#             ARK - checking OK
#################################################

%files ark -f ark.lang
%defattr(644,root,root,755)

%config(missingok) /etc/X11/kde/applnk/Utilities/ark.kdelnk

%attr(755,root,root) %{_bindir}/ark

%{_datadir}/kde/doc/HTML/en/ark

%{_datadir}/kde/icons/ark.xpm
%{_datadir}/kde/icons/mini/ark.xpm

#################################################
#             KAB - checking OK
#################################################

%files kab -f kab.lang
%defattr(644,root,root,755)

%config(missingok) /etc/X11/kde/applnk/Utilities/kab.kdelnk

%attr(755,root,root) %{_bindir}/kab
%attr(755,root,root) %{_bindir}/kabapi_test

%{_datadir}/kde/apps/kab

%lang(de) %{_datadir}/kde/doc/HTML/de/kab
%{_datadir}/kde/doc/HTML/en/kab

%{_datadir}/kde/icons/kab.xpm
%{_datadir}/kde/icons/mini/kab.xpm

#################################################
#             KARM - checking OK
#################################################

%files karm -f karm.lang
%defattr(644,root,root,755)

%config(missingok) /etc/X11/kde/applnk/Utilities/KArm.kdelnk

%attr(755,root,root) %{_bindir}/karm

%{_datadir}/kde/doc/HTML/en/karm

%{_datadir}/kde/icons/karm.xpm
%{_datadir}/kde/icons/mini/karm.xpm

#################################################
#             KCALC - checking OK
#################################################

%files kcalc -f kcalc.lang
%defattr(644,root,root,755)

%config(missingok) /etc/X11/kde/applnk/Utilities/kcalc.kdelnk

%attr(755,root,root) %{_bindir}/kcalc

%{_datadir}/kde/apps/kcalc

%lang(de) %{_datadir}/kde/doc/HTML/de/kcalc
%{_datadir}/kde/doc/HTML/en/kcalc

%{_datadir}/kde/icons/mini/kcalc.xpm
%{_datadir}/kde/icons/kcalc.xpm

#################################################
#             KEDIT - checking OK
#################################################

%files kedit -f kedit.lang
%defattr(644,root,root,755)

%config(missingok) /etc/X11/kde/applnk/Applications/KEdit.kdelnk

%attr(755,root,root) %{_bindir}/kedit

%{_datadir}/kde/apps/kedit/

%{_datadir}/kde/doc/HTML/en/kedit

%{_datadir}/kde/icons/mini/kedit.xpm
%{_datadir}/kde/icons/kedit.xpm

#################################################
#             KFLOPPY - chscking OK
#################################################

%files kfloppy -f kfloppy.lang
%defattr(644,root,root,755)

%config(missingok) /etc/X11/kde/applnk/Utilities/KFloppy.kdelnk

%attr(755,root,root) %{_bindir}/kfdformat
%attr(755,root,root) %{_bindir}/kfloppy
%attr(755,root,root) %{_bindir}/kmkdosfs
%attr(755,root,root) %{_bindir}/kmke2fs

%{_datadir}/kde/apps/kfloppy

%{_datadir}/kde/doc/HTML/en/kfloppy

%{_datadir}/kde/icons/mini/kfloppy.xpm
%{_datadir}/kde/icons/kfloppy.xpm

#################################################
#             KHEXDIT - checking OK
#################################################

%files khexdit -f khexdit.lang
%defattr(644,root,root,755)

%config(missingok) /etc/X11/kde/applnk/Utilities/khexdit.kdelnk

%attr(755,root,root) %{_bindir}/khexdit

%{_datadir}/kde/doc/HTML/en/khexdit
%lang(it) %{_datadir}/kde/doc/HTML/it/khexdit

%{_datadir}/kde/icons/mini/khexdit.xpm
%{_datadir}/kde/icons/khexdit.xpm

#################################################
#             KJOTS - checking OK
#################################################

%files kjots -f kjots.lang
%defattr(644,root,root,755)

%config(missingok) /etc/X11/kde/applnk/Utilities/Kjots.kdelnk

%attr(755,root,root) %{_bindir}/kjots

%{_datadir}/kde/apps/kjots

%{_datadir}/kde/doc/HTML/en/kjots

%{_datadir}/kde/icons/mini/kjots.xpm
%{_datadir}/kde/icons/kjots.xpm

#################################################
#             KLIPPER - checking OK
#################################################

%files klipper -f klipper.lang
%defattr(644,root,root,755)

%config(missingok) /etc/X11/kde/applnk/Utilities/klipper.kdelnk

%attr(755,root,root) %{_bindir}/klipper

%{_datadir}/kde/icons/mini/klipper.xpm
%{_datadir}/kde/icons/klipper.xpm

#################################################
#             KLJETTOOL - checking OK
#################################################

%files kljettool -f kljettool.lang
%defattr(644,root,root,755)

%config(missingok) /etc/X11/kde/applnk/Utilities/KLJetTool.kdelnk

%attr(755,root,root) %{_bindir}/kljettool

%{_datadir}/kde/doc/HTML/en/kljettool

%{_datadir}/kde/icons/mini/kljettool.xpm
%{_datadir}/kde/icons/kljetlogo.xpm

#################################################
#             KLPQ - checking OK
#################################################

%files klpq -f klpq.lang
%defattr(644,root,root,755)

%config(missingok) /etc/X11/kde/applnk/Utilities/KLpq.kdelnk

%attr(755,root,root) %{_bindir}/klpq

%{_datadir}/kde/doc/HTML/en/klpq

%{_datadir}/kde/icons/mini/klpq.xpm
%{_datadir}/kde/icons/klpq.xpm

#################################################
#             KNOTES
#################################################

%files knotes -f knotes.lang
%defattr(644,root,root,755)

%config(missingok) /etc/X11/kde/applnk/Utilities/knotes.kdelnk

%attr(755,root,root) %{_bindir}/knotes

%{_datadir}/kde/apps/knotes/

%{_datadir}/kde/doc/HTML/en/knotes

%{_datadir}/kde/icons/mini/knotes.xpm
%{_datadir}/kde/icons/knotes.xpm
