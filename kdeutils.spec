#
%define		_state		stable
%define		_ver		3.2.3

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
Release:	1
Epoch:		9
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{_ver}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	3a98f8a0a6f4582e03d4503708cb218a
#Source0:	http://ep09.pld-linux.org/~djurban/kde/%{name}-%{version}.tar.bz2
Icon:		kde-utils.xpm
#Patch100:		%{name}-branch.diff
Patch0:		%{name}-kdf-label.patch
Patch1:		%{name}-vcategories.patch
Patch2:		%{name}-userinfo.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bzip2
BuildRequires:	kdebase-devel >= 9:%{version}
BuildRequires:	libxml2-progs
BuildRequires:	libtool
%ifarch ppc
BuildRequires:	pbbuttonsd-lib >= 0.5.6-2
%endif
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	unsermake
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
 - KCharSelect - narzêdzie do wybierania znaków,
 - KDEPasswd,
 - KDESsh - narzêdzie do zdalnego wykonywania programów,
 - Kdf - graficzny interfejs do sprawdzania miejsca na dysku,
 - KEdit - edytor tekstu,
 - KFind - frontend do wyszukiwania plików,
 - KFloppy - narzêdzie do formatowania dyskietek,
 - KHexedit - szesnastkowy edytor plików,
 - KJots - notatnik,
 - KLaptopDaemon - demon dla laptopów,
 - KLipper - przegl±darka schowka,
 - KLJetTool - narzêdzie dla u¿ytkowników drukarek LaserJet,
 - KLpq - zarz±dca wydruków,
 - KLprFax - frontend faksowy dla LPD u¿ywaj±cy efax,
 - KNotes - inny notatnik,
 - KPm - program do zarz±dzania procesami,
 - KTimer - timer,
 - KTop - zarz±dca zadañ,
 - KTreeBrowser,
 - ksim - monitor systemu.

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
Ark is a program for managing and quickly extracting archives. It
supports arj, rar, zip, tar, zoo, lha and other formats.

%description ark -l pl
Ark jest programem s³u¿±cym do zarz±dzania i szybkiego rozpakowywania
archiwów. Obs³uguje archiwa arj, rar, zip, tar, zoo, lha oraz inne
formaty.

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
Application for selecting characters.

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
  aplikacji do przycisków pilota oraz konfiguracji samych pilotów (czyli
  konfiguracji lirc)
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
Application that allows changing your password.

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
A KDE SSH frontend.

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
KFloppy formats floppy disks and puts a DOS or ext2fs filesystem on
them.

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
kgpg is a simple, free, open source KDE frontend for gpg. It features
- editor mode enables you to type/paste a text and
  encrypt/decrypt/sign/verify it
- key manager: import, export, delete, sign, generate and edit keys.
- integration with konqueror: left click on a file to decrypt/verify
  it, right click on a file to encrypt/sign it.
- encryption: support for symetric encryption. Multiple keys & default
  key encryption. Optional shredding of source files
- signatures: creation & verification of detached & cleartext
  signatures
- drag & drop encryption + clipboard en/decryption

%description kgpg -l pl
kgpg jest prost±, darmow±, z otwartymi ¼ród³ami, graficzn± nak³adk± na
gpg przeznaczon± dla KDE. Ma nastêpuj±ce mo¿liwo¶ci:
- tryb edytora umo¿liwiaj±cy napisanie/wklejenie tekstu oraz
  zaszyfrowanie/odszyfrowanie/podpisanie/sprawdzenie go,
- zarz±dzanie kluczami: import, eksport, usuwanie, podpisywanie,
  generowanie oraz edycjê,
- integracjê z Konquerorem: klikniêcie lewym przyciskiem na pliku w
  celu odszyfrowania/sprawdzenia go, klikniêcie prawym przyciskiem na
  pliku w celu zaszyfrowania/podpisania go,
- szyfrowanie: obs³uga szyfrów symetrycznych; wiele kluczy i domy¶lne
  szyfrowanie kluczem; opcjonalnie niszczenie plików ¼ród³owych,
- sygnatury: tworzenie i sprawdzanie oddzielonych i czysto tekstowych
  sygnatur,
- szyfrowanie metod± przeci±gnij-i-upu¶æ oraz szyfrowanie i
  odszyfrowywanie schowka.

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
A laptop battery monitoring tool for KDE

%description klaptopdaemon -l pl
Wska¼nik zu¿ycia baterii w laptopie dla KDE.

%description klaptopdaemon -l pt_BR
Miniaplicativo de status de bateria para laptops

%package kmilo
Summary:	KDE support for various types of hardware input devices
Summary(pl):	Wsparcie KDE dla ró¿nych rodzajów sprzêtowych urz±dzeñ wej¶ciowych
Group:		X11/Applications
Requires:	kdelibs >= 9:%{version}
Obsoletes:	kdeutils-kmilo-kvaio
Obsoletes:	kdeutils-kmilo-powerbook

%description kmilo
This is a kded module that can be extended to support various types of
hardware input devices that exist, such as those on keyboards. It
presently supports:
- PowerBooks
- Sony Vaio laptops (tested on Vaio PCG-GRX series)

%description kmilo -l pl
To jest modu³ kded, który mo¿e byæ rozszerzany, by obs³ugiwaæ ró¿ne
rodzaje sprzêtowych urz±dzeñ wej¶ciowych, takich jak te na
klawiaturze. Aktualnie obs³uguje:
- PowerBooki
- laptopy Sony Vaio (testowany na Vaio z serii PCG-GRX)

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
Requires:	kdebase-desktop >= 9:%{version}

%description ksim
A KDE system monitoring tool that features:
- GKrellm theme support
- host name display
- uptime, memory and swap display
- filesystem usage plugin
- disk information plugin
- net plugin being able to monitor eth0, ppp0 and others
- sensor plugin able to monitor any sensor via lm_sensors
- APM laptop battery meter
- CPU plugin that can monitor CPU usage.


%description ksim -l pl
Narzêdzie do monitorowania systemu dla KDE o nastêpuj±cych
mo¿liwo¶ciach:
- obs³uga motywów GKrellma
- wy¶wietlanie nazwy komputera
- wy¶wietlanie uptime'u, stanu pamiêci i swapa
- wtyczka wykorzystania systemu plików
- wtyczka informacji o dysku
- wtyczka sieciowa potrafi±ca monitorowaæ eth0, ppp0 i inne
- wtyczka czujników potrafi±ca monitorowaæ dowolne czujniki przez
  lm_sensors
- miernik baterii laptopów korzystaj±cy z APM
- wtyczka procesora monitoruj±ca obci±¿enie procesora.

%package ktimer
Summary:	KDE Timer
Summary(pl):	Timer dla KDE
Summary(pt_BR):	Monitor de tempo em forma de mini-aplicativo
Group:		X11/Applications
Requires:	kdelibs >= 9:%{version}
Obsoletes:	ktimer

%description ktimer
This is a timer application for KDE. It allows you to execute commands
after a certain amount of time. It allows looping commands as well as
delaying the execution of a command.

%description ktimer -l pl
To jest aplikacja timera dla KDE. Umo¿liwia wykonywanie poleceñ po
okre¶lonym czasie, zapêtlanie poleceñ, a tak¿e opó¼nienie wykonywania
poleceñ.

%description ktimer -l pt_BR
Monitor de tempo em forma de mini-aplicativo.

%package kwalletmanager
Summary:	Password management tool for KDE
Summary(pl):	Narzêdzie do zarz±dzania has³ami dla KDE
Group:		X11/Applications
Requires:	kdebase-core >= 9:%{version}

%description kwalletmanager
Password management tool for KDE.

%description kwalletmanager -l pl
Narzêdzie do zarz±dzania has³ami w KDE.

%package userinfo
Summary:	User account information editor
Summary(pl):	Edytor informacji o koncie u¿ytkownika
Group:		X11/Applications
Requires:	kdm >= 9:%{version}

%description userinfo
A tool for changing information for a system account also supports
changing the password.

%description userinfo -l pl
userinfo zmienia informacje o koncie u¿ytkownika. Ten modu³ zawiera
funkcjonalno¶æ programu kdepasswd.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

echo "KDE_OPTIONS=nofinal" >> ksim/monitors/snmp/Makefile.am

%build
cp %{_datadir}/automake/config.sub admin
export kde_htmldir=%{_kdedocdir}
export kde_libs_htmldir=%{_kdedocdir}
export UNSERMAKE=%{_datadir}/unsermake/unsermake
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
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir}

mv $RPM_BUILD_ROOT%{_desktopdir}/kde/kwallet{config,}.desktop

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

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkcmlaptop.so
%attr(755,root,root) %{_libdir}/libkmilo.so
%attr(755,root,root) %{_libdir}/libkregexpeditorcommon.so
%attr(755,root,root) %{_libdir}/libksimcore.so
%{_includedir}/*

%files ark
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
%{_kdedocdir}/en/ark

%files kcalc
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
%{_kdedocdir}/en/kcalc

%files kcharselect
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kcharselect
%{_libdir}/kde3/kcharselect_panelapplet.la
%attr(755,root,root) %{_libdir}/kde3/kcharselect_panelapplet.so
%{_datadir}/apps/kicker/applets/kcharselectapplet.desktop
%{_desktopdir}/kde/KCharSelect.desktop
%{_iconsdir}/*/*/apps/kcharselect.*
%{_kdedocdir}/en/kcharselect

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
%{_kdedocdir}/en/irkick
%{_kdedocdir}/en/kcmlirc

%files kdepasswd
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kdepasswd
%{_desktopdir}/kde/kdepasswd.desktop

%files kdessh
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kdessh

%files kdf
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
%{_kdedocdir}/en/kdf
%{_kdedocdir}/en/kinfocenter/blockdevices

%files kedit
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
%{_kdedocdir}/en/kedit

%files kfloppy
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kfloppy
%{_desktopdir}/kde/KFloppy.desktop
%{_iconsdir}/*/*/apps/kfloppy.*
%{_kdedocdir}/en/kfloppy

%files kgpg
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kgpg
%{_datadir}/apps/kgpg
%{_datadir}/apps/konqueror/servicemenus/encryptfile.desktop
%{_datadir}/apps/konqueror/servicemenus/encryptfolder.desktop
%{_datadir}/autostart/kgpg.desktop
%{_datadir}/config.kcfg/kgpg.kcfg
%{_desktopdir}/kde/kgpg.desktop
%{_iconsdir}/*/*/apps/kgpg.png
%{_kdedocdir}/en/kgpg

%files khexedit
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/khexedit
%{_libdir}/kde3/libkbyteseditwidget.la
%attr(755,root,root) %{_libdir}/kde3/libkbyteseditwidget.so
%{_datadir}/apps/khexedit
%{_datadir}/services/kbyteseditwidget.desktop
%{_desktopdir}/kde/khexedit.desktop
%{_iconsdir}/*/*/apps/khexedit.*
%{_kdedocdir}/en/khexedit

%files kjots
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kjots
%{_datadir}/apps/kjots
%{_datadir}/config.kcfg/kjots.kcfg
%{_desktopdir}/kde/Kjots.desktop
%{_iconsdir}/*/*/apps/kjots.*
%{_kdedocdir}/en/kjots

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
%{_libdir}/kde3/kcm_kvaio.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kvaio.so
%{_libdir}/kde3/kmilo_kvaio.la
%attr(755,root,root) %{_libdir}/kde3/kmilo_kvaio.so
%{_datadir}/services/kmilo/kmilo_kvaio.desktop
%{_desktopdir}/kde/kvaio.desktop
%ifarch ppc
%attr(755,root,root) %{_libdir}/kde3/kmilo_powerbook.so
%{_libdir}/kde3/kmilo_powerbook.la
%{_datadir}/services/kmilo/kmilo_powerbook.desktop
%endif

%files klaptopdaemon
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
%{_kdedocdir}/en/kcontrol/kcmlowbat*
%{_kdedocdir}/en/kcontrol/laptop
%{_kdedocdir}/en/kcontrol/powerctrl

%files kregexpeditor
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kregexpeditor
%{_libdir}/libkregexpeditorcommon.la
%attr(755,root,root) %{_libdir}/libkregexpeditorcommon.so.*.*.*
%{_libdir}/kde3/libkregexpeditorgui.la
%attr(755,root,root) %{_libdir}/kde3/libkregexpeditorgui.so
%{_datadir}/apps/kregexpeditor
%{_datadir}/services/kregexpeditorgui.desktop
%{_desktopdir}/kde/kregexpeditor.desktop
%{_kdedocdir}/en/KRegExpEditor

%files ksim
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
%{_kdedocdir}/en/ksim

%files ktimer
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ktimer
%{_desktopdir}/kde/ktimer.desktop
%{_iconsdir}/*/*/*/ktimer.png
%{_kdedocdir}/en/ktimer

%files kwalletmanager
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
%{_kdedocdir}/en/kwallet

%files userinfo
%defattr(644,root,root,755)
%{_libdir}/kde3/kcm_userinfo.la
%attr(755,root,root) %{_libdir}/kde3/kcm_userinfo.so
%{_datadir}/apps/kdm/pics/users/*
%{_desktopdir}/kde/userinfo.desktop
