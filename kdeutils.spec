#
# Conditional build:
%bcond_without  i18n    # dont build i18n subpackage
#
%define		_state		stable
%define		_ver		3.2.0
##%define		_snap		040110

Summary:	K Desktop Environment - utilities
Summary(pl):	K Desktop Environment - narzêdzia
Summary(es):	KDE - Utilitarios
Summary(ja):	KDE¥Ç¥¹¥¯¥È¥Ã¥×´Ä¶­ - ¥æ¡¼¥Æ¥£¥ê¥Æ¥£
Summary(pt_BR):	KDE - Utilitários
Summary(ru):	K Desktop Environment - õÔÉÌÉÔÙ
Summary(uk):	K Desktop Environment - õÔÉÌ¦ÔÉ
Summary(zh_CN):	KDEÊµÓÃ¹¤¾ß
Name:		kdeutils
Version:	%{_ver}
Release:	3
Epoch:		9
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{name}-%{version}.tar.bz2
# Source0-md5:	988480b534c1fab9003f624edb87e7a7
#Source0:	http://ep09.pld-linux.org/~djurban/kde/%{name}-%{version}.tar.bz2
%if %{with i18n}
Source1:        http://ep09.pld-linux.org/~djurban/kde/i18n/kde-i18n-%{name}-%{version}.tar.bz2
# Source1-md5:	e63a7e83445904676217d3f09243ce90
%endif
Patch0:		%{name}-3.2branch.diff
Patch1:		%{name}-kdf-label.patch
#Patch1:		%{name}-kedit-confirmoverwrite.patch
#Patch2:		%{name}-fix-kdf-mem-leak.patch
Patch3:		%{name}-vcategories.patch
Patch4:		%{name}-userinfo.patch
Patch5:		%{name}-gcc34.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bzip2
BuildRequires:	ed
BuildRequires:	kdebase-devel >= 9:%{version}
BuildRequires:	libxml2-progs
BuildRequires:	libtool
%ifarch ppc
BuildRequires:	pbbuttonsd-lib >= 0.5.6-2
%endif
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KDE utilities. Package includes:
 - Ark - archive manager,
 - KAb - address book,
 - KArm - time tracker,
 - KCalc - calculator KCharSelect,
 - KCharSelect - character Selector,
 - KDEPasswd,
 - KDESsh - SSH frontend,
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
 - ksim - system monitor.

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
 - ksim

%description -l ja
KDE¥Ç¥¹¥¯¥È¥Ã¥×´Ä¶­ÍÑ¤Î¥æ¡¼¥Æ¥£¥ê¥Æ¥£
°Ê²¼¤Î¤è¤¦¤Ê¥Ñ¥Ã¥±¡¼¥¸¤¬Æþ¤Ã¤Æ¤¤¤Þ¤¹¡£

- ark - ¥¢¡¼¥«¥¤¥ÖÁàºî¥Ä¡¼¥ë
- karm - personal time tracker
- kcalc - ÅÅÂî
- kedit - ¥Æ¥­¥¹¥È¥¨¥Ç¥£¥¿
- kfloppy - ¥Õ¥í¥Ã¥Ô¡¼¥Õ¥©¡¼¥Þ¥Ã¥¿
- khexedit - ¥Ð¥¤¥Ê¥ê¥¨¥Ç¥£¥¿
- kjots - note taker
- kljettool - HP¥×¥ê¥ó¥¿ÀßÄê¥Ä¡¼¥ë
- knotes - ¥Ý¥¹¥È¥¤¥Ã¥È

%description -l pl
Narzêdzia dla KDE. Pakiet zawiera:
 - Ark - program do zarz±dzania archiwami,
 - KAb - ksi±¿ka adresowa,
 - KArm - czasomierz,
 - KCalc - kalkulator,
 - KCharSelect,
 - KDESsh - narzêdzie do zdalnego wykonywania programów,
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
 - ksim - monitor systemu

%description -l pt_BR
Utilitários para o KDE. Programas disponíveis neste pacote:
 - Ark - controle de tempo pessoal,
 - KAb - gerenciador do livro de endereços,
 - KArm,
 - KCalc - calculadora científica,
 - KCharSelect,
 - KDESsh - ferramenta de execução remota de programas,
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

%description -l ru
õÔÉÌÉÔÙ ÄÌÑ K Desktop Environment. ÷ËÌÀÞÁÅÔ:
 - ark - ÍÅÎÅÄÖÅÒ ÁÒÈÉ×Ï× tar/gzip,
 - kab - ÁÄÒÅÓÎÁÑ ËÎÉÇÁ,
 - karm - ÐÅÒÓÏÎÁÌØÎÙÊ ÐÌÁÎÉÒÏ×ÝÉË,
 - kcalc - ÎÁÕÞÎÙÊ ËÁÌØËÕÌÑÔÏÒ,
 - kedit - ÐÒÏÓÔÏÊ ÔÅËÓÔÏ×ÙÊ ÒÅÄÁËÔÏÒ,
 - kfloppy - ÕÔÉÌÉÔÁ ÄÌÑ ÆÏÒÍÁÔÉÒÏ×ÁÎÉÑ ÆÌÏÐÐÉ-ÄÉÓËÏ×,
 - khexedit - ÒÅÄÁËÔÏÒ ÂÉÎÁÒÎÙÈ ÆÁÊÌÏ×,
 - kjots - ÂÌÏËÎÏÔ,
 - klipper - ÕÔÉÌÉÔÁ ÄÌÑ ÒÁÂÏÔÙ Ó ÂÕÆÅÒÏÍ ÏÂÍÅÎÁ,
 - kljettool - ÕÔÉÌÉÔÁ ÄÌÑ ÎÁÓÔÒÏÊËÉ ÐÒÉÎÔÅÒÏ×, ÓÏ×ÍÅÓÔÉÍÙÈ Ó HP,
 - klpq - ÍÅÎÅÄÖÅÒ ÏÞÅÒÅÄÉ ÐÅÞÁÔÉ,
 - knotes - post-it notes ÄÌÑ ÄÅÓËÔÏÐÁ,
 - kpm - ÍÅÎÅÄÖÅÒ ÐÒÏÃÅÓÓÏ×, ÐÏÈÏÖÉÊ ÎÁ 'top', ÎÏ ÂÏÌÅÅ ÐÒÏÄ×ÉÎÕÔÙÊ.

%description -l uk
õÔÉÌÉÔÙ ÄÌÑ K Desktop Environment. í¦ÓÔÉÔØ:
 - ark - ÍÅÎÅÄÖÅÒ ÁÒÈ¦×¦× tar/gzip,
 - kab - ÁÄÒÅÓÎÁ ËÎÉÇÁ,
 - karm - ÐÅÒÓÏÎÁÌØÎÙÊ ÐÌÁÎÕ×ÁÌØÎÉË,
 - kcalc - ÎÁÕÞÎÉÊ ËÁÌØËÕÌÑÔÏÒ,
 - kedit - ÐÒÏÓÔÉÊ ÔÅËÓÔÏ×ÉÊ ÒÅÄÁËÔÏÒ,
 - kfloppy - ÕÔÉÌ¦ÔÁ ÄÌÑ ÆÏÒÍÁÔÕ×ÁÎÎÑ ÆÌÏÐ¦-ÄÉÓË¦×,
 - khexedit - ÒÅÄÁËÔÏÒ Â¦ÎÁÒÎÉÈ ÆÁÊÌ¦×,
 - kjots - ÎÏÔÁÔÎÉË,
 - klipper - ÕÔÉÌ¦ÔÁ ÄÌÑ ÒÏÂÏÔÉ Ú ÂÕÆÅÒÏÍ ÏÂÍ¦ÎÕ,
 - kljettool - ÕÔÉÌ¦ÔÁ ÄÌÑ ÎÁÌÁÇÏÄÖÅÎÎÑ ÐÒ¦ÎÔÅÒ¦×, ÓÕÍ¦ÓÎÉÈ Ú HP,
 - klpq - ÍÅÎÅÄÖÅÒ ÞÅÒÇÉ ÄÒÕËÕ,
 - knotes - post-it notes ÄÌÑ ÄÅÓËÔÏÐÕ,
 - kpm - ÍÅÎÅÄÖÅÒ ÐÒÏÃÅÓ¦×, ÓÈÏÖÉÊ ÎÁ 'top', ÁÌÅ Ú Â¦ÌØÛÉÍÉ
   ÍÏÖÌÉ×ÏÓÔÑÍÉ.

%package devel
Summary:	Header files for compiling applications that use kdeutils libraries
Summary(pl):	Pliki nag³ówkowe do kompilacji aplikacji u¿ywaj±cych bibliotek kdeutils
Summary(pt_BR):	Arquivos de inclusão para as bibliotecas do kdeutils
Group:		X11/Development/Libraries
Requires:	kdebase-devel >= 9:%{version}
Requires:	%{name}-klaptopdaemon = %{epoch}:%{version}-%{release}
Requires:	%{name}-kmilo = %{epoch}:%{version}-%{release}
Requires:	%{name}-kregexpeditor = %{epoch}:%{version}-%{release}
Requires:	%{name}-ksim = %{epoch}:%{version}-%{release}

%description devel
This package includes the header files you will need to compile
applications that use kdeutils libraries.

%description devel -l pl
Ten pakiet zawiera pliki nag³ówkowe niezbêdne do kompilacji aplikacji
u¿ywaj±cych bibliotek kdeutils.

%description devel -l pt_BR
Arquivos de inclusão para desenvolvimento e compilação de programas
que usem as bibliotecas do kdeutils

%package ark
Summary:	KDE Archive Manager
Summary(pl):	Zarz±dca archiwów dla KDE
Summary(pt_BR):	Gerenciador de pacotes TAR/comprimidos do KDE
Group:		X11/Applications
Requires:	kdebase-core >= 9:%{version}

%description ark
Ark is a program for managing and quickly extracting archives.

%description ark -l pl
Ark jest programem s³u¿±cym do zarz±dzania i szybkiego rozpakowywania
archiwów.

%description ark -l pt_BR
Gerenciador de pacotes TAR/comprimidos do KDE.

%package kcalc
Summary:	KDE Calculator
Summary(pl):	Kalkulator dla KDE
Summary(pt_BR):	Calculadora do KDE
Group:		X11/Applications
Requires:	kdebase-core >= 9:%{version}
Obsoletes:	kcalc

%description kcalc
Calculator for KDE.

%description kcalc -l pl
Kalkulator dla KDE.

%description kcalc -l pt_BR
Calculadora do KDE.

%package kcharselect
Summary:	KDE Character Selector
Summary(pl):	Program do wybierania znaków dla KDE
Summary(pt_BR):	Ferramenta de seleção de caracteres
Group:		X11/Applications
Requires:	kdebase-core >= 9:%{version}
Obsoletes:	kcharselect

%description kcharselect
Character Selector.

%description kcharselect -l pl
Program do wybierania znaków.

%package kdelirc
Summary:	KDE frontend for the Linux Infrared Remote Control system
Summary(pl):	Frontend KDE dla systemu LIRC (zdalnego sterowania podczerwieni±)
Group:		X11/Applications
Requires:	kdebase-core >= 9:%{version}

%description kdelirc
KDELIRC is a KDE frontend for the Linux Infrared Remote Control
system. It has two aims:
- provide a control center module for configuration of application
  bindings to remote control buttons and actual remote controls
  installed (i.e. lirc configuration).
- provide a system-tray applet to act as a proxy between the LIRC
  system and KDE (applications).

%description kdelirc -l pl
KDELIRC to frontend KDE dla systemu LIRC (Linux Infrared Remote
Control - zdalnego sterowania podczerwieni±). Ma dwa cele:
- zapewnienie modu³u dla centrum sterowania do konfiguracji dowi±zañ
  aplikacji do przycisków pilota oraz konfiguracji samych pilotów
  (czyli konfiguracji lirc)
- zapewnienie apletu tacki systemowej s³u¿±cego jako proxy pomiêdzy
  systemem LIRC oraz KDE (aplikacjami).

%package kdepasswd
Summary:	KDE Passwd
Summary(pl):	passwd dla KDE
Summary(pt_BR):	Ferramenta de mudança de senha
Group:		X11/Applications
Requires:	kdelibs >= 9:%{version}
Obsoletes:	kdepasswd

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
Requires:	kdelibs >= 9:%{version}
Obsoletes:	kdessh

%description kdessh
SSH Frontend.

%description kdessh -l pl
Frontend SSH dla KDE.

%description kdessh -l pt_BR
Ferramenta de execução remota de programas.

%package kdf
Summary:	KDE Disk space GUI
Summary(pl):	df dla KDE
Summary(pt_BR):	Mostra o status de espaço em disco
Group:		X11/Applications
Requires:	kdebase-infocenter >= 9:%{version}
Obsoletes:	kdf

%description kdf
This program shows the disk usage of the mounted devices.

%description kdf -l pl
Ten program pokazuje zajêto¶æ dysku dla zamontowanych urz±dzeñ.

%description kdf -l pt_BR
Mostra o status de espaço em disco.

%package kedit
Summary:	KDE Text Editor
Summary(pl):	Edytor tekstu dla KDE
Summary(pt_BR):	Editor de texto melhorado do KDE
Group:		X11/Applications/Editors
Requires:	kdebase-core >= 9:%{version}
Obsoletes:	kedit

%description kedit
Simple text editor for KDE.

%description kedit -l pl
Prosty edytor tekstu dla KDE.

%description kedit -l pt_BR
Editor de texto melhorado do KDE.

%package kfloppy
Summary:	KDE Floppy Formater
Summary(pl):	Program formatuj±cy dyskietki dla KDE
Summary(pt_BR):	Ferramenta de formatação de disquetes
Group:		X11/Applications
Requires:	kdebase-core >= 9:%{version}
Requires:	dosfstools
Obsoletes:	kfloppy

%description kfloppy
KFloppy formats disks and puts a DOS or ext2fs filesystem on them.

%description kfloppy -l pl
KFloppy formatuje dyskietki i zak³ada na nich system plików DOS lub
ext2.

%description kfloppy -l pt_BR
Ferramenta de formatação de disquetes.

%package kgpg
Summary:	A frontend for gpg
Summary(pl):	Nak³adka graficzna na gpg
Group:		X11/Applications
Requires:	kdebase-core >= 9:%{version}
Obsoletes:	kgpg

%description kgpg
kgpg is a simple, free, open source KDE frontend for gpg.

%description kgpg -l pl
kgpg jest prost± graficzn± nak³adk± na gpg przeznaczon± dla KDE.

%package khexedit
Summary:	KDE Hex Editor
Summary(pl):	Edytor szesnastkowy dla KDE
Summary(pt_BR):	Editor hexadecimal para arquivos binários
Group:		X11/Applications/Editors
Requires:	kdebase-core >= 9:%{version}
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
Requires:	kdebase-core >= 9:%{version}
Obsoletes:	kjots

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
Requires:	kdebase-infocenter >= 9:%{version}
Obsoletes:	laptop

%description klaptopdaemon
KDE Laptop Daemon.

%description klaptopdaemon -l pl
Wska¼nik zu¿ycia baterii w laptopie dla KDE.

%description klaptopdaemon -l pt_BR
Miniaplicativo de status de bateria para laptops

%package kmilo
Summary:	KDE support for various types of hardware input devices
Summary(pl):	Wsparcie KDE dla ró¿nych rodzajów sprzêtowych urz±dzeñ wej¶ciowych
Group:		X11/Applications
Requires:	kdelibs >= 9:%{version}

%description kmilo
This is a kded module that can be extended to support various types of
hardware input devices that exist, such as those on keyboards.
It presently supports:
- PowerBooks
- Sony Vaio laptops (tested on Vaio PCG-GRX series)

%description kmilo -l pl
To jest modu³ kded, który mo¿e byæ rozszerzany, by obs³ugiwaæ ró¿ne
rodzaje sprzêtowych urz±dzeñ wej¶ciowych, takich jak te na
klawiaturze. Aktualnie obs³uguje:
- PowerBooki
- laptopy Sony Vaio (testowany na Vaio z serii PCG-GRX)

%package kmilo-kvaio
Summary:	Sony Vaio KMilo module
Summary(pl):	Modu³ KMilo dla laptopów Sony Vaio
Group:		X11/Applications
Requires:	kdebase-core >= 9:%{version}
Requires:	%{name}-kmilo = %{epoch}:%{version}-%{release}
Obsoletes:	kdeutils-kmilo < 9:3.1.2.031022

%description kmilo-kvaio
KMilo module for Sony Vaio laptop support.

%description kmilo-kvaio -l pl
Modu³ KMilo dla laptopów Sony Vaio.

%package kmilo-powerbook
Summary:	PowerBook KMilo module
Summary(pl):	Modu³ KMilo dla PowerBooków
Group:		X11/Applications
Requires:	kdebase-core >= 9:%{version}
Requires:	%{name}-kmilo = %{epoch}:%{version}-%{release}
Obsoletes:	kdeutils-kmilo < 9:3.1.2.031022

%description kmilo-powerbook
KMilo module for PowerBooks support.

%description kmilo-powerbook -l pl
Modu³ KMilo dla PowerBooków.

%package kregexpeditor
Summary:	Graphical regular expression editor
Summary(pl):	Graficzny edytor wyra¿eñ regularnych
Group:		X11/Applications
Requires:	kdebase-core >= 9:%{version}
Obsoletes:	kregexpeditor

%description kregexpeditor
Graphical regular expression editor.

%description kregexpeditor -l pl
Graficzny edytor wyra¿eñ regularnych.

%package ksim
Summary:	K System Information Monitor
Summary(pl):	K System Information Monitor - monitor informacji o systemie
Group:		X11/Applications
Requires:	kdebase-kicker >= 9:%{version}

%description ksim
System Monitor.

%description ksim -l pl
Monitor systemu.

%package ktimer
Summary:	KDE Timer
Summary(pl):	Zegarek KDE
Summary(pt_BR):	Monitor de tempo em forma de mini-aplicativo
Group:		X11/Applications
Requires:	kdelibs >= 9:%{version}
Obsoletes:	ktimer

%description ktimer
Time tracker applet.

%description ktimer -l pl
Zegarek.

%description ktimer -l pt_BR
Monitor de tempo em forma de mini-aplicativo.

%package kwalletmanager
Summary:	Wallet management tool for KDE
Summary(pl):	Narzêdzie do zarz±dzania portfelem dla KDE
Group:		X11/Applications
Requires:	kdebase-core >= 9:%{version}

%description kwalletmanager
Wallet management tool for KDE.

%description kwalletmanager -l pl
Narzêdzie do zarz±dzania portfelem dla KDE.

%package userinfo
Summary:	User Account
Summary(pl):	Konto u¿ytkownika
Group:		X11/Applications
Requires:	kdm >= 9:%{version}

%description userinfo
userinfo changes user account information. This module contains
kdepasswd program functionality.

%description userinfo -l pl
userinfo zmienia informacje o koncie u¿ytkownika. Ten modu³ zawiera
funkcjonalno¶æ programu kdepasswd.

%package i18n
Summary:	Common internationalization and localization files for kdeutils
Summary(pl):	Wspó³dzielone pliki umiêdzynarodawiaj±ce dla kdeutils
Group:		X11/Applications
Requires:	kdelibs-i18n >= 9:%{version}

%description i18n
Internationalization and localization files for kdeutils.

%description i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kdeutils.

%package ark-i18n
Summary:	Internationalization and localization files for ark
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla arka
Group:		X11/Applications
Requires:	%{name}-ark = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-core-i18n >= 9:%{version}

%description ark-i18n
Internationalization and localization files for ark.

%description ark-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla arka.

%package kcalc-i18n
Summary:	Internationalization and localization files for kcalc
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kcalca
Group:		X11/Applications
Requires:	%{name}-kcalc = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-core-i18n >= 9:%{version}

%description kcalc-i18n
Internationalization and localization files for kcalc.

%description kcalc-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kcalca.

%package kcharselect-i18n
Summary:	Internationalization and localization files for kcharselect
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kcharselecta
Group:		X11/Applications
Requires:	%{name}-kcharselect = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-core-i18n >= 9:%{version}

%description kcharselect-i18n
Internationalization and localization files for kcharselect.

%description kcharselect-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kcharselecta.

%package kdf-i18n
Summary:	Internationalization and localization files for kdf
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kdf
Group:		X11/Applications
Requires:	%{name}-kdf = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-infocenter-i18n >= 9:%{version}

%description kdf-i18n
Internationalization and localization files for kdf.

%description kdf-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kdf.

%package kedit-i18n
Summary:	Internationalization and localization files for kedit
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kedita
Group:		X11/Applications
Requires:	%{name}-kedit = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-core-i18n >= 9:%{version}

%description kedit-i18n
Internationalization and localization files for kedit.

%description kedit-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kedita.

%package kfloppy-i18n
Summary:	Internationalization and localization files for kfloppy
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kfloppy
Group:		X11/Applications
Requires:	%{name}-kfloppy = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-core-i18n >= 9:%{version}

%description kfloppy-i18n
Internationalization and localization files for kfloppy.

%description kfloppy-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kfloppy.

%package kgpg-i18n
Summary:	Internationalization and localization files for kgpg
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kgpg
Group:		X11/Applications
Requires:	%{name}-kgpg = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-core-i18n >= 9:%{version}

%description kgpg-i18n
Internationalization and localization files for kgpg.

%description kgpg-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kgpg.

%package khexedit-i18n
Summary:	Internationalization and localization files for khexedit
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla khexedita
Group:		X11/Applications
Requires:	%{name}-khexedit = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-core-i18n >= 9:%{version}

%description khexedit-i18n
Internationalization and localization files for khexedit.

%description khexedit-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla khexedita.

%package kjots-i18n
Summary:	Internationalization and localization files for kjots
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kjots
Group:		X11/Applications
Requires:	%{name}-kjots = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-core-i18n >= 9:%{version}

%description kjots-i18n
Internationalization and localization files for kjots.

%description kjots-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kjots.

%package klaptopdaemon-i18n
Summary:	Internationalization and localization files for klaptopdaemon
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla klaptopdaemona
Group:		X11/Applications
Requires:	%{name}-klaptopdaemon = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-infocenter-i18n >= 9:%{version}

%description klaptopdaemon-i18n
Internationalization and localization files for klaptopdaemon.

%description klaptopdaemon-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla klaptopdaemona.

%package kregexpeditor-i18n
Summary:	Internationalization and localization files for kregexpeditor
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kregexpeditora
Group:		X11/Applications
Requires:	%{name}-kregexpeditor = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-core-i18n >= 9:%{version}

%description kregexpeditor-i18n
Internationalization and localization files for kregexpeditor.

%description kregexpeditor-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kregexpeditora.

%package ksim-i18n
Summary:	Internationalization and localization files for ksim
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla ksima
Group:		X11/Applications
Requires:	%{name}-ksim = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-kicker-i18n >= 9:%{version}

%description ksim-i18n
Internationalization and localization files for ksim.

%description ksim-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla ksima.

%package ktimer-i18n
Summary:	Internationalization and localization files for ktimer
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla ktimera
Group:		X11/Applications
Requires:	%{name}-ktimer = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}

%description ktimer-i18n
Internationalization and localization files for ktimer.

%description ktimer-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla ktimera.

%package kwalletmanager-i18n
Summary:	Internationalization and localization files for kwalletmanager
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kwalletmanagera
Group:		X11/Applications
Requires:	%{name}-kwalletmanager = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-core-i18n >= 9:%{version}

%description kwalletmanager-i18n
Internationalization and localization files for kwalletmanager.

%description kwalletmanager-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kwalletmanagera.

%package kdelirc-i18n
Summary:	Internationalization and localization files for kdelirc
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kdelirca
Group:		X11/Applications
Requires:	%{name}-kdelirc = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-core-i18n >= 9:%{version}

%description kdelirc-i18n
Internationalization and localization files for kdelirc.

%description kdelirc-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kdelirca.

%package userinfo-i18n
Summary:	Internationalization and localization files for userinfo
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla userinfo
Group:		X11/Applications
Requires:       %{name}-userinfo = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	kdm-i18n >= 9:%{version}

%description userinfo-i18n
Internationalization and localization files for userinfo.

%description userinfo-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla userinfo.

%package kdessh-i18n
Summary:	Internationalization and localization files for kdessh
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kdessh
Group:		X11/Applications
Requires:       %{name}-kdessh = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}

%description kdessh-i18n
Internationalization and localization files for kdessh.

%description kdessh-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kdessh.

%package kdepasswd-i18n
Summary:	Internationalization and localization files for kdepasswd
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kdepasswd
Group:		X11/Applications
Requires:       %{name}-kdepasswd = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}

%description kdepasswd-i18n
Internationalization and localization files for kdepasswd.

%description kdepasswd-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kdepasswd.

%prep
%setup -q 
%patch0 -p1
%patch1 -p1
#%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
cp /usr/share/automake/config.sub admin
%{__make} -f admin/Makefile.common cvs

%configure \
	--with-qt-libraries=%{_libdir} \
	--disable-rpath \
	--enable-final

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

mv $RPM_BUILD_ROOT%{_desktopdir}/kde/kwallet{config,}.desktop

%if %{with i18n}
if [ -f "%{SOURCE1}" ] ; then
	bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT
	for f in $RPM_BUILD_ROOT%{_datadir}/locale/*/LC_MESSAGES/*.mo; do
		if [ "`file $f | sed -e 's/.*,//' -e 's/message.*//'`" -le 1 ] ; then
			rm -f $f
		fi
	done
else
	echo "No i18n sources found and building --with i18n. FIXIT!"
	exit 1
fi
%endif

%find_lang ark			--with-kde
%find_lang KRegExpEditor	--with-kde
%find_lang kcalc		--with-kde
%find_lang kcharselect		--with-kde
> kdf.lang
%find_lang kdf			--with-kde
%find_lang blockdevices		--with-kde
cat blockdevices.lang >> kdf.lang
%find_lang kedit		--with-kde
%find_lang kfloppy		--with-kde
%find_lang kgpg			--with-kde
%find_lang khexedit		--with-kde
%find_lang kjots		--with-kde
%if %{with i18n}
%find_lang klaptopdaemon        --with-kde
%else
> klaptopdaemon.lang
%endif
%find_lang kcmlowbatcrit	--with-kde
%find_lang kcmlowbatwarn	--with-kde
%find_lang laptop		--with-kde
%find_lang powerctrl		--with-kde
cat {kcmlowbatcrit,kcmlowbatwarn,laptop,powerctrl}.lang >> klaptopdaemon.lang
%find_lang ksim			--with-kde
%find_lang ktimer		--with-kde
%find_lang kwallet		--with-kde

%if %{with i18n}
%find_lang kdelirc              --with-kde
%find_lang irkick	        --with-kde
%find_lang kcmlirc              --with-kde
cat irkick.lang >> kdelirc.lang
cat kcmlirc.lang >> kdelirc.lang

%find_lang kwalletmanager	--with-kde
cat kwalletmanager.lang >> kwallet.lang
%find_lang kcmkwallet		--with-kde
cat kcmkwallet.lang >> kwallet.lang

%find_lang kcmlaptop		--with-kde
cat kcmlaptop.lang >> klaptopdaemon.lang
%find_lang kcmkvaio		--with-kde
cat kcmkvaio.lang >> klaptopdaemon.lang

%find_lang kregexpeditor	--with-kde
cat kregexpeditor.lang >> KRegExpEditor.lang

%find_lang kcharselectapplet	--with-kde
cat kcharselectapplet.lang >> kcharselect.lang

%find_lang userinfo		--with-kde
%find_lang desktop_kdeutils	--with-kde
%find_lang kdessh		--with-kde
%find_lang kdepasswd            --with-kde
# We dont buidl kcardchooser (disabled by default by coolo) 
# renaableing it would be posssible, but what for?
# %find_lang kcardchooser            --with-kde
%endif

files="ark \
kcalc \
kcharselect \
kdf \
kedit \
kfloppy \
kgpg \
khexedit \
kjots \
klaptopdaemon \
KRegExpEditor \
ksim \
ktimer \
kwallet"

for i in $files; do
	> ${i}_en.lang
        echo "%defattr(644,root,root,755)" > ${i}_en.lang
	grep en\/ ${i}.lang|grep -v apidocs >> ${i}_en.lang
	grep -v apidocs $i.lang|grep -v en\/ > ${i}.lang.1
	mv ${i}.lang.1 ${i}.lang
done

durne=`ls -1 *.lang|grep -v _en`

for i in $durne; 
do
	echo $i >> control
	grep -v en\/ $i|grep -v apidocs >> ${i}.1
	if [ -f ${i}.1 ] ; then
		mv ${i}.1 ${i}
	fi
done

%clean
rm -rf $RPM_BUILD_ROOT

%post	klaptopdaemon	-p /sbin/ldconfig
%postun	klaptopdaemon	-p /sbin/ldconfig

%post	kmilo		-p /sbin/ldconfig
%postun	kmilo		-p /sbin/ldconfig

%post	kregexpeditor	-p /sbin/ldconfig
%postun	kregexpeditor	-p /sbin/ldconfig

%post	ksim		-p /sbin/ldconfig
%postun	ksim		-p /sbin/ldconfig

%if %{with i18n}
%files i18n -f desktop_kdeutils.lang
%files ark-i18n -f ark.lang
%files kcalc-i18n -f kcalc.lang
%files kcharselect-i18n -f kcharselect.lang
%files kdf-i18n -f kdf.lang
%files kedit-i18n -f kedit.lang
%files kfloppy-i18n -f kfloppy.lang
%files kgpg-i18n -f kgpg.lang
%files khexedit-i18n -f khexedit.lang
%files kjots-i18n -f kjots.lang
%files klaptopdaemon-i18n -f klaptopdaemon.lang
%files kregexpeditor-i18n -f KRegExpEditor.lang
%files ksim-i18n -f ksim.lang
%files ktimer-i18n -f ktimer.lang
%files kwalletmanager-i18n -f kwallet.lang
%files kdelirc-i18n -f kdelirc.lang
%files userinfo-i18n -f userinfo.lang
%files kdessh-i18n -f kdessh.lang
%files kdepasswd-i18n -f kdepasswd.lang
%endif

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkcmlaptop.so
%attr(755,root,root) %{_libdir}/libkmilo.so
%attr(755,root,root) %{_libdir}/libkregexpeditorcommon.so
%attr(755,root,root) %{_libdir}/libksimcore.so
%{_includedir}/*

%files ark -f ark_en.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ark
%{_libdir}/libkdeinit_ark.la
%attr(755,root,root) %{_libdir}/libkdeinit_ark.so
%{_libdir}/kde3/ark.la
%attr(755,root,root) %{_libdir}/kde3/ark.so
%{_libdir}/kde3/libarkpart.la
%attr(755,root,root) %{_libdir}/kde3/libarkpart.so
%{_datadir}/apps/ark
%{_datadir}/apps/konqueror/servicemenus/ark_directory_service.desktop
%{_datadir}/apps/konqueror/servicemenus/arkservicemenu.desktop
%{_datadir}/services/ark_part.desktop
%{_desktopdir}/kde/ark.desktop
%{_iconsdir}/*/*/apps/ark.*

%files kcalc -f kcalc_en.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kcalc
%{_libdir}/libkdeinit_kcalc.la
%attr(755,root,root) %{_libdir}/libkdeinit_kcalc.so
%{_libdir}/kde3/kcalc.la
%attr(755,root,root) %{_libdir}/kde3/kcalc.so
%{_datadir}/apps/kcalc
%{_datadir}/apps/kconf_update/kcalcrc.upd
%{_datadir}/config.kcfg/kcalc.kcfg
%{_desktopdir}/kde/kcalc.desktop
%{_iconsdir}/*/*/apps/kcalc.*

%files kcharselect -f kcharselect_en.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kcharselect
%{_libdir}/kde3/kcharselect_panelapplet.la
%attr(755,root,root) %{_libdir}/kde3/kcharselect_panelapplet.so
%{_datadir}/apps/kicker/applets/kcharselectapplet.desktop
%{_desktopdir}/kde/KCharSelect.desktop
%{_iconsdir}/*/*/apps/kcharselect.*

%files kdelirc 
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/irkick
%{_libdir}/libkdeinit_irkick.la
%attr(755,root,root) %{_libdir}/libkdeinit_irkick.so
%{_libdir}/kde3/irkick.la
%attr(755,root,root) %{_libdir}/kde3/irkick.so
%{_libdir}/kde3/kcm_kcmlirc.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kcmlirc.so
%{_datadir}/apps/irkick
%{_datadir}/apps/profiles/klauncher.profile.xml
%{_datadir}/apps/profiles/konqueror.profile.xml
%{_datadir}/apps/profiles/noatun.profile.xml
%{_datadir}/apps/profiles/profile.dtd
%{_datadir}/apps/remotes/RM-0010.remote.xml
%{_datadir}/apps/remotes/cimr100.remote.xml
%{_datadir}/apps/remotes/hauppauge.remote.xml
%{_datadir}/apps/remotes/remote.dtd
%{_datadir}/apps/remotes/sherwood.remote.xml
%{_datadir}/autostart/irkick.desktop
%{_desktopdir}/kde/irkick.desktop
%{_desktopdir}/kde/kcmlirc.desktop
%{_iconsdir}/hicolor/*/apps/irkick.png

%files kdepasswd
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kdepasswd
%{_desktopdir}/kde/kdepasswd.desktop

%files kdessh
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kdessh

%files kdf -f kdf_en.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kdf
%attr(755,root,root) %{_bindir}/kwikdisk
%{_libdir}/kde3/kcm_kdf.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kdf.so
%{_datadir}/apps/kdf
%{_desktopdir}/kde/kcmdf.desktop
%{_desktopdir}/kde/kdf.desktop
%{_desktopdir}/kde/kwikdisk.desktop
%{_iconsdir}/*/*/apps/kcmdf.*
%{_iconsdir}/*/*/apps/kdf.*
%{_iconsdir}/*/*/apps/kwikdisk.*

%files kedit -f kedit_en.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kedit
%{_libdir}/libkdeinit_kedit.la
%attr(755,root,root) %{_libdir}/libkdeinit_kedit.so
%{_libdir}/kde3/kedit.la
%attr(755,root,root) %{_libdir}/kde3/kedit.so
%{_datadir}/apps/kedit
%{_datadir}/config.kcfg/kedit.kcfg
%{_desktopdir}/kde/KEdit.desktop
%{_iconsdir}/*/*/apps/kedit.*

%files kfloppy -f kfloppy_en.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kfloppy
%{_desktopdir}/kde/KFloppy.desktop
%{_iconsdir}/*/*/apps/kfloppy.*

%files kgpg -f kgpg_en.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kgpg
%{_datadir}/apps/kgpg
%{_datadir}/apps/konqueror/servicemenus/encryptfile.desktop
%{_datadir}/apps/konqueror/servicemenus/encryptfolder.desktop
%{_datadir}/autostart/kgpg.desktop
%{_datadir}/config.kcfg/kgpg.kcfg
%{_desktopdir}/kde/kgpg.desktop
%{_iconsdir}/*/*/apps/kgpg.png

%files khexedit -f khexedit_en.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/khexedit
%{_libdir}/kde3/libkbyteseditwidget.la
%attr(755,root,root) %{_libdir}/kde3/libkbyteseditwidget.so
%{_datadir}/apps/khexedit
%{_datadir}/services/kbyteseditwidget.desktop
%{_desktopdir}/kde/khexedit.desktop
%{_iconsdir}/*/*/apps/khexedit.*

%files kjots -f kjots_en.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kjots
%{_datadir}/apps/kjots
%{_datadir}/config.kcfg/kjots.kcfg
%{_desktopdir}/kde/Kjots.desktop
%{_iconsdir}/*/*/apps/kjots.*

%files kmilo
%defattr(644,root,root,755)
%{_libdir}/libkmilo.la
%attr(755,root,root) %{_libdir}/libkmilo.so.*.*.*
%{_libdir}/kde3/kded_kmilod.la
%attr(755,root,root) %{_libdir}/kde3/kded_kmilod.so
%{_libdir}/kde3/kmilo_generic.la
%attr(755,root,root) %{_libdir}/kde3/kmilo_generic.so
%{_datadir}/services/kded/kmilod.desktop
%dir %{_datadir}/services/kmilo
%{_datadir}/services/kmilo/kmilo_generic.desktop
%{_datadir}/servicetypes/kmilo

%files kmilo-kvaio
%defattr(644,root,root,755)
%{_libdir}/kde3/kcm_kvaio.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kvaio.so
%{_libdir}/kde3/kmilo_kvaio.la
%attr(755,root,root) %{_libdir}/kde3/kmilo_kvaio.so
%{_datadir}/services/kmilo/kmilo_kvaio.desktop
%{_desktopdir}/kde/kvaio.desktop

%ifarch ppc
%files kmilo-powerbook
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kmilo_powerbook.so
%{_libdir}/kde3/kmilo_powerbook.la
%{_datadir}/services/kmilo/kmilo_powerbook.desktop
%endif

%files klaptopdaemon -f klaptopdaemon_en.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/klaptop*
%{_libdir}/libkcmlaptop.la
%attr(755,root,root) %{_libdir}/libkcmlaptop.so.*.*.*
%{_libdir}/kde3/kded_klaptopdaemon.la
%attr(755,root,root) %{_libdir}/kde3/kded_klaptopdaemon.so
%{_libdir}/kde3/kcm_laptop.la
%attr(755,root,root) %{_libdir}/kde3/kcm_laptop.so
%{_datadir}/apps/klaptopdaemon
%{_datadir}/services/kded/klaptopdaemon.desktop
%{_desktopdir}/kde/laptop.desktop
%{_desktopdir}/kde/pcmcia.desktop
%{_iconsdir}/*/*/*/*laptop*

%files kregexpeditor -f KRegExpEditor_en.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kregexpeditor
%{_libdir}/libkregexpeditorcommon.la
%attr(755,root,root) %{_libdir}/libkregexpeditorcommon.so.*.*.*
%{_libdir}/kde3/libkregexpeditorgui.la
%attr(755,root,root) %{_libdir}/kde3/libkregexpeditorgui.so
%{_datadir}/apps/kregexpeditor
%{_datadir}/services/kregexpeditorgui.desktop
%{_desktopdir}/kde/kregexpeditor.desktop

%files ksim -f ksim_en.lang
%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/ksim
#%{_libdir}/ksim.la
#%attr(755,root,root) %{_libdir}/ksim.so
%{_libdir}/libksimcore.la
%attr(755,root,root) %{_libdir}/libksimcore.so.*.*.*
%{_libdir}/kde3/ksim*.la
%attr(755,root,root) %{_libdir}/kde3/ksim*.so
%{_datadir}/apps/kicker/extensions/ksim.desktop
%{_datadir}/apps/ksim
%{_datadir}/config/ksim_panelextensionrc
%{_desktopdir}/kde/ksim.desktop
%{_iconsdir}/*/*/apps/ksim*.png
%{_iconsdir}/*/*/devices/ksim*.png

%files ktimer -f ktimer_en.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ktimer
%{_desktopdir}/kde/ktimer.desktop
%{_iconsdir}/*/*/*/ktimer.png

%files kwalletmanager -f kwallet_en.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kwalletmanager
%{_libdir}/kde3/kcm_kwallet.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kwallet.so
%{_datadir}/apps/kwalletmanager
%{_datadir}/services/kwallet_config.desktop
%{_datadir}/services/kwalletmanager_show.desktop
%{_desktopdir}/kde/kwallet.desktop
%{_desktopdir}/kde/kwalletmanager.desktop
%{_iconsdir}/crystalsvg/*/apps/kwalletmanager.png

%files userinfo
%defattr(644,root,root,755)
%{_libdir}/kde3/kcm_userinfo.la
%attr(755,root,root) %{_libdir}/kde3/kcm_userinfo.so
%{_datadir}/apps/kdm/pics/users/*
%{_desktopdir}/kde/userinfo.desktop
