Summary:	K Desktop Environment - utilities
Summary(pl):	K Desktop Environment - narz�dzia
Summary(es):	KDE - Utilitarios
Summary(pt_BR):	KDE - Utilit�rios
Name:		kdeutils
version:	2.2.2
Release:	2
Epoch:		6
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplica��es
Group(pt):	X11/Aplica��es
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.bz2
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= %{version}
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _prefix         /usr/X11R6
%define         _fontdir        /usr/share/fonts
%define         _htmldir        %{_datadir}/doc/kde/HTML

%description
KDE utilities. Package includes:
 - Ark - archive manager,
 - KAb - address book,
 - KArm - time tracker,
 - KCalc - calculator KCharSelect,
 - KCharSelect - character Selector,
 - KDEPasswd,
 - KDESsh - SSH rontend,
 - Kdf - disk space GUI,
 - KEdit - text editor,
 - KFind - find frontend,
 - KFloppy - floppy formating tool,
 - KHexEdit - HEX file editor,
 - KJots - note taker,
 - KLaptopDaemon - laptop daemon,
 - KLipper - clipboard viewer,
 - KLJetTool - tool for LaserJet priter users,
 - KLpq - print manager,
 - KLprFax - LPD fax frontend using efax,
 - KNotes - notes,
 - KPm - process manager,
 - KTimer - timer,
 - KTop - task manager,
 - KTreeBrowser,
 - KWrite - text editor.

%description -l es
Utilitarios para KDE. Programas disponibles en este paquete:
 - Ark,
 - KAb,
 - KArm - control de tiempo personal,
 - KCalc - calculadora cient�fica,
 - KCharSelect,
 - KDESsh,
 - Kdf -
 - KEdit - editor de textos sencillo,
 - KFloppy - herramienta de formatear disquetes,
 - KFind,
 - KHexEdit - editor hexadecimal,
 - KJots - bloque de notas,
 - KLaptopDaemon,
 - KLjetTool - herramienta de configuraci�n de impresoras HP,
 - KLpq - print manager,
 - KLprFax,
 - KNotes - recados para coger en el ambiente gr�fico,
 - KPm,
 - KTimer.

%description -l pl
Narz�dzia dla KDE. Pakiet zawiera:
 - Ark - program do zarz�dzania archiwami,
 - KAb - ksi��ka adresowa,
 - KArm - czasomierz,
 - KCalc - kalkulator,
 - KCharSelect,
 - KDESsh - ferramenta de execu��o remota de programas,
 - Kdf,
 - KEdit - edytor tekstu,
 - KFloppy - narz�dzie do formatowania dyskietek,
 - KFind,
 - KHexedit - edytor plik�w binarnych,
 - KJots - notatnik,
 - KLaptopDaemon,
 - KLJetTool - narz�dzie dla u�ytkownik�w drukarek LaserJet,
 - KLpq - zarz�dca wydruk�w,
 - KLprFax,
 - KNotes - inny notatnik,
 - KPm - program do zarz�dzania procesami,
 - KTimer.

%description -l pt_BR
Utilit�rios para o KDE. Programas dispon�veis neste pacote:
 - Ark - controle de tempo pessoal,
 - KAb - gerenciador do livro de endere�os,
 - KArm,
 - KCalc - calculadora cient�fica,
 - KCharSelect,
 - KDESsh,
 - KEdit - editor de textos simples
 - KFloppy - ferramenta de formata��o de disquetes,
 - KFind - ferramenta de procura de arquivos,
 - KHexEdit - editor hexadecimal,
 - KJots - bloco de notas,
 - KLaptopDaemon - miniaplicativo de status de bateria para laptops,
 - KLjetTool - ferramenta de configura��o de impressoras HP,
 - KLpq - interface para gerenciamento das filas de impress�o,
 - KLprFax - interface para impress�o em sa�da de Fax
 - KNotes - recados para colar no ambiente gr�fico,
 - KPm - monitor gr�fico de processos e do sistema,
 - KTimer - Monitor de tempo em forma de mini-aplicativo.

%package ark
Summary:	KDE Archive Manager 
Summary(pl):	Zarz�dca archiw�w dla KDE
Summary(pt_BR):	Gerenciador de pacotes TAR/comprimidos do KDE
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplica��es
Group(pt):	X11/Aplica��es
Requires:	kdelibs >= %{version}

%description ark
Ark is a program for managing and quickly extracting archives.

%description -l pl ark
Ark jest programem s�u��cym do zarz�dzania i szybkiego rozpakowywania
archiw�w.

%description -l pt_BR ark
Gerenciador de pacotes TAR/comprimidos do KDE.

%package kab
Summary:	KDE Address Book
Summary(pl):	Ksi��ka adresowa dla KDE
Summary(pt_BR):	Gerenciador do livro de endere�os
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplica��es
Group(pt):	X11/Aplica��es
Requires:	kdelibs >= %{version}

%description kab
Kab is a simple address book for KDE.

%description -l pl kab
Kab jest prost� ksi��k� adresow� dla KDE.

%description -l pt_BR kab
Gerenciador do livro de endere�os.

%package karm
Summary:	KDE Time Tracker
Summary(pl):	Time Tracker dla KDE
Summary(pt_BR):	Gerenciador pessoal de tempo e tarefas
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplica��es
Group(pt):	X11/Aplica��es
Requires:	kdelibs >= %{version}

%description karm
KArm is a time tracker for busy people who need to keep track of the
amount of time they spend on various tasks.

%description -l pl karm
Narz�dzie pozwalaj�ce ustali� ile czasu si� sp�dzi�o robi�c r�ne
rzeczy.

%package kcalc
Summary:	KDE Calculator	
Summary(pl):	Kalkulator dla KDE
Summary(pt_BR):	Calculadora do KDE
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplica��es
Group(pt):	X11/Aplica��es
Requires:	kdelibs >= %{version}

%description kcalc
Calculator for KDE.

%description -l pl kcalc
Kalkulator dla KDE.

%description -l pt_BR kcalc
Calculadora do KDE.

%package kcharselect
Summary:	KDE Character Selector
Summary(pt_BR):	Ferramenta de sele��o de caracteres
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplica��es
Group(pt):	X11/Aplica��es
Requires:	kdelibs >= %{version}

%description kcharselect
Character Selector.

%package kdepasswd
Summary:	KDE Passwd
Summary(pt_BR):	Ferramenta de mudan�a de senha
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplica��es
Group(pt):	X11/Aplica��es
Requires:	kdelibs >= %{version}

%description kdepasswd
Change your password.

%description -l pt_BR kdepasswd
Ferramenta de mudan�a de senha.

%package kdessh
Summary:	KDE SSH Frontend
Summary(pt_BR):	Ferramenta de execu��o remota de programas
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplica��es
Group(pt):	X11/Aplica��es
Requires:	kdelibs >= %{version}

%description kdessh
SSH Frontend.

%description -l pt_BR kdessh
Ferramenta de execu��o remota de programas.

%package kedit
Summary:	KDE Text Editor	
Summary(pl):	Edytor tekstu dla KDE
Summary(pt_BR):	Editor de texto melhorado do KDE
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplica��es
Group(pt):	X11/Aplica��es
Requires:	kdelibs >= %{version}

%description kedit
Simple text editor for KDE.

%description -l pl kedit
Prosty edytor tekstu dla KDE.

%description -l pt_BR kedit
Editor de texto melhorado do KDE.

%package kdf
Summary:	KDE Disk space GUI
Summary(pt_BR):	Mostra o status de espa�o em disco
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplica��es
Group(pt):	X11/Aplica��es
Requires:	kdelibs >= %{version}

%description kdf
This program shows the disk usage of the mounted devices.

%description -l pt_BR kdf
Mostra o status de espa�o em disco.

%package kfind
Summary:	KDE Find
Summary(pt_BR):	Ferramenta de procura de arquivos
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplica��es
Group(pt):	X11/Aplica��es
Requires:	kdelibs >= %{version}

%description kfind
Find Util.

%description -l pt_BR kfind
Ferramenta de procura de arquivos.

%package kfloppy
Summary:	KDE Floppy Formater	
Summary(pl):	Program formatuj�cy dyskietki dla KDE
Summary(pt_BR):	Ferramenta de formata��o de disquetes
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplica��es
Group(pt):	X11/Aplica��es
Requires:	kdelibs >= %{version}
Requires:	dosfstools
	
%description kfloppy
KFloppy formats disks and puts a DOS or ext2fs filesystem on them.

%description -l pl kfloppy
KFloppy formatuje dyskietki i zak�ada na nich system pliku DOS lub
ext2.

%description -l pt_BR kfloppy
Ferramenta de formata��o de disquetes.

%package khexedit
Summary:	KDE Hex Editor	
Summary(pl):	Edytor szesnastkowy dla KDE
Summary(pt_BR):	Editor hexadecimal para arquivos bin�rios
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplica��es
Group(pt):	X11/Aplica��es
Requires:	kdelibs >= %{version}
Obsoletes:	khexedit

%description khexedit
Hex Editor is a small and simple viewer for binary files.

%description -l pl khexedit
Hex Editor jest ma�ym i prostym edytorem plik�w binarnych.

%description -l pt_BR khexedit
Editor hexadecimal para arquivos bin�rios.

%package kjots
Summary:	KDE Note taker
Summary(pl):	Notatnik dla KDE
Summary(pt_BR):	Ferramenta de armazenamento de livros
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplica��es
Group(pt):	X11/Aplica��es
Requires:	kdelibs >= %{version}

%description kjots
kjots is a small note taker program. Name and idea are taken from the
jots program included in the tkgoodstuff package.

%description -l pl kjots
KJots to ma�y program do zapisywania notatek.

%description -l pt_BR kjots
Ferramenta de armazenamento de livros.

%package klaptopdaemon
Summary:	KDE Laptop Daemon
Summary(pt_BR):	Miniaplicativo de status de bateria para laptops
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplica��es
Group(pt):	X11/Aplica��es
Requires:	kdelibs >= %{version}

%description klaptopdaemon
KDE Laptop Daemon.

%description -l pt_BR klaptopdaemon
Miniaplicativo de status de bateria para laptops

%package kljettool
Summary:	KDE LaserJet Tool	
Summary(pl):	Konfigurator drukarek LaserJet dla KDE
Summary(pt_BR):	Interface de configura��o de impressora HP Laserjet
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplica��es
Group(pt):	X11/Aplica��es
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
KLJetToll to program umo�liwiaj�cy konfiguracj� drukarek Hewlett
Packard LaserJet.

%description -l pt_BR kljettool
Interface de configura��o de impressora HP Laserjet.

%package klpq 
Summary:	KDE Print Manager
Summary(pl):	Zarz�dca wydruku dla KDE
Summary(pt_BR):	Interface para gerenciamento das filas de impress�o
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplica��es
Group(pt):	X11/Aplica��es
Requires:	kdelibs >= %{version}

%description klpq
Klpq is a frontend to the print spooler. Klpq does not modify the
printqueue by itself, but uses the underlying commands: lpq, lprm and
lpc.

%description -l pl klpq
Klpq jest nak�adk� graficzn� dla KDE, umo�liwiaj�c� zarz�dzanie
wydrukami. Nie modyfikuje kolejki wydruk�w sammodzielnie, lecz
wykorzystuje do tego celu polecenia: lpq, lprm i lpc.

%description -l pt_BR klpq
Interface para gerenciamento das filas de impress�o.

%package klprfax
Summary:	KDE LPD fax frontend using efax
Summary(pt_BR):	Interface para impress�o em sa�da de Fax
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplica��es
Group(pt):	X11/Aplica��es
Requires:	kdelibs >= %{version}
Requires:	efax

%description klprfax
With this program you can fax by printing to an lpd device.

%description -l pt_BR klprfax
Interface para impress�o em sa�da de fax.

%package knotes 
Summary:	KDE Notes
Summary(pl):	Notes dla KDE
Summary(pt_BR):	Pequeno editor de texto para guardar notas r�pidas
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplica��es
Group(pt):	X11/Aplica��es
Requires:	kdelibs >= %{version}

%description knotes
KNotes is ment to be a really usable and good looking notes
application for the KDE project.

%description -l pl knotes
KNotes to program umo�liwiaj�cy spisywanie notatek i trzymanie ich
widocznych na ekranie.

%description -l pt_BR knotes
Pequeno editor de texto para guardar notas r�pidas.

%package kpm
Summary:	KDE Process Manager
Summary(pl):	Zarz�dca proces�w dla KDE
Summary(pt_BR):	Monitor gr�fico de processos e do sistema
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplica��es
Group(pt):	X11/Aplica��es
Requires:	kdelibs >= %{version}

%description kpm
kpm allows you to view and modify the processes of your Linux
computer. It shows detailed information of running processes, computer
resources like RAM, swap space, CPU utilization and so on. You can
kill processes and modify their priority.

%description -l pl kpm
kpm umo�liwia Ci zarz�dzanie procesami w Twoim systemie. Wy�wietla
szczeg�owe informacje na temat uruchomionych proces�w, zasob�w
systemu jak np. wielko�� u�ywanej pami�ci czy partycji wymiany,
wykorzystanie procesora, itp. Masz mo�liwo�� zabijania proces�w i
modyfikowania ich priorytet�w.

%description -l pt_BR kpm
Monitor gr�fico de processos e do sistema.

%package ktimer
Summary:	KDE Timer
Summary(pt_BR):	Monitor de tempo em forma de mini-aplicativo
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplica��es
Group(pt):	X11/Aplica��es
Requires:	kdelibs >= %{version}

%description ktimer
Time tracker appplet.

%description -l pt_BR ktimer
Monitor de tempo em forma de mini-aplicativo.

%package devel
Summary:	Header files for compiling applications that use kdeutils libraries.
Summary(pt_BR):	Arquivos de inclus�o para as bibliotecas do kdeutils
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(es):	X11/Desarrollo/Bibliotecas
Group(fr):	X11/Development/Librairies
Group(pl):	X11/Programowanie/Biblioteki
Group(pt_BR):	X11/Desenvolvimento/Bibliotecas
Group(ru):	X11/����������/����������
Group(uk):	X11/��������/��̦�����
Requires:	kdelibs-devel >= %{version}
Requires:	kdebase-devel >= %{version}

%description devel
This package includes the header files you will need to compile
applications that use kdeutils libraries.

%description -l pt_BR devel
Arquivos de inclus�o para desenvolvimento e compila��o de programas
que usem as bibliotecas do kdeutils

%prep
%setup -q
%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

%{__make} -f Makefile.cvs
%configure \
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

%post   ark -p /sbin/ldconfig
%postun ark -p /sbin/ldconfig

%post   kcharselect -p /sbin/ldconfig
%postun kcharselect -p /sbin/ldconfig

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

%files khexedit
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

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/libark.so
%attr(755,root,root) %{_libdir}/libkcharselectapplet.so
%{_includedir}/*
