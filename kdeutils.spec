%define 	REV	20000418
Summary:	K Desktop Environment - utilities
Summary(pl):	K Desktop Environment - narzêdzia
Name:		kdeutils
Version:	2.0
Release:	1.pre_%{REV}
Copyright:      GPL
Group:          X11/KDE/Utilities
Group(pl):      X11/KDE/Narzêdzia
Source:		ftp://ftp.kde.org/pub/kde/snapshots/current/%{name}-%{REV}.tar.bz2
BuildRequires:	kdelibs-devel
BuildRequires:	qt-devel >= 2.1
BuildRequires:	libstdc++-devel
BuildRequires:	XFree86-devel
BuildRequires:	libtiff-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libungif-devel
BuildRequires:	libpng-devel
BuildRequires:	zlib-devel
Requires:	qt >= 2.1
Requires:	kdelibs = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_prefix		/usr/X11R6

%description
KDE utilities.
Package includes:
  Ark - archive manager
  Iconpackager - 
  KAb - address book
  KArm - time tracker
  KCalc - calculator
  KCharSelect -
  KDEPasswd -
  KDESsh - 
  Kdf -
  KEdit - text editor
  KFind -
  KFloppy - floppy formating tool
  KHexEdit - HEX file editor
  KJots - note taker
  KLaptopDaemon - 
  KLipper - clipboard viewer
  KLJetTool - tool for LaserJet priter users
  KLpq - print manager
  KNotes - notes
  KTop - task manager
  KTreeBrowser -
  KWrite - text editor

%description -l pl
Narzêdzia dla KDE.
Pakiet zawiera:
  Ark - program do zarz±dzania archiwami
  KAb - ksi±¿ka adresowa
  KArm - czasomierz
  KCalc - kalkulator
  KEdit - edytor tekstu
  KFloppy - narzêdzie do formatowania dyskietek
  KHexdit - edytor plików binarnych
  KJots - notatnik
  KLJetTool - narzêdzie dla u¿ytkowników drukarek LaserJet
  KNotes - inny notatnik
  Kpm - program do zarz±dzania procesami
  KTop - program do zarz±dzania procesami
  KWrite - rozbudowany edytor tekstu

%package ark
Summary:	KDE Archive Manager 
Summary(pl):	Zarz±dca archiwów dla KDE
Group:		X11/KDE/Utilities
Group(pl):	X11/KDE/Narzêdzia
Requires:	qt >= 1.44
Requires:	kdelibs = %{version}

%description ark
Ark is a program for managing and quickly extracting archives.

%description -l pl ark
Ark jest programem s³u¿±cym do zarz±dzania i szybkiego rozpakowywania
archiwów. 

%package kab
Summary:	KDE Address Book
Summary(pl):	Ksi±¿ka adresowa dla KDE
Group:		X11/KDE/Utilities
Group(pl):	X11/KDE/Narzêdzia
Requires:	qt >= 1.44
Requires:	kdelibs = %{version}

%description kab
Kab is a simple address book for KDE.

%description -l pl kab
Kab jest prost± ksi±¿k± adresow± dla KDE.

%package karm
Summary:	KDE Time Tracker
Summary(pl):	Time Tracker dla KDE
Group:		X11/KDE/Utilities
Group(pl):	X11/KDE/Narzêdzia
Requires:	qt >= 1.44
Requires:	kdelibs = %{version}

%description karm
KArm is a time tracker for busy people who need to keep track of the amount 
of time they spend on various tasks.

%description -l pl karm
Narzêdzie pozwalaj±ce ustaliæ ile czasu siê spêdzi³o robi±c ró¿ne rzeczy.

%package kcalc
Summary:	KDE Calculator	
Summary(pl):	Kalkulator dla KDE
Group:		X11/KDE/Utilities
Group(pl):	X11/KDE/Narzêdzia
Requires:	qt >= 1.44
Requires:	kdelibs = %{version}

%description kcalc
Calculator for KDE.

%description -l pl kcalc
Kalkulator dla KDE.

%package kedit
Summary:	KDE Text Editor	
Summary(pl):	Edytor tekstu dla KDE
Group:		X11/KDE/Utilities
Group(pl):	X11/KDE/Narzêdzia
Requires:	qt >= 1.44
Requires:	kdelibs = %{version}

%description kedit
Simple text editor for KDE.

%description -l pl kcalc
Prosty edytor tekstu dla KDE.

%package kfloppy
Summary:	KDE Floppy Formater	
Summary(pl):	Program formatuj±cy dyskietki dla KDE
Group:		X11/KDE/Utilities
Group(pl):	X11/KDE/Narzêdzia
Requires:	qt >= 1.44
Requires:	kdelibs = %{version}

%description kfloppy
KFloppy formats disks and puts a DOS or ext2fs filesystem on them.

%description -l pl kfloppy
KFloppy formatuje dyskietki i zak³ada na nich system pliku DOS lub ext2.

%package khexdit
Summary:	KDE Hex Editor	
Summary(pl):	Edytor szesnastkowy dla KDE
Group:		X11/KDE/Utilities
Group(pl):	X11/KDE/Narzêdzia
Requires:	qt >= 1.44
Requires:	kdelibs = %{version}

%description khexdit
Hex Editor is a small and simple viewer for binary files.

%description -l pl khexdit
Hex Editor jest ma³ym i prostym edytorem plików binarnych.

%package kjots
Summary:	KDE Note taker
Summary(pl):	Notatnik dla KDE
Group:		X11/KDE/Utilities
Group(pl):	X11/KDE/Narzêdzia
Requires:	qt >= 1.44
Requires:	kdelibs = %{version}

%description kjots
kjots is a small note taker program. Name and idea are taken from
the jots program included in the tkgoodstuff package.

%description -l pl kjots
KJots to ma³y program do zapisywania notatek.

%package klipper
Summary:	KDE Cut & Paste History
Summary(pl):	Historia schowka dla KDE
Group:		X11/KDE/Utilities
Group(pl):	X11/KDE/Narzêdzia
Requires:	qt >= 1.44
Requires:	kdelibs = %{version}

%description klipper
klipper displays cut&paste history.

%description -l pl klipper
klipper wy¶wietla historiê operacji 'wytnij i wklej'.

%package kljettool
Summary:	KDE LaserJet Tool	
Summary(pl):	Konfigurator drukarek LaserJet dla KDE
Group:		X11/KDE/Utilities
Group(pl):	X11/KDE/Narzêdzia
Requires:	qt >= 1.44
Requires:	kdelibs = %{version}

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
Summary:	KDE Print Manager
Summary(pl):	Zarz±dca wydruku dla KDE
Group:		X11/KDE/Utilities
Group(pl):	X11/KDE/Narzêdzia
Requires:	qt >= 1.44
Requires:	kdelibs = %{version}

%description klpq
Klpq is a frontend to the print spooler. Klpq does not modify the printqueue 
by itself, but uses the underlying commands: lpq, lprm and lpc.

%description -l pl klpq
Klpq jest nak³adk± graficzn± dla KDE, umo¿liwiaj±c± zarz±dzanie wydrukami.
Nie modyfikuje kolejki wydruków sammodzielnie, lecz wykorzystuje do tego
celu polecenia: lpq, lprm i lpc.

%package knotes 
Summary:	KDE Notes
Summary(pl):	Notes dla KDE
Group:		X11/KDE/Utilities
Group(pl):	X11/KDE/Narzêdzia
Requires:	qt >= 1.44
Requires:	kdelibs = %{version}

%description knotes
KNotes is ment to be a really usable and good looking notes application 
for the KDE project.

%description -l pl knotes
KNotes to program umo¿liwiaj±cy spisywanie notatek i trzymanie ich 
widocznych na ekranie.

%package kpm
Summary:	KDE Process Manager
Summary(pl):	Zarz±dca procesów dla KDE
Group:		X11/KDE/Utilities
Group(pl):	X11/KDE/Narzêdzia
Requires:	qt >= 1.44
Requires:	kdelibs = %{version}

%description kpm
kpm allows you to view and modify the processes of your Linux computer. 
It shows detailed information of running processes, computer resources 
like RAM, swap space, CPU utilization and so on. 
You can kill processes and modify their priority. 

%description -l pl kpm
kpm umo¿liwia Ci zarz±dzanie procesami w Twoim systemie. Wy¶wietla
szczegó³owe informacje na temat uruchomionych procesów, zasobów systemu
jak np. wielko¶æ u¿ywanej pamiêci czy partycji wymiany, wykorzystanie
procesora, itp. Masz mo¿liwo¶æ zabijania procesów i modyfikowania ich
priorytetów.

%package ktop
Summary:	KDE Task Manager
Summary(pl):	Zarz±dca zadañ dla KDE
Group:		X11/KDE/Utilities
Group(pl):	X11/KDE/Narzêdzia
Requires:	qt >= 1.44
Requires:	kdelibs = %{version}

%description ktop
KTop is the KDE Task Manager. It displays the processes running on
computer in list and tree form. Processes can be killed and various
other signals can be send to specific processes. It also features a
processor load and memory usage monitor.

%description -l pl ktop
KTop jest zarz±dc± zadañ dla KDE. Wy¶wietla on listê aktualnie uruchomionych
procesów. Masz mo¿liwo¶æ zabijania okre¶lonych procesów jak równie¿ wysy³ania 
do nich ró¿nych innych sygna³ów. KTop posiada równie¿ monitor obci±¿enia
procesora i wykorzystania pamiêci.

%package kwrite
Summary:	KDE Text Editor
Summary(pl):	Edytor tekstu dla KDE
Group:		X11/KDE/Utilities
Group(pl):	X11/KDE/Narzêdzia
Requires:	qt >= 1.44
Requires:	kdelibs = %{version}

%description kwrite
KWrite is an enhanced text editor for KDE.

%description -l pl kwrite
KWrite jest rozbudowanym edytorem tekstu dla KDE.

%prep
%setup -q -n %{name}

%build
export KDEDIR=%{_prefix}
CXXFLAGS="$RPM_OPT_FLAGS -Wall"
CFLAGS="$RPM_OPT_FLAGS -Wall"
CCOPTS="$RPM_OPT_FLAGS -Wall"
export CXXFLAGS CFLAGS CCOPTS
%configure \
	--prefix=$KDEDIR \
	--with-qt-dir=%{_prefix} \
 	--with-install-root=$RPM_BUILD_ROOT \
 	--with-pam="yes"
%{__make} KDEDIR=$KDEDIR

%install
rm -rf $RPM_BUILD_ROOT
export KDEDIR=%{_prefix}
%{__make} RUN_KAPPFINDER=no prefix=$RPM_BUILD_ROOT$KDEDIR install

%find_lang ark 
%find_lang kab 
%find_lang karm
%find_lang kcalc
%find_lang kedit
%find_lang kfloppy
%find_lang khexdit
%find_lang kjots
%find_lang klipper
%find_lang kljettool
%find_lang klpq
%find_lang knotes

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
