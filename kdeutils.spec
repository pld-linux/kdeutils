Summary:	K Desktop Environment - utilities
Summary(pl):	K Desktop Environment - narzêdzia
Name:		kdeutils
Version:	2.0.1
Release:	1
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/distribution/tar/generic/src/%{name}-%{version}.tar.bz2
BuildRequires:	qt-devel >= 2.2.2
BuildRequires:	kdelibs-devel = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _prefix         /usr/X11R6
%define         _fontdir        /usr/share/fonts
%define         _htmldir        %{_datadir}/doc/kde/HTML

%description
KDE utilities. Package includes:
Ark - archive manager Iconpackager -
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
Requires:	kdelibs = %{version}

%description ark
Ark is a program for managing and quickly extracting archives.

%description -l pl ark
Ark jest programem s³u¿±cym do zarz±dzania i szybkiego rozpakowywania
archiwów.

%package kab
Summary:	KDE Address Book
Summary(pl):	Ksi±¿ka adresowa dla KDE
Group:		X11/Applications
Requires:	kdelibs = %{version}

%description kab
Kab is a simple address book for KDE.

%description -l pl kab
Kab jest prost± ksi±¿k± adresow± dla KDE.

%package karm
Summary:	KDE Time Tracker
Summary(pl):	Time Tracker dla KDE
Group:		X11/Applications
Requires:	kdelibs = %{version}

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
Requires:	kdelibs = %{version}

%description kcalc
Calculator for KDE.

%description -l pl kcalc
Kalkulator dla KDE.

%package kcharselect
Summary:	KDE Character Selector
Group:		X11/Applications
Requires:	kdelibs = %{version}

%description kcharselect
Character Selector

%package kdepasswd
Summary:	KDE Passwd
Group:		X11/Applications
Requires:	kdelibs = %{version}

%description kdepasswd
Change your password

%package kedit
Summary:	KDE Text Editor	
Summary(pl):	Edytor tekstu dla KDE
Group:		X11/Applications
Requires:	kdelibs = %{version}

%description kedit
Simple text editor for KDE.

%description -l pl kedit
Prosty edytor tekstu dla KDE.

%package kfind
Summary:	KDE Find
Group:		X11/Applications
Requires:	kdelibs = %{version}

%description kfind
Find Util

%package kfloppy
Summary:	KDE Floppy Formater	
Summary(pl):	Program formatuj±cy dyskietki dla KDE
Group:		X11/Applications
Requires:	kdelibs = %{version}

%description kfloppy
KFloppy formats disks and puts a DOS or ext2fs filesystem on them.

%description -l pl kfloppy
KFloppy formatuje dyskietki i zak³ada na nich system pliku DOS lub
ext2.

%package khexdit
Summary:	KDE Hex Editor	
Summary(pl):	Edytor szesnastkowy dla KDE
Group:		X11/Applications
Requires:	kdelibs = %{version}

%description khexdit
Hex Editor is a small and simple viewer for binary files.

%description -l pl khexdit
Hex Editor jest ma³ym i prostym edytorem plików binarnych.

%package kjots
Summary:	KDE Note taker
Summary(pl):	Notatnik dla KDE
Group:		X11/Applications
Requires:	kdelibs = %{version}

%description kjots
kjots is a small note taker program. Name and idea are taken from the
jots program included in the tkgoodstuff package.

%description -l pl kjots
KJots to ma³y program do zapisywania notatek.

%package klaptopdaemon
Summary:	KDE Laptop Daemon
Group:		X11/Applications
Requires:	kdelibs = %{version}

%description klaptopdaemon
KDE Laptop Daemon

%package kljettool
Summary:	KDE LaserJet Tool	
Summary(pl):	Konfigurator drukarek LaserJet dla KDE
Group:		X11/Applications
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
KLJetToll to program umo¿liwiaj±cy konfiguracjê drukarek Hewlett
Packard LaserJet.

%package klpq 
Summary:	KDE Print Manager
Summary(pl):	Zarz±dca wydruku dla KDE
Group:		X11/Applications
Requires:	kdelibs = %{version}

%description klpq
Klpq is a frontend to the print spooler. Klpq does not modify the
printqueue by itself, but uses the underlying commands: lpq, lprm and
lpc.

%description -l pl klpq
Klpq jest nak³adk± graficzn± dla KDE, umo¿liwiaj±c± zarz±dzanie
wydrukami. Nie modyfikuje kolejki wydruków sammodzielnie, lecz
wykorzystuje do tego celu polecenia: lpq, lprm i lpc.

%package knotes 
Summary:	KDE Notes
Summary(pl):	Notes dla KDE
Group:		X11/Applications
Requires:	kdelibs = %{version}

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
Requires:	kdelibs = %{version}

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

%package ktimemon
Summary:	KDE TimeMon
Group:		X11/Applications
Requires:	kdelibs = %{version}

%description ktimemon

%prep
%setup -q
%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

%configure \
        --with-qt-dir=%{_prefix} \
        --with-install-root=$RPM_BUILD_ROOT \
        --with-pam="yes"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_applnkdir}/Settings/KDE

%{__make} install DESTDIR=$RPM_BUILD_ROOT


mv $RPM_BUILD_ROOT%{_applnkdir}/Editors/KEdit.desktop $RPM_BUILD_ROOT%{_applnkdir}/Utilities
mv $RPM_BUILD_ROOT%{_applnkdir}/Settings/{Information,PowerControl} $RPM_BUILD_ROOT%{_applnkdir}/Settings/KDE

%clean
rm -rf $RPM_BUILD_ROOT

%files ark
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ark
%{_applnkdir}/Utilities/ark.desktop
%{_datadir}/doc/kde/HTML/en/ark
%{_datadir}/apps/ark
%{_pixmapsdir}/locolor/*x*/apps/ark.png
%{_pixmapsdir}/hicolor/*x*/apps/ark.png

%files kab
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kab
%{_applnkdir}/Utilities/kab.desktop
%{_datadir}/doc/kde/HTML/en/ark
%{_datadir}/apps/ark
%{_pixmapsdir}/locolor/*x*/apps/ark.png
%{_pixmapsdir}/hicolor/*x*/apps/ark.png

%files karm
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/karm
%{_applnkdir}/Utilities/karm.desktop
%{_datadir}/doc/kde/HTML/en/karm
%{_datadir}/apps/karm
%{_pixmapsdir}/locolor/*x*/apps/karm.png
%{_pixmapsdir}/hicolor/*x*/apps/karm.png

%files kcalc
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kcalc
%{_applnkdir}/Utilities/karm.desktop
%{_datadir}/doc/kde/HTML/en/kcalc
%{_datadir}/apps/kcalc
%{_pixmapsdir}/locolor/*x*/apps/kcalc.png
%{_pixmapsdir}/hicolor/*x*/apps/kcalc.png

%files kcharselect
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kcharselect
%{_applnkdir}/Utilities/KCharSelect.desktop
%{_pixmapsdir}/locolor/*x*/apps/kcharselect.png
%{_pixmapsdir}/hicolor/*x*/apps/kcharselect.png

%files kdepasswd
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kdepasswd
%{_applnkdir}/Utilities/kdepasswd.desktop

%files kedit
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kedit
%{_applnkdir}/Utilities/KEdit.desktop
%{_datadir}/doc/kde/HTML/en/kedit
%{_datadir}/apps/kedit
%attr(755,root,root) %{_libdir}/kedit.*
%{_pixmapsdir}/locolor/*x*/apps/kedit.png
%{_pixmapsdir}/hicolor/*x*/apps/kedit.png

%files kfind
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kfind
%{_applnkdir}/Kfind.desktop
%{_datadir}/doc/kde/HTML/en/kfind
%{_datadir}/apps/kedit
%attr(755,root,root) %{_libdir}/kfind.*
%{_pixmapsdir}/locolor/*x*/apps/kfind.png
%{_pixmapsdir}/hicolor/*x*/apps/kfind.png

%files kfloppy
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kfloppy
%{_applnkdir}/Utilities/KFloppy.desktop
%{_datadir}/doc/kde/HTML/en/kfloppy
%{_datadir}/apps/kfloppy
%{_pixmapsdir}/locolor/*x*/apps/kfloppy.png
%{_pixmapsdir}/hicolor/*x*/apps/kfloppy.png

%files khexdit
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/khexedit
%{_applnkdir}/Utilities/khexedit.desktop
%{_datadir}/doc/kde/HTML/en/khexedit
%{_datadir}/apps/khexedit
%{_pixmapsdir}/locolor/*x*/apps/khexedit.png
%{_pixmapsdir}/hicolor/*x*/apps/khexedit.png

%files kjots
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kjots
%{_applnkdir}/Utilities/Kjots.desktop
%{_datadir}/doc/kde/HTML/en/kjots
%{_datadir}/apps/kjots
%{_pixmapsdir}/locolor/*x*/apps/kjots.png
%{_pixmapsdir}/hicolor/*x*/apps/kjots.png

%files klaptopdaemon
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/klaptopdaemon
%{_applnkdir}/Settings/KDE/Information/*.desktop
%{_applnkdir}/Settings/KDE/PowerControl/*.desktop
%{_datadir}/apps/klaptopdaemon
%attr(755,root,root) %{_libdir}/libkcm_laptop.??
%{_pixmapsdir}/locolor/*x*/apps/laptop*.png
%{_pixmapsdir}/hicolor/*x*/apps/laptop*.png

%files kljettool
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kljettool
%{_applnkdir}/Utilities/KLJetTool.desktop
%{_datadir}/doc/kde/HTML/en/kljettool
%{_datadir}/apps/kljettool
%{_pixmapsdir}/locolor/*x*/apps/kljettool.png
%{_pixmapsdir}/hicolor/*x*/apps/kljettool.png

%files klpq
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/klpq
%{_applnkdir}/Utilities/KLpq.desktop
%{_datadir}/doc/kde/HTML/en/klpq
%{_pixmapsdir}/locolor/*x*/apps/klpq.png
%{_pixmapsdir}/hicolor/*x*/apps/klpq.png

%files knotes
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/knotes
%{_applnkdir}/Utilities/knotes.desktop
%{_datadir}/doc/kde/HTML/en/knotes
%{_datadir}/apps/knotes
%{_datadir}/config/knotesrc
%{_pixmapsdir}/locolor/*x*/apps/knotes.png
%{_pixmapsdir}/hicolor/*x*/apps/knotes.png

%files kpm
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kpm*
%{_applnkdir}/Utilities/kpm.desktop
%{_datadir}/doc/kde/HTML/en/kpm
%{_pixmapsdir}/locolor/*x*/apps/kpm.png
%{_pixmapsdir}/hicolor/*x*/apps/kpm.png

%files ktimemon
%defattr(644,root,root,755)
%{_datadir}/doc/kde/HTML/en/
%{_datadir}/apps/kicker/applets/ktimemon.desktop
%attr(755,root,root) %{_libdir}/libktimemon.??
%{_pixmapsdir}/locolor/*x*/apps/ktimemon.png
