Summary:	K Desktop Environment - utilities
Summary(pl):	K Desktop Environment - narzêdzia
Name:		kdeutils
version:	2.2.1
Release:	1
Epoch:		6
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.bz2
BuildRequires:	qt-devel >= 2.2.2
BuildRequires:	kdelibs-devel >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _prefix         /usr/X11R6
%define         _fontdir        /usr/share/fonts
%define         _htmldir        %{_datadir}/doc/kde/HTML

%description
KDE utilities. Package includes: Ark - archive manager Iconpackager -
KAb - address book KArm - time tracker KCalc - calculator KCharSelect
- KDEPasswd - KDESsh - Kdf - KEdit - text editor KFind - KFloppy -
  floppy formating tool KHexEdit - HEX file editor KJots - note taker
  KLaptopDaemon - KLipper - clipboard viewer KLJetTool - tool for
  LaserJet priter users KLpq - print manager KNotes - notes KTop - task
  manager KTreeBrowser - KWrite - text editor

%description -l pl
Narzêdzia dla KDE. Pakiet zawiera: Ark - program do zarz±dzania
archiwami KAb - ksi±¿ka adresowa KArm - czasomierz KCalc - kalkulator
KEdit - edytor tekstu KFloppy - narzêdzie do formatowania dyskietek
KHexdit - edytor plików binarnych KJots - notatnik KLJetTool -
narzêdzie dla u¿ytkowników drukarek LaserJet KNotes - inny notatnik
Kpm - program do zarz±dzania procesami KTop - program do zarz±dzania
procesami KWrite - rozbudowany edytor tekstu

%package ark
Summary:	KDE Archive Manager 
Summary(pl):	Zarz±dca archiwów dla KDE
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Requires:	kdelibs >= %{version}

%description ark
Ark is a program for managing and quickly extracting archives.

%description -l pl ark
Ark jest programem s³u¿±cym do zarz±dzania i szybkiego rozpakowywania
archiwów.

%package kab
Summary:	KDE Address Book
Summary(pl):	Ksi±¿ka adresowa dla KDE
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Requires:	kdelibs >= %{version}

%description kab
Kab is a simple address book for KDE.

%description -l pl kab
Kab jest prost± ksi±¿k± adresow± dla KDE.

%package karm
Summary:	KDE Time Tracker
Summary(pl):	Time Tracker dla KDE
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Requires:	kdelibs >= %{version}

%description karm
KArm is a time tracker for busy people who need to keep track of the
amount of time they spend on various tasks.

%description -l pl karm
Narzêdzie pozwalaj±ce ustaliæ ile czasu siê spêdzi³o robi±c ró¿ne
rzeczy.

%package kcalc
Summary:	KDE Calculator	
Summary(pl):	Kalkulator dla KDE
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Requires:	kdelibs >= %{version}

%description kcalc
Calculator for KDE.

%description -l pl kcalc
Kalkulator dla KDE.

%package kcharselect
Summary:	KDE Character Selector
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Requires:	kdelibs >= %{version}

%description kcharselect
Character Selector

%package kdepasswd
Summary:	KDE Passwd
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Requires:	kdelibs >= %{version}

%description kdepasswd
Change your password

%package kdessh
Summary:	KDE SSH Frontend
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Requires:	kdelibs >= %{version}

%description kdessh
SSH Frontend

%package kedit
Summary:	KDE Text Editor	
Summary(pl):	Edytor tekstu dla KDE
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Requires:	kdelibs >= %{version}

%description kedit
Simple text editor for KDE.

%description -l pl kedit
Prosty edytor tekstu dla KDE.

%package kdf
Summary:	KDE Disk space GUI
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Requires:	kdelibs >= %{version}

%description kdf
This program shows the disk usage of the mounted devices.

%package kfind
Summary:	KDE Find
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Requires:	kdelibs >= %{version}

%description kfind
Find Util

%package kfloppy
Summary:	KDE Floppy Formater	
Summary(pl):	Program formatuj±cy dyskietki dla KDE
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Requires:	kdelibs >= %{version}

%description kfloppy
KFloppy formats disks and puts a DOS or ext2fs filesystem on them.

%description -l pl kfloppy
KFloppy formatuje dyskietki i zak³ada na nich system pliku DOS lub
ext2.

%package khexdit
Summary:	KDE Hex Editor	
Summary(pl):	Edytor szesnastkowy dla KDE
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Requires:	kdelibs >= %{version}

%description khexdit
Hex Editor is a small and simple viewer for binary files.

%description -l pl khexdit
Hex Editor jest ma³ym i prostym edytorem plików binarnych.

%package kjots
Summary:	KDE Note taker
Summary(pl):	Notatnik dla KDE
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Requires:	kdelibs >= %{version}

%description kjots
kjots is a small note taker program. Name and idea are taken from the
jots program included in the tkgoodstuff package.

%description -l pl kjots
KJots to ma³y program do zapisywania notatek.

%package klaptopdaemon
Summary:	KDE Laptop Daemon
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Requires:	kdelibs >= %{version}

%description klaptopdaemon
KDE Laptop Daemon

%package kljettool
Summary:	KDE LaserJet Tool	
Summary(pl):	Konfigurator drukarek LaserJet dla KDE
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Requires:	kdelibs >= %{version}

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
KLJetToll to program umo¿liwiaj±cy konfiguracjê drukarek Hewlett
Packard LaserJet.

%package klpq 
Summary:	KDE Print Manager
Summary(pl):	Zarz±dca wydruku dla KDE
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Requires:	kdelibs >= %{version}

%description klpq
Klpq is a frontend to the print spooler. Klpq does not modify the
printqueue by itself, but uses the underlying commands: lpq, lprm and
lpc.

%description -l pl klpq
Klpq jest nak³adk± graficzn± dla KDE, umo¿liwiaj±c± zarz±dzanie
wydrukami. Nie modyfikuje kolejki wydruków sammodzielnie, lecz
wykorzystuje do tego celu polecenia: lpq, lprm i lpc.

%package klprfax
Summary:	KDE LPD fax frontend using efax
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Requires:	kdelibs >= %{version}
Requires:	efax

%description klprfax
With this program you can fax by printing to an lpd device.

%package knotes 
Summary:	KDE Notes
Summary(pl):	Notes dla KDE
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Requires:	kdelibs >= %{version}

%description knotes
KNotes is ment to be a really usable and good looking notes
application for the KDE project.

%description -l pl knotes
KNotes to program umo¿liwiaj±cy spisywanie notatek i trzymanie ich
widocznych na ekranie.

%package kpm
Summary:	KDE Process Manager
Summary(pl):	Zarz±dca procesów dla KDE
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Requires:	kdelibs >= %{version}

%description kpm
kpm allows you to view and modify the processes of your Linux
computer. It shows detailed information of running processes, computer
resources like RAM, swap space, CPU utilization and so on. You can
kill processes and modify their priority.

%description -l pl kpm
kpm umo¿liwia Ci zarz±dzanie procesami w Twoim systemie. Wy¶wietla
szczegó³owe informacje na temat uruchomionych procesów, zasobów
systemu jak np. wielko¶æ u¿ywanej pamiêci czy partycji wymiany,
wykorzystanie procesora, itp. Masz mo¿liwo¶æ zabijania procesów i
modyfikowania ich priorytetów.

%package ktimer
Summary:	KDE Timer
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Requires:	kdelibs >= %{version}

%description ktimer

%prep
%setup -q
%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

%configure2_13 \
	%{!?debug:--disable-debug} \
        --with-qt-dir=%{_prefix} \
        --with-install-root=$RPM_BUILD_ROOT \
        --with-pam="yes"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_applnkdir}/{Settings/KDE,Development/Editors}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_applnkdir}/Editors/KEdit.desktop $RPM_BUILD_ROOT%{_applnkdir}/Development/Editors
mv $RPM_BUILD_ROOT%{_applnkdir}/Settings/{Information,PowerControl} $RPM_BUILD_ROOT%{_applnkdir}/Settings/KDE

%clean
rm -rf $RPM_BUILD_ROOT

%files ark
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ark
%attr(755,root,root) %{_libdir}/libark.??
%attr(755,root,root) %{_libdir}/libark.so.*.*.*
%{_applnkdir}/Utilities/ark.desktop
%{_datadir}/apps/ark
%{_datadir}/apps/konqueror/servicemenus/arkservicemenu.desktop
%{_datadir}/services/arkpart.desktop
%{_pixmapsdir}/*/*/apps/ark.*
%lang(en) %{_htmldir}/en/ark

%files kab
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kab
%{_applnkdir}/Utilities/kab.desktop
%{_datadir}/apps/kab
%{_pixmapsdir}/*/*/apps/kab.*
%lang(en) %{_htmldir}/en/kab

%files karm
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/karm
%{_applnkdir}/Utilities/karm.desktop
%{_datadir}/apps/karm
%{_pixmapsdir}/*/*/apps/karm.*
%lang(en) %{_htmldir}/en/karm

%files kcalc
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kcalc
%attr(755,root,root) %{_libdir}/kcalc.*
%{_applnkdir}/Utilities/kcalc.desktop
%{_datadir}/apps/kcalc
%{_pixmapsdir}/*/*/apps/kcalc.*
%lang(en) %{_htmldir}/en/kcalc

%files kcharselect
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kcharselect
%attr(755,root,root) %{_libdir}/libkcharselectapplet.??
%attr(755,root,root) %{_libdir}/libkcharselectapplet.so.*.*.*
%{_applnkdir}/Utilities/KCharSelect.desktop
%{_datadir}/apps/kicker/applets/kcharselectapplet.desktop
%{_pixmapsdir}/*/*/apps/kcharselect.*

%files kdepasswd
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kdepasswd
%{_applnkdir}/Utilities/kdepasswd.desktop

%files kdessh
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kdessh

%files kdf
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kdf
%attr(755,root,root) %{_bindir}/kwikdisk
%attr(755,root,root) %{_libdir}/libkcm_kdf.*
%{_datadir}/apps/kdf
%{_applnkdir}/System/kdf.desktop
%{_applnkdir}/System/kwikdisk.desktop
%{_applnkdir}/Settings/KDE/Information/kcmdf.desktop
%{_pixmapsdir}/*/*/apps/kcmdf.*
%{_pixmapsdir}/*/*/apps/kdf.*
%{_pixmapsdir}/*/*/apps/kwikdisk.*
%lang(en) %{_htmldir}/en/kdf

%files kedit
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kedit
%attr(755,root,root) %{_libdir}/kde2/kedit.*
%{_applnkdir}/Development/Editors/KEdit.desktop
%{_datadir}/apps/kedit
%{_pixmapsdir}/*/*/apps/kedit.*
%lang(en) %{_htmldir}/en/kedit

%files kfind
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kfind
%attr(755,root,root) %{_libdir}/kfind.*
%{_applnkdir}/Kfind.desktop
%{_datadir}/apps/kfind
%{_pixmapsdir}/*/*/apps/kfind.*
%lang(en) %{_htmldir}/en/kfind

%files kfloppy
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kfloppy
%{_applnkdir}/Utilities/KFloppy.desktop
%{_datadir}/apps/kfloppy
%{_pixmapsdir}/*/*/apps/kfloppy.*
%lang(en) %{_htmldir}/en/kfloppy

%files khexdit
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/khexedit
%{_applnkdir}/Utilities/khexedit.desktop
%{_datadir}/apps/khexedit
%{_pixmapsdir}/*/*/apps/khexedit.*
%lang(en) %{_htmldir}/en/khexedit

%files kjots
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kjots
%{_applnkdir}/Utilities/Kjots.desktop
%{_datadir}/apps/kjots
%{_pixmapsdir}/*/*/apps/kjots.*
%lang(en) %{_htmldir}/en/kjots

%files klaptopdaemon
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/klaptopdaemon
%attr(755,root,root) %{_libdir}/libkcm_laptop.*
%{_applnkdir}/Settings/KDE/Information/pcmcia.desktop
%{_applnkdir}/Settings/KDE/PowerControl/battery.desktop
%{_applnkdir}/Settings/KDE/PowerControl/bwarning.desktop
%{_applnkdir}/Settings/KDE/PowerControl/cwarning.desktop
%{_applnkdir}/Settings/KDE/PowerControl/power.desktop
%{_datadir}/apps/klaptopdaemon
%{_pixmapsdir}/*/*/apps/laptop_battery.*
%{_pixmapsdir}/*/*/apps/laptop_pcmcia.*
%{_pixmapsdir}/*/*/apps/klaptopdaemon.*

%files kljettool
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kljettool
%{_applnkdir}/Utilities/KLJetTool.desktop
%{_datadir}/apps/kljettool
%{_pixmapsdir}/*/*/apps/kljettool.*
%lang(en) %{_htmldir}/en/kljettool

%files klpq
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/klpq
%{_applnkdir}/Utilities/KLpq.desktop
%{_pixmapsdir}/*/*/apps/klpq.*
%lang(en) %{_htmldir}/en/klpq

%files klprfax
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/klprfax*
%{_applnkdir}/Utilities/klprfax.desktop
%{_pixmapsdir}/*/*/apps/klprfax.*
%lang(en) %{_htmldir}/en/klprfax

%files knotes
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/knotes
%{_applnkdir}/Utilities/knotes.desktop
%{_datadir}/apps/knotes
%{_datadir}/config/knotesrc
%{_includedir}/KNotesIface.h
%{_pixmapsdir}/*/*/apps/knotes.*
%lang(en) %{_htmldir}/en/knotes

%files kpm
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kpm
%attr(755,root,root) %{_bindir}/kpmdocked
%{_applnkdir}/System/kpm.desktop
%{_pixmapsdir}/*/*/apps/kpm.*
%lang(en) %{_htmldir}/en/kpm

%files ktimer
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ktimer
%{_applnkdir}/Utilities/ktimer.desktop
