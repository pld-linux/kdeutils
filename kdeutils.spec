Summary:	K Desktop Environment - utilities
Summary(pl):	K Desktop Environment - narzêdzia
Summary(es):	KDE - Utilitarios
Summary(pt_BR):	KDE - Utilitários
Name:		kdeutils
version:	2.2.2
Release:	7
Epoch:		6
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.bz2
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= %{version}
BuildRequires:	libxml2-progs
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_fontdir	/usr/share/fonts
%define		_htmldir	/usr/share/doc/kde/HTML

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
 - KCalc - calculadora científica,
 - KCharSelect,
 - KDESsh,
 - Kdf -
 - KEdit - editor de textos sencillo,
 - KFloppy - herramienta de formatear disquetes,
 - KFind,
 - KHexEdit - editor hexadecimal,
 - KJots - bloque de notas,
 - KLaptopDaemon,
 - KLjetTool - herramienta de configuración de impresoras HP,
 - KLpq - print manager,
 - KLprFax,
 - KNotes - recados para coger en el ambiente gráfico,
 - KPm,
 - KTimer.

%description -l pl
Narzêdzia dla KDE. Pakiet zawiera:
 - Ark - program do zarz±dzania archiwami,
 - KAb - ksi±¿ka adresowa,
 - KArm - czasomierz,
 - KCalc - kalkulator,
 - KCharSelect,
 - KDESsh - ferramenta de execução remota de programas,
 - Kdf,
 - KEdit - edytor tekstu,
 - KFloppy - narzêdzie do formatowania dyskietek,
 - KFind,
 - KHexedit - edytor plików binarnych,
 - KJots - notatnik,
 - KLaptopDaemon,
 - KLJetTool - narzêdzie dla u¿ytkowników drukarek LaserJet,
 - KLpq - zarz±dca wydruków,
 - KLprFax,
 - KNotes - inny notatnik,
 - KPm - program do zarz±dzania procesami,
 - KTimer.

%description -l pt_BR
Utilitários para o KDE. Programas disponíveis neste pacote:
 - Ark - controle de tempo pessoal,
 - KAb - gerenciador do livro de endereços,
 - KArm,
 - KCalc - calculadora científica,
 - KCharSelect,
 - KDESsh,
 - KEdit - editor de textos simples
 - KFloppy - ferramenta de formatação de disquetes,
 - KFind - ferramenta de procura de arquivos,
 - KHexEdit - editor hexadecimal,
 - KJots - bloco de notas,
 - KLaptopDaemon - miniaplicativo de status de bateria para laptops,
 - KLjetTool - ferramenta de configuração de impressoras HP,
 - KLpq - interface para gerenciamento das filas de impressão,
 - KLprFax - interface para impressão em saída de Fax
 - KNotes - recados para colar no ambiente gráfico,
 - KPm - monitor gráfico de processos e do sistema,
 - KTimer - Monitor de tempo em forma de mini-aplicativo.

%package ark
Summary:	KDE Archive Manager
Summary(pl):	Zarz±dca archiwów dla KDE
Summary(pt_BR):	Gerenciador de pacotes TAR/comprimidos do KDE
Group:		X11/Applications
Requires:	kdelibs >= %{version}

%description ark
Ark is a program for managing and quickly extracting archives.

%description ark -l pl
Ark jest programem s³u¿±cym do zarz±dzania i szybkiego rozpakowywania
archiwów.

%description ark -l pt_BR
Gerenciador de pacotes TAR/comprimidos do KDE.

%package kab
Summary:	KDE Address Book
Summary(pl):	Ksi±¿ka adresowa dla KDE
Summary(pt_BR):	Gerenciador do livro de endereços
Group:		X11/Applications
Requires:	kdelibs >= %{version}

%description kab
Kab is a simple address book for KDE.

%description kab -l pl
Kab jest prost± ksi±¿k± adresow± dla KDE.

%description kab -l pt_BR
Gerenciador do livro de endereços.

%package karm
Summary:	KDE Time Tracker
Summary(pl):	Time Tracker dla KDE
Summary(pt_BR):	Gerenciador pessoal de tempo e tarefas
Group:		X11/Applications
Requires:	kdelibs >= %{version}

%description karm
KArm is a time tracker for busy people who need to keep track of the
amount of time they spend on various tasks.

%description karm -l pl
Narzêdzie pozwalaj±ce ustaliæ ile czasu siê spêdzi³o robi±c ró¿ne
rzeczy.

%package kcalc
Summary:	KDE Calculator
Summary(pl):	Kalkulator dla KDE
Summary(pt_BR):	Calculadora do KDE
Group:		X11/Applications
Requires:	kdelibs >= %{version}

%description kcalc
Calculator for KDE.

%description kcalc -l pl
Kalkulator dla KDE.

%description kcalc -l pt_BR
Calculadora do KDE.

%package kcharselect
Summary:	KDE Character Selector
Summary(pl):	Wybierajka znaków dla KDE
Summary(pt_BR):	Ferramenta de seleção de caracteres
Group:		X11/Applications
Requires:	kdelibs >= %{version}

%description kcharselect
Character Selector.

%description kcharselect -l pl
Program do wybierania znaków.

%package kdepasswd
Summary:	KDE Passwd
Summary(pl):	passwd dla KDE
Summary(pt_BR):	Ferramenta de mudança de senha
Group:		X11/Applications
Requires:	kdelibs >= %{version}

%description kdepasswd
Change your password.

%description kdepasswd -l pl
Program do zmiany has³a z poziomu KDE.

%description kdepasswd -l pt_BR
Ferramenta de mudança de senha.

%package kdessh
Summary:	KDE SSH Frontend
Summary(pl):	Frontend SSH dla KDE
Summary(pt_BR):	Ferramenta de execução remota de programas
Group:		X11/Applications
Requires:	kdelibs >= %{version}

%description kdessh
SSH Frontend.

%description kdessh -l pl
Frontend SSH dla KDE.

%description kdessh -l pt_BR
Ferramenta de execução remota de programas.

%package kedit
Summary:	KDE Text Editor
Summary(pl):	Edytor tekstu dla KDE
Summary(pt_BR):	Editor de texto melhorado do KDE
Group:		X11/Applications
Requires:	kdelibs >= %{version}

%description kedit
Simple text editor for KDE.

%description kedit -l pl
Prosty edytor tekstu dla KDE.

%description kedit -l pt_BR
Editor de texto melhorado do KDE.

%package kdf
Summary:	KDE Disk space GUI
Summary(pl):	df dla KDE
Summary(pt_BR):	Mostra o status de espaço em disco
Group:		X11/Applications
Requires:	kdelibs >= %{version}

%description kdf
This program shows the disk usage of the mounted devices.

%description kdf -l pl
Ten program pokazuje zajêto¶æ dysku dla zamontowanych urz±dzeñ.

%description kdf -l pt_BR
Mostra o status de espaço em disco.

%package kfind
Summary:	KDE Find
Summary(pl):	find dla KDE
Summary(pt_BR):	Ferramenta de procura de arquivos
Group:		X11/Applications
Requires:	kdelibs >= %{version}
Requires:	kdebase = %{version}

%description kfind
Find Util.

%description kfind -l pl
Wyszukiwarka plików dla KDE.

%description kfind -l pt_BR
Ferramenta de procura de arquivos.

%package kfloppy
Summary:	KDE Floppy Formater
Summary(pl):	Program formatuj±cy dyskietki dla KDE
Summary(pt_BR):	Ferramenta de formatação de disquetes
Group:		X11/Applications
Requires:	kdelibs >= %{version}
Requires:	dosfstools

%description kfloppy
KFloppy formats disks and puts a DOS or ext2fs filesystem on them.

%description kfloppy -l pl
KFloppy formatuje dyskietki i zak³ada na nich system pliku DOS lub
ext2.

%description kfloppy -l pt_BR
Ferramenta de formatação de disquetes.

%package khexedit
Summary:	KDE Hex Editor
Summary(pl):	Edytor szesnastkowy dla KDE
Summary(pt_BR):	Editor hexadecimal para arquivos binários
Group:		X11/Applications
Requires:	kdelibs >= %{version}
Obsoletes:	khexedit

%description khexedit
Hex Editor is a small and simple viewer for binary files.

%description khexedit -l pl
Hex Editor jest ma³ym i prostym edytorem plików binarnych.

%description khexedit -l pt_BR
Editor hexadecimal para arquivos binários.

%package kjots
Summary:	KDE Note taker
Summary(pl):	Notatnik dla KDE
Summary(pt_BR):	Ferramenta de armazenamento de livros
Group:		X11/Applications
Requires:	kdelibs >= %{version}

%description kjots
kjots is a small note taker program. Name and idea are taken from the
jots program included in the tkgoodstuff package.

%description kjots -l pl
KJots to ma³y program do zapisywania notatek.

%description kjots -l pt_BR
Ferramenta de armazenamento de livros.

%package klaptopdaemon
Summary:	KDE Laptop Daemon
Summary(pl):	Wska¼nik zu¿ycia baterii w laptopie dla KDE
Summary(pt_BR):	Miniaplicativo de status de bateria para laptops
Group:		X11/Applications
Requires:	kdelibs >= %{version}

%description klaptopdaemon
KDE Laptop Daemon.

%description klaptopdaemon -l pl
Wska¼nik zu¿ycia baterii w laptopie dla KDE.

%description klaptopdaemon -l pt_BR
Miniaplicativo de status de bateria para laptops

%package kljettool
Summary:	KDE LaserJet Tool
Summary(pl):	Konfigurator drukarek LaserJet dla KDE
Summary(pt_BR):	Interface de configuração de impressora HP Laserjet
Group:		X11/Applications
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

%description kljettool -l pl
KLJetToll to program umo¿liwiaj±cy konfiguracjê drukarek Hewlett
Packard LaserJet.

%description kljettool -l pt_BR
Interface de configuração de impressora HP Laserjet.

%package klpq
Summary:	KDE Print Manager
Summary(pl):	Zarz±dca wydruku dla KDE
Summary(pt_BR):	Interface para gerenciamento das filas de impressão
Group:		X11/Applications
Requires:	kdelibs >= %{version}

%description klpq
Klpq is a frontend to the print spooler. Klpq does not modify the
printqueue by itself, but uses the underlying commands: lpq, lprm and
lpc.

%description klpq -l pl
Klpq jest nak³adk± graficzn± dla KDE, umo¿liwiaj±c± zarz±dzanie
wydrukami. Nie modyfikuje kolejki wydruków sammodzielnie, lecz
wykorzystuje do tego celu polecenia: lpq, lprm i lpc.

%description klpq -l pt_BR
Interface para gerenciamento das filas de impressão.

%package klprfax
Summary:	KDE LPD fax frontend using efax
Summary(pl):	Frontend do faksu via lpd dla KDE
Summary(pt_BR):	Interface para impressão em saída de Fax
Group:		X11/Applications
Requires:	kdelibs >= %{version}
Requires:	efax

%description klprfax
With this program you can fax by printing to an lpd device.

%description klprfax -l pl
Program ten umo¿liwia wysy³anie faksów przez drukowanie ich do lpd.

%description klprfax -l pt_BR
Interface para impressão em saída de fax.

%package knotes
Summary:	KDE Notes
Summary(pl):	Notes dla KDE
Summary(pt_BR):	Pequeno editor de texto para guardar notas rápidas
Group:		X11/Applications
Requires:	kdelibs >= %{version}

%description knotes
KNotes is ment to be a really usable and good looking notes
application for the KDE project.

%description knotes -l pl
KNotes to program umo¿liwiaj±cy spisywanie notatek i trzymanie ich
widocznych na ekranie.

%description knotes -l pt_BR
Pequeno editor de texto para guardar notas rápidas.

%package kpm
Summary:	KDE Process Manager
Summary(pl):	Zarz±dca procesów dla KDE
Summary(pt_BR):	Monitor gráfico de processos e do sistema
Group:		X11/Applications
Requires:	kdelibs >= %{version}

%description kpm
kpm allows you to view and modify the processes of your Linux
computer. It shows detailed information of running processes, computer
resources like RAM, swap space, CPU utilization and so on. You can
kill processes and modify their priority.

%description kpm -l pl
kpm umo¿liwia Ci zarz±dzanie procesami w Twoim systemie. Wy¶wietla
szczegó³owe informacje na temat uruchomionych procesów, zasobów
systemu jak np. wielko¶æ u¿ywanej pamiêci czy partycji wymiany,
wykorzystanie procesora, itp. Masz mo¿liwo¶æ zabijania procesów i
modyfikowania ich priorytetów.

%description kpm -l pt_BR
Monitor gráfico de processos e do sistema.

%package ktimer
Summary:	KDE Timer
Summary(pl):	Zegarek KDE
Summary(pt_BR):	Monitor de tempo em forma de mini-aplicativo
Group:		X11/Applications
Requires:	kdelibs >= %{version}

%description ktimer
Time tracker appplet.

%description ktimer -l pl
Zegarek.

%description ktimer -l pt_BR
Monitor de tempo em forma de mini-aplicativo.

%package devel
Summary:	Header files for compiling applications that use kdeutils libraries
Summary(pl):	Pliki nag³ówkowe do kompilacji aplikacji u¿ywaj±cych bibliotek kde
Summary(pt_BR):	Arquivos de inclusão para as bibliotecas do kdeutils
Group:		X11/Development/Libraries
Requires:	kdelibs-devel >= %{version}
Requires:	kdebase-devel >= %{version}

%description devel
This package includes the header files you will need to compile
applications that use kdeutils libraries.

%description devel -l pl
Ten pakiet zawiera pliki nag³ówkowe niezbêdne do kompilacji aplikacji
u¿ywaj±cych bibliotek kdeutils.

%description devel -l pt_BR
Arquivos de inclusão para desenvolvimento e compilação de programas
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
%attr(755,root,root) %{_libdir}/libark.so.*.*.*
%{_applnkdir}/Utilities/ark.desktop
%{_datadir}/apps/ark
%{_datadir}/apps/konqueror/servicemenus/arkservicemenu.desktop
%{_datadir}/services/arkpart.desktop
%{_pixmapsdir}/*/*/apps/ark.*
%{_htmldir}/en/ark

%files kab
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kab
%{_applnkdir}/Utilities/kab.desktop
%{_datadir}/apps/kab/htmlexport
%{_datadir}/apps/kab/pics/*
%{_pixmapsdir}/*/*/apps/kab.*
%{_htmldir}/en/kab

%files karm
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/karm
%{_applnkdir}/Utilities/karm.desktop
%{_datadir}/apps/karm
%{_pixmapsdir}/*/*/apps/karm.*
%{_htmldir}/en/karm

%files kcalc
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kcalc
%attr(755,root,root) %{_libdir}/kcalc.*
%{_applnkdir}/Utilities/kcalc.desktop
%{_datadir}/apps/kcalc
%{_pixmapsdir}/*/*/apps/kcalc.*
%{_htmldir}/en/kcalc

%files kcharselect
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kcharselect
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
%{_htmldir}/en/kdf

%files kedit
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kedit
%attr(755,root,root) %{_libdir}/kde2/kedit.*
%{_applnkdir}/Development/Editors/KEdit.desktop
%{_datadir}/apps/kedit
%{_pixmapsdir}/*/*/apps/kedit.*
%{_htmldir}/en/kedit

%files kfind
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kfind
%attr(755,root,root) %{_libdir}/kfind.*
%{_applnkdir}/Kfind.desktop
%{_pixmapsdir}/*/*/apps/kfind.*
%{_htmldir}/en/kfind

%files kfloppy
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kfloppy
%{_applnkdir}/Utilities/KFloppy.desktop
%{_datadir}/apps/kfloppy
%{_pixmapsdir}/*/*/apps/kfloppy.*
%{_htmldir}/en/kfloppy

%files khexedit
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/khexedit
%{_applnkdir}/Utilities/khexedit.desktop
%{_datadir}/apps/khexedit
%{_pixmapsdir}/*/*/apps/khexedit.*
%{_htmldir}/en/khexedit

%files kjots
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kjots
%{_applnkdir}/Utilities/Kjots.desktop
%{_datadir}/apps/kjots
%{_pixmapsdir}/*/*/apps/kjots.*
%{_htmldir}/en/kjots

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
%{_htmldir}/en/kljettool

%files klpq
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/klpq
%{_applnkdir}/Utilities/KLpq.desktop
%{_pixmapsdir}/*/*/apps/klpq.*
%{_htmldir}/en/klpq

%files klprfax
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/klprfax*
%{_applnkdir}/Utilities/klprfax.desktop
%{_pixmapsdir}/*/*/apps/klprfax.*
%{_htmldir}/en/klprfax

%files knotes
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/knotes
%{_applnkdir}/Utilities/knotes.desktop
%{_datadir}/apps/knotes
%{_datadir}/config/knotesrc
%{_pixmapsdir}/*/*/apps/knotes.*
%{_htmldir}/en/knotes

%files kpm
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kpm
%attr(755,root,root) %{_bindir}/kpmdocked
%{_applnkdir}/System/kpm.desktop
%{_pixmapsdir}/*/*/apps/kpm.*
%{_htmldir}/en/kpm

%files ktimer
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ktimer
%{_applnkdir}/Utilities/ktimer.desktop

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libark.??
%attr(755,root,root) %{_libdir}/libkcharselectapplet.??
%{_includedir}/*
