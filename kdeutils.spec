
%define		_state		stable
%define		_ver		3.4.0

%define		_minlibsevr	9:3.4.0
%define		_minbaseevr	9:3.4.0

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
Release:	0.1
Epoch:		9
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{_ver}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	cb7e5402eedaca816e210d460e22e53a
#Patch0:		%{name}-kdf-label.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bzip2
BuildRequires:	ed
BuildRequires:	kdebase-devel >= %{_minbaseevr}
BuildRequires:	libxml2-progs
BuildRequires:	libtool
%ifarch ppc
BuildRequires:	pbbuttonsd-lib >= 0.5.6-2
%endif
BuildRequires:	rpmbuild(macros) >= 1.129
#BuildRequires:	unsermake >= 040511
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KDE utilities. Package includes:
 - Ark - archive manager,
 - KCalc - calculator KCharSelect,
 - KCharSelect - character Selector,
 - KDEPasswd, password change application
 - KDESsh - SSH frontend,
 - Kdf - disk space GUI,
 - KEdit - text editor,
 - KFloppy - floppy formating tool,
 - KHexEdit - HEX file editor,
 - KJots - note taker,
 - KLaptopDaemon - laptop daemon,
 - KTimer - timer,
 - KTop - task manager,
 - ksim - system monitor.

%description -l es
Utilitarios para KDE. Programas disponibles en este paquete:
 - Ark,
 - KCalc - calculadora científica,
 - KCharSelect,
 - KDESsh,
 - Kdf -
 - KEdit - editor de textos sencillo,
 - KFloppy - herramienta de formatear disquetes,
 - KHexEdit - editor hexadecimal,
 - KJots - bloque de notas,
 - KLaptopDaemon,
 - KTimer.
 - ksim

%description -l ja
KDE¥Ç¥¹¥¯¥È¥Ã¥×´Ä¶­ÍÑ¤Î¥æ¡¼¥Æ¥£¥ê¥Æ¥£
°Ê²¼¤Î¤è¤¦¤Ê¥Ñ¥Ã¥±¡¼¥¸¤¬Æþ¤Ã¤Æ¤¤¤Þ¤¹¡£

- ark - ¥¢¡¼¥«¥¤¥ÖÁàºî¥Ä¡¼¥ë
- kcalc - ÅÅÂî
- kedit - ¥Æ¥­¥¹¥È¥¨¥Ç¥£¥¿
- kfloppy - ¥Õ¥í¥Ã¥Ô¡¼¥Õ¥©¡¼¥Þ¥Ã¥¿
- khexedit - ¥Ð¥¤¥Ê¥ê¥¨¥Ç¥£¥¿
- kjots - note taker

%description -l pl
Narzêdzia dla KDE. Pakiet zawiera:
 - Ark - program do zarz±dzania archiwami,
 - KCalc - kalkulator,
 - KCharSelect - narzêdzie do wybierania znaków,
 - KDEPasswd,
 - KDESsh - narzêdzie do zdalnego wykonywania programów,
 - Kdf - graficzny interfejs do sprawdzania miejsca na dysku,
 - KEdit - edytor tekstu,
 - KFloppy - narzêdzie do formatowania dyskietek,
 - KHexedit - szesnastkowy edytor plików,
 - KJots - notatnik,
 - KLaptopDaemon - demon dla laptopów,
 - KTimer - timer,
 - KTop - zarz±dca zadañ,
 - ksim - monitor systemu.

%description -l pt_BR
Utilitários para o KDE. Programas disponíveis neste pacote:
 - Ark - controle de tempo pessoal,
 - KCalc - calculadora científica,
 - KCharSelect,
 - KDESsh - ferramenta de execução remota de programas,
 - KEdit - editor de textos simples
 - KFloppy - ferramenta de formatação de disquetes,
 - KHexEdit - editor hexadecimal,
 - KJots - bloco de notas,
 - KLaptopDaemon - miniaplicativo de status de bateria para laptops,
 - KTimer - Monitor de tempo em forma de mini-aplicativo.

%description -l ru
õÔÉÌÉÔÙ ÄÌÑ K Desktop Environment. ÷ËÌÀÞÁÅÔ:
 - ark - ÍÅÎÅÄÖÅÒ ÁÒÈÉ×Ï× tar/gzip,
 - kcalc - ÎÁÕÞÎÙÊ ËÁÌØËÕÌÑÔÏÒ,
 - kedit - ÐÒÏÓÔÏÊ ÔÅËÓÔÏ×ÙÊ ÒÅÄÁËÔÏÒ,
 - kfloppy - ÕÔÉÌÉÔÁ ÄÌÑ ÆÏÒÍÁÔÉÒÏ×ÁÎÉÑ ÆÌÏÐÐÉ-ÄÉÓËÏ×,
 - khexedit - ÒÅÄÁËÔÏÒ ÂÉÎÁÒÎÙÈ ÆÁÊÌÏ×,
 - kjots - ÂÌÏËÎÏÔ,

%description -l uk
õÔÉÌÉÔÙ ÄÌÑ K Desktop Environment. í¦ÓÔÉÔØ:
 - ark - ÍÅÎÅÄÖÅÒ ÁÒÈ¦×¦× tar/gzip,
 - kcalc - ÎÁÕÞÎÉÊ ËÁÌØËÕÌÑÔÏÒ,
 - kedit - ÐÒÏÓÔÉÊ ÔÅËÓÔÏ×ÉÊ ÒÅÄÁËÔÏÒ,
 - kfloppy - ÕÔÉÌ¦ÔÁ ÄÌÑ ÆÏÒÍÁÔÕ×ÁÎÎÑ ÆÌÏÐ¦-ÄÉÓË¦×,
 - khexedit - ÒÅÄÁËÔÏÒ Â¦ÎÁÒÎÉÈ ÆÁÊÌ¦×,
 - kjots - ÎÏÔÁÔÎÉË,

%package devel
Summary:	Header files for compiling applications that use kdeutils libraries
Summary(pl):	Pliki nag³ówkowe do kompilacji aplikacji u¿ywaj±cych bibliotek kdeutils
Summary(pt_BR):	Arquivos de inclusão para as bibliotecas do kdeutils
Group:		X11/Development/Libraries
Requires:	kdebase-devel >= %{_minbaseevr}
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
Requires:	kdebase-core >= %{_minbaseevr}

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
Requires:	kdebase-core >= %{_minbaseevr}
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
Requires:	kdebase-core >= %{_minbaseevr}
Obsoletes:	kcharselect

%description kcharselect
Application for selecting characters.

%description kcharselect -l pl
Program do wybierania znaków.

%package kdelirc
Summary:	KDE frontend for the Linux Infrared Remote Control system
Summary(pl):	Frontend KDE dla systemu LIRC (zdalnego sterowania podczerwieni±)
Group:		X11/Applications
Requires:	kdebase-core >= %{_minbaseevr}

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

%package kdessh
Summary:	KDE SSH Frontend
Summary(pl):	Frontend SSH dla KDE
Summary(pt_BR):	Ferramenta de execução remota de programas
Group:		X11/Applications
Requires:	kdelibs >= %{_minlibsevr}
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
Requires:	kdebase-infocenter >= %{_minbaseevr}
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
Requires:	kdebase-core >= %{_minbaseevr}
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
Requires:	kdebase-core >= %{_minbaseevr}
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
Requires:	kdebase-core >= %{_minbaseevr}
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
Requires:	kdebase-core >= %{_minbaseevr}
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
Requires:	kdebase-core >= %{_minbaseevr}
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
Requires:	kdebase-infocenter >= %{_minbaseevr}
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
Requires:	kdelibs >= %{_minlibsevr}
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

%package kmilo-kvaio
Summary:	Sony Vaio KMilo module
Summary(pl):	Modu³ KMilo dla laptopów Sony Vaio
Group:		X11/Applications
Requires:	kdebase-core >= %{_minbaseevr}
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
Requires:	kdebase-core >= %{_minbaseevr}
Requires:	%{name}-kmilo = %{epoch}:%{version}-%{release}
Obsoletes:	kdeutils-kmilo < 9:3.1.2.031022

%description kmilo-powerbook
KMilo module for PowerBooks support.

%description kmilo-powerbook -l pl
Modu³ KMilo dla PowerBooków.

%package kmilo-thinkpad
Summary:	ThinkPad KMilo module
Summary(pl):	Modu³ KMilo dla ThinkPadów
Group:		X11/Applications
Requires:	kdebase-core >= %{_minbaseevr}
Requires:	%{name}-kmilo = %{epoch}:%{version}-%{release}

%description kmilo-thinkpad
KMilo module for ThinkPads support.

%description kmilo-thinkpad -l pl
Modu³ KMilo dla ThinkPadów.

%package kregexpeditor
Summary:	Graphical regular expression editor
Summary(pl):	Graficzny edytor wyra¿eñ regularnych
Group:		X11/Applications
Requires:	kdebase-core >= %{_minbaseevr}
Obsoletes:	kregexpeditor

%description kregexpeditor
Graphical regular expression editor.

%description kregexpeditor -l pl
Graficzny edytor wyra¿eñ regularnych.

%package ksim
Summary:	K System Information Monitor
Summary(pl):	K System Information Monitor - monitor informacji o systemie
Group:		X11/Applications
Requires:	kdebase-desktop >= %{_minbaseevr}

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
Requires:	kdelibs >= %{_minlibsevr}
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
Requires:	kdebase-core >= %{_minbaseevr}

%description kwalletmanager
Password management tool for KDE.

%description kwalletmanager -l pl
Narzêdzie do zarz±dzania has³ami w KDE.

%prep
%setup -q
#%patch0 -p1

%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Utility;Archiving;/' \
	-e 's/Terminal=0/Terminal=false/' \
	ark/ark.desktop
%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Utility;Applet;/' \
	kdelirc/irkick/irkick.desktop
%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Utility;Calculator;/' \
	-e 's/Terminal=0/Terminal=false/' \
	kcalc/kcalc.desktop
%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;TextEditor;X-HexEditor;/' \
	-e 's/Terminal=0/Terminal=false/' \
	khexedit/khexedit.desktop
%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;System;Monitor;/' \
	-e '/\[Desktop Entry\]/aEncoding=UTF-8' \
	ksim/ksim.desktop
%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Utility;Applet;/' \
	kdf/kwikdisk.desktop
%{__sed} -i -e 's/Terminal=0/Terminal=false/' \
	kcharselect/KCharSelect.desktop \
	kdf/kdf.desktop \
	kdf/kwikdisk.desktop \
	kedit/KEdit.desktop \
	kfloppy/KFloppy.desktop \
	khexedit/khexedit.desktop \
	kjots/Kjots.desktop \
	kregexpeditor/kregexpeditor.desktop \
	ktimer/ktimer.desktop \
	kwallet/kwalletmanager.desktop
for f in `find . -name \*.desktop`; do
	if grep -q '^Categories=.*[^;]$' $f; then
		sed -i -e 's/\(^Categories=.*$\)/\1;/' $f
	fi
	if grep -q '\[ven\]' $f; then
		sed -i -e 's/\[ven\]/[ve]/' $f
	fi
done

%build
cp %{_datadir}/automake/config.sub admin

#export UNSERMAKE=%{_datadir}/unsermake/unsermake

#echo "KDE_OPTIONS = nofinal" >> ksim/monitors/snmp/Makefile.am

%{__make} -f admin/Makefile.common cvs

%configure \
	--disable-rpath \
	--enable-final \
	--with-qt-libraries=%{_libdir} \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
rm -rf *.lang

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir}

mv $RPM_BUILD_ROOT%{_desktopdir}/kde/kwallet{config,}.desktop

%find_lang ark			--with-kde
%find_lang irkick		--with-kde
%find_lang KRegExpEditor	--with-kde
%find_lang kcalc		--with-kde
%find_lang kcharselect		--with-kde
%find_lang kcontrol		--with-kde
%find_lang kdf			--with-kde
%find_lang blockdevices		--with-kde
cat blockdevices.lang >> kdf.lang
%find_lang kcmlirc		--with-kde
cat kcmlirc.lang >> irkick.lang
%find_lang kedit		--with-kde
%find_lang kfloppy		--with-kde
%find_lang kgpg			--with-kde
%find_lang khexedit		--with-kde
%find_lang kjots		--with-kde
%find_lang ksim			--with-kde
%find_lang ktimer		--with-kde
%find_lang kwallet		--with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	khexedit	-p /sbin/ldconfig
%postun	khexedit	-p /sbin/ldconfig

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
%attr(755,root,root) %{_libdir}/libkhexeditcommon.so
%attr(755,root,root) %{_libdir}/libkregexpeditorcommon.so
%attr(755,root,root) %{_libdir}/libksimcore.so
%{_includedir}/*

%files ark -f ark.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ark
%{_libdir}/libkdeinit_ark.la
%attr(755,root,root) %{_libdir}/libkdeinit_ark.so
%{_libdir}/kde3/ark.la
%attr(755,root,root) %{_libdir}/kde3/ark.so
%{_libdir}/kde3/libarkpart.la
%attr(755,root,root) %{_libdir}/kde3/libarkpart.so
%{_datadir}/apps/ark
%{_datadir}/config.kcfg/ark.kcfg
%{_datadir}/services/ark_part.desktop
%{_desktopdir}/kde/ark.desktop
%{_iconsdir}/*/*/apps/ark.*

%files kcalc -f kcalc.lang
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

%files kcharselect -f kcharselect.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kcharselect
%{_libdir}/kde3/kcharselect_panelapplet.la
%attr(755,root,root) %{_libdir}/kde3/kcharselect_panelapplet.so
%{_datadir}/apps/kcharselect
%{_datadir}/apps/kconf_update/kcharselect.upd
%{_datadir}/apps/kicker/applets/kcharselectapplet.desktop
%{_desktopdir}/kde/KCharSelect.desktop
%{_iconsdir}/*/*/apps/kcharselect.*

%files kdelirc -f irkick.lang
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
%{_datadir}/apps/remotes/sonytv.remote.xml
%{_datadir}/autostart/irkick.desktop
%{_desktopdir}/kde/irkick.desktop
%{_desktopdir}/kde/kcmlirc.desktop
%{_iconsdir}/hicolor/*/apps/irkick.png

%files kdessh
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kdessh

%files kdf -f kdf.lang
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

%files kedit -f kedit.lang
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

%files kfloppy -f kfloppy.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kfloppy
%{_desktopdir}/kde/KFloppy.desktop
%{_iconsdir}/*/*/apps/kfloppy.*

%files kgpg -f kgpg.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kgpg
%{_datadir}/apps/kgpg
%{_datadir}/apps/konqueror/servicemenus/encryptfile.desktop
%{_datadir}/apps/konqueror/servicemenus/encryptfolder.desktop
%{_datadir}/autostart/kgpg.desktop
%{_datadir}/config.kcfg/kgpg.kcfg
%{_desktopdir}/kde/kgpg.desktop
%{_iconsdir}/*/*/apps/kgpg.png

%files khexedit -f khexedit.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/khexedit
%{_libdir}/kde3/libkbyteseditwidget.la
%attr(755,root,root) %{_libdir}/kde3/libkbyteseditwidget.so
%{_libdir}/kde3/libkhexedit2part.la
%attr(755,root,root) %{_libdir}/kde3/libkhexedit2part.so
%{_libdir}/libkhexeditcommon.la
%attr(755,root,root) %{_libdir}/libkhexeditcommon.so.*.*.*
%{_datadir}/apps/khexedit
%{_datadir}/apps/khexedit2part
%{_datadir}/services/khexedit2part.desktop
%{_datadir}/services/kbyteseditwidget.desktop
%{_desktopdir}/kde/khexedit.desktop
%{_iconsdir}/*/*/apps/khexedit.*

%files kjots -f kjots.lang
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
%{_libdir}/kde3/kmilo_asus.la
%attr(755,root,root) %{_libdir}/kde3/kmilo_asus.so
%{_libdir}/kde3/kmilo_delli8k.la
%attr(755,root,root) %{_libdir}/kde3/kmilo_delli8k.so
%{_datadir}/services/kmilo/kmilo_asus.desktop
%{_datadir}/services/kmilo/kmilo_delli8k.desktop

%files kmilo-thinkpad
%defattr(644,root,root,755)
%{_libdir}/kde3/kcm_thinkpad.la
%attr(755,root,root) %{_libdir}/kde3/kcm_thinkpad.so
%{_libdir}/kde3/kmilo_thinkpad.la
%attr(755,root,root) %{_libdir}/kde3/kmilo_thinkpad.so
%{_datadir}/services/kmilo/kmilo_thinkpad.desktop
%{_desktopdir}/kde/thinkpad.desktop

%files klaptopdaemon -f kcontrol.lang
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

%files kregexpeditor -f KRegExpEditor.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kregexpeditor
%{_libdir}/libkregexpeditorcommon.la
%attr(755,root,root) %{_libdir}/libkregexpeditorcommon.so.*.*.*
%{_libdir}/kde3/libkregexpeditorgui.la
%attr(755,root,root) %{_libdir}/kde3/libkregexpeditorgui.so
%{_datadir}/apps/kregexpeditor
%{_datadir}/services/kregexpeditorgui.desktop
%{_desktopdir}/kde/kregexpeditor.desktop
%{_iconsdir}/*/*/*/kregexpeditor.png

%files ksim -f ksim.lang
%defattr(644,root,root,755)
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

%files ktimer -f ktimer.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ktimer
%{_desktopdir}/kde/ktimer.desktop
%{_iconsdir}/*/*/*/ktimer.png

%files kwalletmanager -f kwallet.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kwalletmanager
%{_libdir}/kde3/kcm_kwallet.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kwallet.so
%{_datadir}/apps/kwalletmanager
%{_datadir}/services/kwallet_config.desktop
%{_datadir}/services/kwalletmanager_show.desktop
%{_desktopdir}/kde/kwallet.desktop
%{_desktopdir}/kde/kwalletmanager.desktop
%{_desktopdir}/kde/kwalletmanager-kwalletd.desktop
%{_iconsdir}/crystalsvg/*/apps/kwalletmanager.png
