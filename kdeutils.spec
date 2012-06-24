#
# Conditional build:
# _with_pixmapsubdirs - leave different depth/resolution icons
#
%define		_with_pixmapsubdirs	1
Summary:	K Desktop Environment - utilities
Summary(pl):	K Desktop Environment - narz�dzia
Summary(es):	KDE - Utilitarios
Summary(ja):	KDE�ǥ����ȥå״Ķ� - �桼�ƥ���ƥ�
Summary(ko):	K ����ũž ȯ�� - �������� ����
Summary(pt_BR):	KDE - Utilit�rios
Summary(ru):	K Desktop Environment - �������
Summary(uk):	K Desktop Environment - ���̦��
Summary(zh_CN):	KDEʵ�ù���
Name:		kdeutils
Version:	3.0.5a
Release:	0.3
Epoch:		7
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.bz2
# generated from kde-i18n
Source1:	kde-i18n-%{name}-%{version}.tar.bz2
Source2:	%{name}-extra_icons.tar.bz2
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-kdf-label.patch
Patch2:		%{name}-kedit-confirmoverwrite.patch
Patch3:		%{name}-fix-klaptopdaemon-mem-leak.patch
Patch4:		%{name}-fix-klaptodeamon-mem-leak2.patch
Patch5:		%{name}-fix-klaptodeamon-mem-leak3.patch
Patch6:		%{name}-use-klineeditdlg.patch
Patch7:		%{name}-fix-kdf-mem-leak.patch
Patch8:		%{name}-fix-kedit-enable-disable-cut-copy-action.patch
Patch9:		%{name}-charselectapplet-no-version.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	awk
BuildRequires:	bzip2
BuildRequires:	fam-devel
BuildRequires:	grep
BuildRequires:	kdelibs-devel >= %{version}
BuildRequires:	libxml2-progs
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_fontdir	/usr/share/fonts
%define		_htmldir	/usr/share/doc/kde/HTML

%define		no_install_post_chrpath		1

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

%description -l ja
KDE�ǥ����ȥå״Ķ��ѤΥ桼�ƥ���ƥ�
�ʲ��Τ褦�ʥѥå����������äƤ��ޤ���

- ark - �������������ġ���
- karm - personal time tracker
- kcalc - ����
- kedit - �ƥ����ȥ��ǥ���
- kfloppy - �ե�åԡ��ե����ޥå�
- khexedit - �Х��ʥꥨ�ǥ���
- kjots - note taker
- kljettool - HP�ץ������ġ���
- knotes - �ݥ��ȥ��å�

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

%description -l ru
������� ��� K Desktop Environment. ��������:
 - ark - �������� ������� tar/gzip,
 - kab - �������� �����,
 - karm - ������������ �����������,
 - kcalc - ������� �����������,
 - kedit - ������� ��������� ��������,
 - kfloppy - ������� ��� �������������� ������-������,
 - khexedit - �������� �������� ������,
 - kjots - �������,
 - klipper - ������� ��� ������ � ������� ������,
 - kljettool - ������� ��� ��������� ���������, ����������� � HP,
 - klpq - �������� ������� ������,
 - knotes - post-it notes ��� ��������,
 - kpm - �������� ���������, ������� �� 'top', �� ����� �����������.

%description -l uk
������� ��� K Desktop Environment. ������:
 - ark - �������� ��Ȧצ� tar/gzip,
 - kab - ������� �����,
 - karm - ������������ ������������,
 - kcalc - ������� �����������,
 - kedit - ������� ��������� ��������,
 - kfloppy - ���̦�� ��� ������������ ���Ц-���˦�,
 - khexedit - �������� ¦������ ���̦�,
 - kjots - ��������,
 - klipper - ���̦�� ��� ������ � ������� ��ͦ��,
 - kljettool - ���̦�� ��� ������������ �Ҧ���Ҧ�, ��ͦ���� � HP,
 - klpq - �������� ����� �����,
 - knotes - post-it notes ��� ��������,
 - kpm - �������� �����Ӧ�, ������ �� 'top', ��� � ¦������
   ������������.

%package devel
Summary:	Header files for compiling applications that use kdeutils libraries
Summary(pl):	Pliki nag��wkowe do kompilacji aplikacji u�ywaj�cych bibliotek kde
Summary(pt_BR):	Arquivos de inclus�o para as bibliotecas do kdeutils
Group:		X11/Development/Libraries
Requires:	kdelibs-devel >= %{version}
Requires:	kdebase-devel >= %{version}
Obsoletes:	kregexpeditor-devel
Obsoletes:	kdeutils-kab
Obsoletes:	kdeutils-karm
Obsoletes:	kdeutils-kfind
Obsoletes:	kdeutils-khexdit
Obsoletes:	kdeutils-knotes
Obsoletes:	kdeutils-kpm

%description devel
This package includes the header files you will need to compile
applications that use kdeutils libraries.

%description devel -l pl
Ten pakiet zawiera pliki nag��wkowe niezb�dne do kompilacji aplikacji
u�ywaj�cych bibliotek kdeutils.

%description devel -l pt_BR
Arquivos de inclus�o para desenvolvimento e compila��o de programas
que usem as bibliotecas do kdeutils.

%package ark
Summary:	KDE Archive Manager
Summary(pl):	Zarz�dca archiw�w dla KDE
Summary(pt_BR):	Gerenciador de pacotes TAR/comprimidos do KDE
Group:		X11/Applications
Requires:	kdelibs >= %{version}
Obsoletes:	kdeutils-kab
Obsoletes:	kdeutils-karm
Obsoletes:	kdeutils-kfind
Obsoletes:	kdeutils-khexdit
Obsoletes:	kdeutils-knotes
Obsoletes:	kdeutils-kpm

%description ark
Ark is a program for managing and quickly extracting archives.

%description ark -l pl
Ark jest programem s�u��cym do zarz�dzania i szybkiego rozpakowywania
archiw�w.

%description ark -l pt_BR
Gerenciador de pacotes TAR/comprimidos do KDE.

%package kcalc
Summary:	KDE Calculator
Summary(pl):	Kalkulator dla KDE
Summary(pt_BR):	Calculadora do KDE
Group:		X11/Applications
Requires:	kdelibs >= %{version}
Obsoletes:	kcalc
Obsoletes:	kdeutils-kab
Obsoletes:	kdeutils-karm
Obsoletes:	kdeutils-kfind
Obsoletes:	kdeutils-khexdit
Obsoletes:	kdeutils-knotes
Obsoletes:	kdeutils-kpm

%description kcalc
Calculator for KDE.

%description kcalc -l pl
Kalkulator dla KDE.

%description kcalc -l pt_BR
Calculadora do KDE.

%package kcharselect
Summary:	KDE Character Selector
Summary(pl):	Wybierajka znak�w dla KDE
Summary(pt_BR):	Ferramenta de sele��o de caracteres
Group:		X11/Applications
Requires:	kdelibs >= %{version}
Obsoletes:	kcharselect
Obsoletes:	kdeutils-kab
Obsoletes:	kdeutils-karm
Obsoletes:	kdeutils-kfind
Obsoletes:	kdeutils-khexdit
Obsoletes:	kdeutils-knotes
Obsoletes:	kdeutils-kpm

%description kcharselect
Character Selector.

%description kcharselect -l pl
Program do wybierania znak�w.

%package kdepasswd
Summary:	KDE Passwd
Summary(pl):	passwd dla KDE
Summary(pt_BR):	Ferramenta de mudan�a de senha
Group:		X11/Applications
Requires:	kdelibs >= %{version}
Obsoletes:	kdepasswd
Obsoletes:	kdeutils-kab
Obsoletes:	kdeutils-karm
Obsoletes:	kdeutils-kfind
Obsoletes:	kdeutils-khexdit
Obsoletes:	kdeutils-knotes
Obsoletes:	kdeutils-kpm

%description kdepasswd
Change your password.

%description kdepasswd -l pl
Program do zmiany has�a z poziomu KDE.

%description kdepasswd -l pt_BR
Ferramenta de mudan�a de senha.

%package kdessh
Summary:	KDE SSH Frontend
Summary(pl):	Frontend SSH dla KDE
Summary(pt_BR):	Ferramenta de execu��o remota de programas
Group:		X11/Applications
Requires:	kdelibs >= %{version}
Obsoletes:	kdessh
Obsoletes:	kdeutils-kab
Obsoletes:	kdeutils-karm
Obsoletes:	kdeutils-kfind
Obsoletes:	kdeutils-khexdit
Obsoletes:	kdeutils-knotes
Obsoletes:	kdeutils-kpm

%description kdessh
SSH Frontend.

%description kdessh -l pl
Frontend SSH dla KDE.

%description kdessh -l pt_BR
Ferramenta de execu��o remota de programas.

%package kedit
Summary:	KDE Text Editor
Summary(pl):	Edytor tekstu dla KDE
Summary(pt_BR):	Editor de texto melhorado do KDE
Group:		X11/Applications
Requires:	kdelibs >= %{version}
Obsoletes:	kedit
Obsoletes:	kdeutils-kab
Obsoletes:	kdeutils-karm
Obsoletes:	kdeutils-kfind
Obsoletes:	kdeutils-khexdit
Obsoletes:	kdeutils-knotes
Obsoletes:	kdeutils-kpm

%description kedit
Simple text editor for KDE.

%description kedit -l pl
Prosty edytor tekstu dla KDE.

%description kedit -l pt_BR
Editor de texto melhorado do KDE.

%package kdf
Summary:	KDE Disk space GUI
Summary(pl):	df dla KDE
Summary(pt_BR):	Mostra o status de espa�o em disco
Group:		X11/Applications
Requires:	kdelibs >= %{version}
Obsoletes:	kdf
Obsoletes:	kdeutils-kab
Obsoletes:	kdeutils-karm
Obsoletes:	kdeutils-kfind
Obsoletes:	kdeutils-khexdit
Obsoletes:	kdeutils-knotes
Obsoletes:	kdeutils-kpm

%description kdf
This program shows the disk usage of the mounted devices.

%description kdf -l pl
Ten program pokazuje zaj�to�� dysku dla zamontowanych urz�dze�.

%description kdf -l pt_BR
Mostra o status de espa�o em disco.

%package kfloppy
Summary:	KDE Floppy Formater
Summary(pl):	Program formatuj�cy dyskietki dla KDE
Summary(pt_BR):	Ferramenta de formata��o de disquetes
Group:		X11/Applications
Requires:	kdelibs >= %{version}
Requires:	dosfstools
Obsoletes:	kfloppy
Obsoletes:	kdeutils-kab
Obsoletes:	kdeutils-karm
Obsoletes:	kdeutils-kfind
Obsoletes:	kdeutils-khexdit
Obsoletes:	kdeutils-knotes
Obsoletes:	kdeutils-kpm

%description kfloppy
KFloppy formats disks and puts a DOS or ext2fs filesystem on them.

%description kfloppy -l pl
KFloppy formatuje dyskietki i zak�ada na nich system pliku DOS lub
ext2.

%description kfloppy -l pt_BR
Ferramenta de formata��o de disquetes.

%package khexedit
Summary:	KDE Hex Editor
Summary(pl):	Edytor szesnastkowy dla KDE
Summary(pt_BR):	Editor hexadecimal para arquivos bin�rios
Group:		X11/Applications
Requires:	kdelibs >= %{version}
Obsoletes:	khexedit
Obsoletes:	kdeutils-kab
Obsoletes:	kdeutils-karm
Obsoletes:	kdeutils-kfind
Obsoletes:	kdeutils-khexdit
Obsoletes:	kdeutils-knotes
Obsoletes:	kdeutils-kpm

%description khexedit
Hex Editor is a small and simple viewer for binary files.

%description khexedit -l pl
Hex Editor jest ma�ym i prostym edytorem plik�w binarnych.

%description khexedit -l pt_BR
Editor hexadecimal para arquivos bin�rios.

%package kjots
Summary:	KDE Note taker
Summary(pl):	Notatnik dla KDE
Summary(pt_BR):	Ferramenta de armazenamento de livros
Group:		X11/Applications
Requires:	kdelibs >= %{version}
Obsoletes:	kjots
Obsoletes:	kdeutils-kab
Obsoletes:	kdeutils-karm
Obsoletes:	kdeutils-kfind
Obsoletes:	kdeutils-khexdit
Obsoletes:	kdeutils-knotes
Obsoletes:	kdeutils-kpm

%description kjots
kjots is a small note taker program. Name and idea are taken from the
jots program included in the tkgoodstuff package.

%description kjots -l pl
KJots to ma�y program do zapisywania notatek.

%description kjots -l pt_BR
Ferramenta de armazenamento de livros.

%package klaptopdaemon
Summary:	KDE Laptop Daemon
Summary(pl):	Wska�nik zu�ycia baterii w laptopie dla KDE
Summary(pt_BR):	Miniaplicativo de status de bateria para laptops
Group:		X11/Applications
Requires:	kdelibs >= %{version}
Obsoletes:	laptop
Obsoletes:	kdeutils-kab
Obsoletes:	kdeutils-karm
Obsoletes:	kdeutils-kfind
Obsoletes:	kdeutils-khexdit
Obsoletes:	kdeutils-knotes
Obsoletes:	kdeutils-kpm

%description klaptopdaemon
KDE Laptop Daemon.

%description klaptopdaemon -l pl
Wska�nik zu�ycia baterii w laptopie dla KDE.

%description klaptopdaemon -l pt_BR
Miniaplicativo de status de bateria para laptops

%package kljettool
Summary:	KDE LaserJet Tool
Summary(pl):	Konfigurator drukarek LaserJet dla KDE
Summary(pt_BR):	Interface de configura��o de impressora HP Laserjet
Group:		X11/Applications
Requires:	kdelibs >= %{version}
Obsoletes:	kljettool
Obsoletes:	kdeutils-kab
Obsoletes:	kdeutils-karm
Obsoletes:	kdeutils-kfind
Obsoletes:	kdeutils-khexdit
Obsoletes:	kdeutils-knotes
Obsoletes:	kdeutils-kpm

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
KLJetToll to program umo�liwiaj�cy konfiguracj� drukarek Hewlett
Packard LaserJet.

%description kljettool -l pt_BR
Interface de configura��o de impressora HP Laserjet.

%package klpq
Summary:	KDE Print Manager
Summary(pl):	Zarz�dca wydruku dla KDE
Summary(pt_BR):	Interface para gerenciamento das filas de impress�o
Group:		X11/Applications
Requires:	kdelibs >= %{version}
Obsoletes:	klpq
Obsoletes:	kdeutils-kab
Obsoletes:	kdeutils-karm
Obsoletes:	kdeutils-kfind
Obsoletes:	kdeutils-khexdit
Obsoletes:	kdeutils-knotes
Obsoletes:	kdeutils-kpm

%description klpq
Klpq is a frontend to the print spooler. Klpq does not modify the
printqueue by itself, but uses the underlying commands: lpq, lprm and
lpc.

%description klpq -l pl
Klpq jest nak�adk� graficzn� dla KDE, umo�liwiaj�c� zarz�dzanie
wydrukami. Nie modyfikuje kolejki wydruk�w sammodzielnie, lecz
wykorzystuje do tego celu polecenia: lpq, lprm i lpc.

%description klpq -l pt_BR
Interface para gerenciamento das filas de impress�o.

%package klprfax
Summary:	KDE LPD fax frontend using efax
Summary(pl):	Frontend do faksu via lpd dla KDE
Summary(pt_BR):	Interface para impress�o em sa�da de Fax
Group:		X11/Applications
Requires:	kdelibs >= %{version}
Requires:	efax
Obsoletes:	klprfax
Obsoletes:	kdeutils-kab
Obsoletes:	kdeutils-karm
Obsoletes:	kdeutils-kfind
Obsoletes:	kdeutils-khexdit
Obsoletes:	kdeutils-knotes
Obsoletes:	kdeutils-kpm

%description klprfax
With this program you can fax by printing to an lpd device.

%description klprfax -l pl
Program ten umo�liwia wysy�anie faks�w przez drukowanie ich do lpd.

%description klprfax -l pt_BR
Interface para impress�o em sa�da de fax.

%package ktimer
Summary:	KDE Timer
Summary(pl):	Zegarek KDE
Summary(pt_BR):	Monitor de tempo em forma de mini-aplicativo
Group:		X11/Applications
Requires:	kdelibs >= %{version}
Obsoletes:	ktimer
Obsoletes:	kdeutils-kab
Obsoletes:	kdeutils-karm
Obsoletes:	kdeutils-kfind
Obsoletes:	kdeutils-khexdit
Obsoletes:	kdeutils-knotes
Obsoletes:	kdeutils-kpm

%description ktimer
Time tracker appplet.

%description ktimer -l pl
Zegarek.

%description ktimer -l pt_BR
Monitor de tempo em forma de mini-aplicativo.

%package kregexpeditor
Summary:	Graphical regular expression editor
Summary(pl):	Graficzny edytor wyra�e� regularnych
Group:		X11/Applications
Requires:	kdelibs = %{version}
Obsoletes:	kregexpeditor
Obsoletes:	kdeutils-kab
Obsoletes:	kdeutils-karm
Obsoletes:	kdeutils-kfind
Obsoletes:	kdeutils-khexdit
Obsoletes:	kdeutils-knotes
Obsoletes:	kdeutils-kpm

%description kregexpeditor
Graphical regular expression editor.

%description kregexpeditor -l pl
Graficzny edytor wyra�e� regularnych.

%package ksim
Summary:	K System Information Monitor
Summary(pl):	K System Information Monitor
Group:		X11/Applications
Requires:	kdelibs = %{version}
Obsoletes:	kdeutils-kab
Obsoletes:	kdeutils-karm
Obsoletes:	kdeutils-kfind
Obsoletes:	kdeutils-khexdit
Obsoletes:	kdeutils-knotes
Obsoletes:	kdeutils-kpm

%description ksim
K System Information Monitor.

%description ksim -l pl
K System Information Monitor.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

%configure \
	%{!?debug:--disable-debug} \
	--with-qt-dir=%{_prefix} \
	--with-install-root=$RPM_BUILD_ROOT \
	--with-pam="yes" \
	--enable-final
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/{Settings/KDE,Utilities,Editors}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_applnkdir}/Settings/{Information,PowerControl} $RPM_BUILD_ROOT%{_applnkdir}/Settings/KDE

#mv $RPM_BUILD_ROOT%{_applnkdir}/System/{More/,}/ksim.desktop

# create in toplevel %%{_pixmapsdir} links to icons
for i in $RPM_BUILD_ROOT%{_pixmapsdir}/hicolor/48x48/apps/{ark,kcalc,kcharselect,kedit,kfloppy,khexedit,kjots,kljettool,klpq,laptop_battery,laptop_pcmcia}.png
do
%if %{?_with_pixmapsubdirs:1}%{!?_with_pixmapsubdirs:0}
	ln -sf `echo $i | sed "s:^$RPM_BUILD_ROOT%{_pixmapsdir}/::"` $RPM_BUILD_ROOT%{_pixmapsdir}	
%else
	cp -af $i $RPM_BUILD_ROOT%{_pixmapsdir}
%endif
done

bzip2 -dc %{SOURCE2} | tar xf - -C $RPM_BUILD_ROOT%{_pixmapsdir}
%if %{!?_with_pixmapsubdirs:1}%{?_with_pixmapsubdirs:0}
rm -f $RPM_BUILD_ROOT%{_pixmapsdir}/*color/??x??/*/{ark,kab3,kcalc,kcharselect,kedit,kfloppy,khexedit,kjots,kljettool,klpq,laptop_battery,laptop_pcmcia}.png
# resized
rm -f $RPM_BUILD_ROOT%{_pixmapsdir}/*color/??x??/*/{kcmdf,kdf,klprfax,kwikdisk}.png
%endif

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT

for f in `find $RPM_BUILD_ROOT%{_applnkdir} -name '.directory' -o -name '*.desktop'` ; do
	awk -v F=$f '/^Icon=/ && !/\.xpm$/ && !/\.png$/ { $0 = $0 ".png";} { print $0; } END { if(F == ".directory") print "Type=Directory"; }' < $f > $f.tmp
	mv -f $f{.tmp,}
done

%find_lang ark			--with-kde
%find_lang KRegExpEditor	--with-kde
%find_lang kregexpeditor	--with-kde
cat kregexpeditor.lang >> KRegExpEditor.lang
%find_lang kab			--with-kde
%find_lang kab3			--with-kde
cat kab3.lang >> kab.lang
%find_lang kcardchooser		--with-kde
%find_lang kcalc		--with-kde
%find_lang kcharselect		--with-kde
%find_lang kcharselectapplet	--with-kde
cat kcharselectapplet.lang >> kcharselect.lang
%find_lang kdepasswd	--with-kde
%find_lang kdessh	--with-kde
%find_lang kdf		--with-kde
%find_lang kedit	--with-kde
%find_lang kfloppy	--with-kde
%find_lang khexedit	--with-kde
%find_lang kjots	--with-kde
%find_lang klaptopdaemon	--with-kde
%find_lang kcmlaptop	--with-kde
cat kcmlaptop.lang >> klaptopdaemon.lang
%find_lang kljettool	--with-kde
%find_lang klpq		--with-kde
%find_lang klprfax	--with-kde
#%find_lang kpm		--with-kde
%find_lang ktimer	--with-kde
#%find_lang cdbakeoven	--with-kde
#%find_lang ksim	--with-kde
# Does not build:
%find_lang kcardchooser	--with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post   ark -p /sbin/ldconfig
%postun ark -p /sbin/ldconfig

%post   ksim -p /sbin/ldconfig
%postun ksim -p /sbin/ldconfig

%files devel
%defattr(644,root,root,755)
%{_includedir}/*
#%{_libdir}/libksimcore.so

%files ark -f ark.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ark
%attr(755,root,root) %{_libdir}/libark.so.*.*.*
%{_applnkdir}/Utilities/ark.desktop
%{_datadir}/apps/ark
%{_datadir}/apps/konqueror/servicemenus/arkservicemenu.desktop
%{_datadir}/services/arkpart.desktop
%{?_with_pixmapsubdirs:%{_pixmapsdir}/*color/*/apps/ark.png}
%{_pixmapsdir}/ark.png

%files kcalc -f kcalc.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kcalc
%attr(755,root,root) %{_libdir}/kcalc.*
%{_applnkdir}/Utilities/kcalc.desktop
%{?_with_pixmapsubdirs:%{_pixmapsdir}/*color/*/apps/kcalc.png}
%{_pixmapsdir}/kcalc.png

%files kcharselect -f kcharselect.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kcharselect
%attr(755,root,root) %{_libdir}/kde3/kcharselectapplet.??
%{_applnkdir}/Utilities/KCharSelect.desktop
%{_datadir}/apps/kicker/applets/kcharselectapplet.desktop
%{?_with_pixmapsubdirs:%{_pixmapsdir}/*color/*/apps/kcharselect.png}
%{_pixmapsdir}/kcharselect.png

%files kdepasswd -f kdepasswd.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kdepasswd
%{_applnkdir}/Utilities/kdepasswd.desktop

%files kdessh -f kdessh.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kdessh

%files kdf -f kdf.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kdf
%attr(755,root,root) %{_bindir}/kwikdisk
%attr(755,root,root) %{_libdir}/kde3/kcm_kdf.??
%{_datadir}/apps/kdf
%{_applnkdir}/System/kdf.desktop
%{_applnkdir}/System/kwikdisk.desktop
%{_applnkdir}/Settings/KDE/Information/kcmdf.desktop
%{?_with_pixmapsubdirs:%{_pixmapsdir}/*color/*/apps/kcmdf.png}
%{?_with_pixmapsubdirs:%{_pixmapsdir}/*color/*/apps/kdf.png}
%{?_with_pixmapsubdirs:%{_pixmapsdir}/*color/*/apps/kwikdisk.png}
%{_pixmapsdir}/kcmdf.png
%{_pixmapsdir}/kdf.png
%{_pixmapsdir}/kwikdisk.png

%files kedit -f kedit.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kedit
%attr(755,root,root) %{_libdir}/kedit.*
%{_applnkdir}/Editors/KEdit.desktop
%{_datadir}/apps/kedit
%{?_with_pixmapsubdirs:%{_pixmapsdir}/*color/*/apps/kedit.png}
%{_pixmapsdir}/kedit.png

%files kfloppy -f kfloppy.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kfloppy
%{_applnkdir}/Utilities/KFloppy.desktop
%{?_with_pixmapsubdirs:%{_pixmapsdir}/*color/*/apps/kfloppy.png}
%{_pixmapsdir}/kfloppy.png

%files khexedit -f khexedit.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/khexedit
%{_applnkdir}/Utilities/khexedit.desktop
%{_datadir}/apps/khexedit
%{?_with_pixmapsubdirs:%{_pixmapsdir}/*color/*/apps/khexedit.png}
%{_pixmapsdir}/khexedit.png

%files kjots -f kjots.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kjots
%{_applnkdir}/Utilities/Kjots.desktop
%{_datadir}/apps/kjots
%{?_with_pixmapsubdirs:%{_pixmapsdir}/*color/*/apps/kjots.png}
%{_pixmapsdir}/kjots.png

%files klaptopdaemon -f klaptopdaemon.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/klaptopdaemon
%attr(755,root,root) %{_libdir}/kde3/kcm_laptop.??
%attr(755,root,root) %{_libdir}/klaptopdaemon.??
%{_applnkdir}/Settings/KDE/Information/pcmcia.desktop
%{_applnkdir}/Settings/KDE/PowerControl/battery.desktop
%{_applnkdir}/Settings/KDE/PowerControl/bwarning.desktop
%{_applnkdir}/Settings/KDE/PowerControl/cwarning.desktop
%{_applnkdir}/Settings/KDE/PowerControl/power.desktop
%{_datadir}/apps/klaptopdaemon
%{_datadir}/services/klaptopdaemon.desktop
%{?_with_pixmapsubdirs:%{_pixmapsdir}/*color/*/apps/klaptopdaemon.png}
%{?_with_pixmapsubdirs:%{_pixmapsdir}/*color/*/apps/laptop_*.png}
%{_pixmapsdir}/laptop_*.png

%files kljettool -f kljettool.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kljettool
%{_applnkdir}/Utilities/KLJetTool.desktop
%{_datadir}/apps/kljettool
%{?_with_pixmapsubdirs:%{_pixmapsdir}/*color/*/apps/kljettool.png}
%{_pixmapsdir}/kljettool.png

%files klpq -f klpq.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/klpq
%{_applnkdir}/Utilities/KLpq.desktop
%{?_with_pixmapsubdirs:%{_pixmapsdir}/*color/*/apps/klpq.png}
%{_pixmapsdir}/klpq.png

%files klprfax -f klprfax.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*fax*
%attr(755,root,root) %{_bindir}/efix
%{_applnkdir}/Utilities/klprfax.desktop
%{?_with_pixmapsubdirs:%{_pixmapsdir}/*color/*/apps/klprfax.png}
%{_pixmapsdir}/klprfax.png
%{_mandir}/man1/*fax.1
%{_mandir}/man1/efix.1

%files ktimer -f ktimer.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ktimer
%{_applnkdir}/Utilities/ktimer.desktop

%files kregexpeditor -f KRegExpEditor.lang
%defattr(644,root,root,755)
%{_libdir}/kde3/libkregexpeditorgui.??
%{_datadir}/apps/kregexpeditor
%{_datadir}/services/kregexpeditorgui.desktop

#%files ksim -f ksim.lang
#%files ksim
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/ksim
#%{_libdir}/ksim.??
#%{_libdir}/libksimcore.la
#%{_libdir}/libksimcore.so.*.*.*
#%{_libdir}/kde3/ksim*
#%{_datadir}/apps/ksim
#%{_datadir}/config/ksimrc
#%{_pixmapsdir}/*/*/apps/ksim*.png
#%{_pixmapsdir}/*/*/devices/ksim*.png
#%{_applnkdir}/System/ksim.desktop
