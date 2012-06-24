
%define         _state          unstable
%define         _kdever         kde-3.1-rc3

Summary:	K Desktop Environment - utilities
Summary(pl):	K Desktop Environment - narz�dzia
Summary(es):	KDE - Utilitarios
Summary(ja):	KDE�ǥ����ȥå״Ķ� - �桼�ƥ���ƥ�
Summary(pt_BR):	KDE - Utilit�rios
Summary(ru):	K Desktop Environment - �������
Summary(uk):	K Desktop Environment - ���̦��
Summary(zh_CN):	KDEʵ�ù���
Name:		kdeutils
Version:	3.0.99
Release:	1
Epoch:		7
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{_kdever}/src/%{name}-%{version}.tar.bz2
# generated from kde-i18n
#Source1:	kde-i18n-%{name}-%{version}.tar.bz2
Patch0:		%{name}-kdf-label.patch
Patch1:		%{name}-kedit-confirmoverwrite.patch
Patch2:		%{name}-fix-kdf-mem-leak.patch
#Patch3:	%{name}-charselectapplet-no-version.patch
BuildRequires:	autoconf
BuildRequires:	automake
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
 - ksim - system monitor.

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
 - ksim

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
 - ksim - monitor systemu

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
Obsoletes:      kdeutils-cdbakeoven                                             
Obsoletes:      kdeutils-kab                                                    
Obsoletes:      kdeutils-karm                                                   
Obsoletes:      kdeutils-kfind                                                  
Obsoletes:      kdeutils-kljettool                                              
Obsoletes:      kdeutils-klpq                                                   
Obsoletes:      kdeutils-klprfax                                                
Obsoletes:      kdeutils-knotes                                                 
Obsoletes:      kdeutils-kpm                                                    
Obsoletes:      kregexpeditor-devel                                             
       
%description devel
This package includes the header files you will need to compile
applications that use kdeutils libraries.

%description devel -l pl
Ten pakiet zawiera pliki nag��wkowe niezb�dne do kompilacji aplikacji
u�ywaj�cych bibliotek kdeutils.

%description devel -l pt_BR
Arquivos de inclus�o para desenvolvimento e compila��o de programas
que usem as bibliotecas do kdeutils

%package ark
Summary:	KDE Archive Manager
Summary(pl):	Zarz�dca archiw�w dla KDE
Summary(pt_BR):	Gerenciador de pacotes TAR/comprimidos do KDE
Group:		X11/Applications
Requires:	kdelibs >= %{version}
Obsoletes:      kdeutils-cdbakeoven                                             
Obsoletes:      kdeutils-kab                                                    
Obsoletes:      kdeutils-karm                                                   
Obsoletes:      kdeutils-kfind                                                  
Obsoletes:      kdeutils-kljettool                                              
Obsoletes:      kdeutils-klpq                                                   
Obsoletes:      kdeutils-klprfax                                                
Obsoletes:      kdeutils-knotes                                                 
Obsoletes:      kdeutils-kpm                                                    
Obsoletes:      kregexpeditor-devel                                             
       
%description ark
Ark is a program for managing and quickly extracting archives.

%description ark -l pl
Ark jest programem s�u��cym do zarz�dzania i szybkiego rozpakowywania
archiw�w.

%description ark -l pt_BR
Gerenciador de pacotes TAR/comprimidos do KDE.

%package cdbakeoven
Summary:	Intuitive tool for burning CDs
Summary(pl):	Intuicyjne narz�dzie do wypalania CD
Group:		X11/Applications
Requires:	kdelibs >= %{version}
Requires:	cdrtools
Requires:	cdrtools-cdda2wav
Requires:	cdrtools-mkisofs
Requires:	cdparanoia-III

%description cdbakeoven
CD Bake Oven was designed with one goal in mind: combine the power and
stability of great command line utilities with contemporary easy to
use user interface. CDBO enables you to create data or music CDs in
the most intuitive matter, allowing you to control every aspect of the
process. It is built on top of very well known 'cdrecord', 'mkisofs',
'cdda2wav' and 'cdparanoia' encapsulating most of the options those
utilities provide. This makes creating professional quality media as
easy as making a few mouse clicks.

%description cdbakeoven -l pl
CD Bake Oven zosta� zaprojektowany w jednym celu: po��czy�
uniwersalno�� i stabilno�� doskona�ych narz�dzi linii polece� z �atwym
w u�yciu interfejsem. CDBO pozwala tworzy� CD z danymi lub muzyk� w
najbardziej intuicyjny spos�b, pozwalaj�c kontrolowa� wszystkie
aspekty procesu. Zosta� zbudowany na bazie doskonale znanych program�w
,,cdrecord'', ,,mkisofs'', ,,cdda2wav'' oraz ,,cdparanoia'' daj�c
dost�p do wi�kszo�ci ich opcji. Czyni to no�nik�w o profesjonalnej
jako�ci r�wnie �atwym jak klikanie myszk�.

%package kab
Summary:	KDE Address Book
Summary(pl):	Ksi��ka adresowa dla KDE
Summary(pt_BR):	Gerenciador do livro de endere�os
Group:		X11/Applications
Requires:	kdelibs >= %{version}

%description kab
Kab is a simple address book for KDE.

%description kab -l pl
Kab jest prost� ksi��k� adresow� dla KDE.

%description kab -l pt_BR
Gerenciador do livro de endere�os.

%package kcalc
Summary:	KDE Calculator
Summary(pl):	Kalkulator dla KDE
Summary(pt_BR):	Calculadora do KDE
Group:		X11/Applications
Requires:	kdelibs >= %{version}
Obsoletes:	kcalc
Obsoletes:      kdeutils-cdbakeoven                                             
Obsoletes:      kdeutils-kab                                                    
Obsoletes:      kdeutils-karm                                                   
Obsoletes:      kdeutils-kfind                                                  
Obsoletes:      kdeutils-kljettool                                              
Obsoletes:      kdeutils-klpq                                                   
Obsoletes:      kdeutils-klprfax                                                
Obsoletes:      kdeutils-knotes                                                 
Obsoletes:      kdeutils-kpm                                                    
Obsoletes:      kregexpeditor-devel                                             
       
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
Obsoletes:      kdeutils-cdbakeoven                                             
Obsoletes:      kdeutils-kab                                                    
Obsoletes:      kdeutils-karm                                                   
Obsoletes:      kdeutils-kfind                                                  
Obsoletes:      kdeutils-kljettool                                              
Obsoletes:      kdeutils-klpq                                                   
Obsoletes:      kdeutils-klprfax                                                
Obsoletes:      kdeutils-knotes                                                 
Obsoletes:      kdeutils-kpm                                                    
Obsoletes:      kregexpeditor-devel                                             
       
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
Obsoletes:      kdeutils-cdbakeoven                                             
Obsoletes:      kdeutils-kab                                                    
Obsoletes:      kdeutils-karm                                                   
Obsoletes:      kdeutils-kfind                                                  
Obsoletes:      kdeutils-kljettool                                              
Obsoletes:      kdeutils-klpq                                                   
Obsoletes:      kdeutils-klprfax                                                
Obsoletes:      kdeutils-knotes                                                 
Obsoletes:      kdeutils-kpm                                                    
Obsoletes:      kregexpeditor-devel                                             
       
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
Obsoletes:      kdeutils-cdbakeoven                                             
Obsoletes:      kdeutils-kab                                                    
Obsoletes:      kdeutils-karm                                                   
Obsoletes:      kdeutils-kfind                                                  
Obsoletes:      kdeutils-kljettool                                              
Obsoletes:      kdeutils-klpq                                                   
Obsoletes:      kdeutils-klprfax                                                
Obsoletes:      kdeutils-knotes                                                 
Obsoletes:      kdeutils-kpm                                                    
Obsoletes:      kregexpeditor-devel                                             
       
%description kdessh
SSH Frontend.

%description kdessh -l pl
Frontend SSH dla KDE.

%description kdessh -l pt_BR
Ferramenta de execu��o remota de programas.

%package kdf
Summary:	KDE Disk space GUI
Summary(pl):	df dla KDE
Summary(pt_BR):	Mostra o status de espa�o em disco
Group:		X11/Applications
Requires:	kdelibs >= %{version}
Obsoletes:	kdf
Obsoletes:      kdeutils-cdbakeoven                                             
Obsoletes:      kdeutils-kab                                                    
Obsoletes:      kdeutils-karm                                                   
Obsoletes:      kdeutils-kfind                                                  
Obsoletes:      kdeutils-kljettool                                              
Obsoletes:      kdeutils-klpq                                                   
Obsoletes:      kdeutils-klprfax                                                
Obsoletes:      kdeutils-knotes                                                 
Obsoletes:      kdeutils-kpm                                                    
Obsoletes:      kregexpeditor-devel                                             
       
%description kdf
This program shows the disk usage of the mounted devices.

%description kdf -l pl
Ten program pokazuje zaj�to�� dysku dla zamontowanych urz�dze�.

%description kdf -l pt_BR
Mostra o status de espa�o em disco.

%package kedit
Summary:	KDE Text Editor
Summary(pl):	Edytor tekstu dla KDE
Summary(pt_BR):	Editor de texto melhorado do KDE
Group:		X11/Applications/Editors
Requires:	kdelibs >= %{version}
Obsoletes:	kedit
Obsoletes:      kdeutils-cdbakeoven                                             
Obsoletes:      kdeutils-kab                                                    
Obsoletes:      kdeutils-karm                                                   
Obsoletes:      kdeutils-kfind                                                  
Obsoletes:      kdeutils-kljettool                                              
Obsoletes:      kdeutils-klpq                                                   
Obsoletes:      kdeutils-klprfax                                                
Obsoletes:      kdeutils-knotes                                                 
Obsoletes:      kdeutils-kpm                                                    
Obsoletes:      kregexpeditor-devel                                             
       
%description kedit
Simple text editor for KDE.

%description kedit -l pl
Prosty edytor tekstu dla KDE.

%description kedit -l pt_BR
Editor de texto melhorado do KDE.

%package kfloppy
Summary:	KDE Floppy Formater
Summary(pl):	Program formatuj�cy dyskietki dla KDE
Summary(pt_BR):	Ferramenta de formata��o de disquetes
Group:		X11/Applications
Requires:	kdelibs >= %{version}
Requires:	dosfstools
Obsoletes:	kfloppy
Obsoletes:      kdeutils-cdbakeoven                                             
Obsoletes:      kdeutils-kab                                                    
Obsoletes:      kdeutils-karm                                                   
Obsoletes:      kdeutils-kfind                                                  
Obsoletes:      kdeutils-kljettool                                              
Obsoletes:      kdeutils-klpq                                                   
Obsoletes:      kdeutils-klprfax                                                
Obsoletes:      kdeutils-knotes                                                 
Obsoletes:      kdeutils-kpm                                                    
Obsoletes:      kregexpeditor-devel                                             
       
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
Group:		X11/Applications/Editors
Requires:	kdelibs >= %{version}
Obsoletes:	khexedit
Obsoletes:      kdeutils-cdbakeoven                                             
Obsoletes:      kdeutils-kab                                                    
Obsoletes:      kdeutils-karm                                                   
Obsoletes:      kdeutils-kfind                                                  
Obsoletes:      kdeutils-kljettool                                              
Obsoletes:      kdeutils-klpq                                                   
Obsoletes:      kdeutils-klprfax                                                
Obsoletes:      kdeutils-knotes                                                 
Obsoletes:      kdeutils-kpm                                                    
Obsoletes:      kregexpeditor-devel                                             
       
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
Obsoletes:      kdeutils-cdbakeoven                                             
Obsoletes:      kdeutils-kab                                                    
Obsoletes:      kdeutils-karm                                                   
Obsoletes:      kdeutils-kfind                                                  
Obsoletes:      kdeutils-kljettool                                              
Obsoletes:      kdeutils-klpq                                                   
Obsoletes:      kdeutils-klprfax                                                
Obsoletes:      kdeutils-knotes                                                 
Obsoletes:      kdeutils-kpm                                                    
Obsoletes:      kregexpeditor-devel                                             
       
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
Obsoletes:      kdeutils-cdbakeoven                                             
Obsoletes:      kdeutils-kab                                                    
Obsoletes:      kdeutils-karm                                                   
Obsoletes:      kdeutils-kfind                                                  
Obsoletes:      kdeutils-kljettool                                              
Obsoletes:      kdeutils-klpq                                                   
Obsoletes:      kdeutils-klprfax                                                
Obsoletes:      kdeutils-knotes                                                 
Obsoletes:      kdeutils-kpm                                                    
Obsoletes:      kregexpeditor-devel                                             
       
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

%description klprfax
With this program you can fax by printing to an lpd device.

%description klprfax -l pl
Program ten umo�liwia wysy�anie faks�w przez drukowanie ich do lpd.

%description klprfax -l pt_BR
Interface para impress�o em sa�da de fax.

%package knotes
Summary:	KDE Notes
Summary(pl):	Notes dla KDE
Summary(pt_BR):	Pequeno editor de texto para guardar notas r�pidas
Group:		X11/Applications
Requires:	kdelibs >= %{version}

%description knotes
KNotes is ment to be a really usable and good looking notes
application for the KDE project.

%description knotes -l pl
KNotes to program umo�liwiaj�cy spisywanie notatek i trzymanie ich
widocznych na ekranie.

%description knotes -l pt_BR
Pequeno editor de texto para guardar notas r�pidas.

%package kpm
Summary:	KDE Process Manager
Summary(pl):	Zarz�dca proces�w dla KDE
Summary(pt_BR):	Monitor gr�fico de processos e do sistema
Group:		X11/Applications
Requires:	kdelibs >= %{version}

%description kpm
kpm allows you to view and modify the processes of your Linux
computer. It shows detailed information of running processes, computer
resources like RAM, swap space, CPU utilization and so on. You can
kill processes and modify their priority.

%description kpm -l pl
kpm umo�liwia Ci zarz�dzanie procesami w Twoim systemie. Wy�wietla
szczeg�owe informacje na temat uruchomionych proces�w, zasob�w
systemu jak np. wielko�� u�ywanej pami�ci czy partycji wymiany,
wykorzystanie procesora, itp. Masz mo�liwo�� zabijania proces�w i
modyfikowania ich priorytet�w.

%description kpm -l pt_BR
Monitor gr�fico de processos e do sistema.

%package kregexpeditor
Summary:	Graphical regular expression editor
Summary(pl):	Graficzny edytor wyra�e� regularnych
Group:		X11/Applications
Requires:	kdelibs >= %{version}
Obsoletes:	kregexpeditor
Obsoletes:      kdeutils-cdbakeoven                                             
Obsoletes:      kdeutils-kab                                                    
Obsoletes:      kdeutils-karm                                                   
Obsoletes:      kdeutils-kfind                                                  
Obsoletes:      kdeutils-kljettool                                              
Obsoletes:      kdeutils-klpq                                                   
Obsoletes:      kdeutils-klprfax                                                
Obsoletes:      kdeutils-knotes                                                 
Obsoletes:      kdeutils-kpm                                                    
Obsoletes:      kregexpeditor-devel                                             
       
%description kregexpeditor
Graphical regular expression editor.

%description kregexpeditor -l pl
Graficzny edytor wyra�e� regularnych.

%package ksim
Summary:	K System Information Monitor
Summary(pl):	K System Information Monitor
Group:		X11/Applications
Requires:	kdelibs >= %{version}
Obsoletes:      kdeutils-cdbakeoven                                             
Obsoletes:      kdeutils-kab                                                    
Obsoletes:      kdeutils-karm                                                   
Obsoletes:      kdeutils-kfind                                                  
Obsoletes:      kdeutils-kljettool                                              
Obsoletes:      kdeutils-klpq                                                   
Obsoletes:      kdeutils-klprfax                                                
Obsoletes:      kdeutils-knotes                                                 
Obsoletes:      kdeutils-kpm                                                    
Obsoletes:      kregexpeditor-devel                                             
       
%description ksim
System Monitor.

%description ksim -l pl
Monitor systemu.

%package ktimer
Summary:	KDE Timer
Summary(pl):	Zegarek KDE
Summary(pt_BR):	Monitor de tempo em forma de mini-aplicativo
Group:		X11/Applications
Requires:	kdelibs >= %{version}
Obsoletes:	ktimer
Obsoletes:	kdeutils-cdbakeoven
Obsoletes:	kdeutils-kab
Obsoletes:	kdeutils-karm
Obsoletes:	kdeutils-kfind
Obsoletes:	kdeutils-kljettool
Obsoletes:	kdeutils-klpq
Obsoletes:	kdeutils-klprfax
Obsoletes:	kdeutils-knotes
Obsoletes:	kdeutils-kpm
Obsoletes:	kregexpeditor-devel 

%description ktimer
Time tracker appplet.

%description ktimer -l pl
Zegarek.

%description ktimer -l pt_BR
Monitor de tempo em forma de mini-aplicativo.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
#%patch3 -p1

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

#%{__make} -C kab
# Doesn't build.
#%{__make} -C kcardtools

%install
rm -rf $RPM_BUILD_ROOT
install -d \
    $RPM_BUILD_ROOT%{_applnkdir}/Settings/KDE

%{__make} install DESTDIR=$RPM_BUILD_ROOT
#%{__make} -C kab install DESTDIR=$RPM_BUILD_ROOT
# Doesn't build.
#%{__make} -C kcardtools install DESTDIR=$RPM_BUILD_ROOT

ALD=$RPM_BUILD_ROOT%{_applnkdir}
mv -f $ALD/{Settings/[!K]*,Settings/KDE}
mv -f $ALD/{Settingsmenu/*.desktop,Settings}
mv -f $ALD/{System/More/*.desktop,System}  
mv -f $ALD/{Utilities/More/*.desktop,Utilities}
mv -f $ALD/{Utilities/khexedit.desktop,Editors}

#mv $RPM_BUILD_ROOT%{_applnkdir}/System/{More/,}/ksim.desktop

#bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT

%find_lang ark			--with-kde
%find_lang KRegExpEditor	--with-kde
#%find_lang kregexpeditor	--with-kde
#cat kregexpeditor.lang >> KRegExpEditor.lang
#%find_lang kab			--with-kde
#%find_lang kab3		--with-kde
#cat kab3.lang >> kab.lang
#%find_lang kcardchooser	--with-kde
%find_lang kcalc		--with-kde
%find_lang kcharselect		--with-kde
#%find_lang kcharselectapplet	--with-kde
#cat kcharselectapplet.lang >> kcharselect.lang
#%find_lang kdepasswd		--with-kde
#%find_lang kdessh		--with-kde
> kdf.lang
%find_lang kdf			--with-kde
%find_lang blockdevices		--with-kde
cat blockdevices.lang >> kdf.lang
%find_lang kedit		--with-kde
%find_lang kfloppy		--with-kde
%find_lang khexedit		--with-kde
%find_lang kjots		--with-kde
> klaptopdaemon.lang
#%find_lang klaptopdaemon	--with-kde
%find_lang kcmlowbatcrit	--with-kde
%find_lang kcmlowbatwarn	--with-kde
%find_lang laptop		--with-kde
%find_lang powerctrl		--with-kde
cat {kcmlowbatcrit,kcmlowbatwarn,laptop,powerctrl}.lang >> klaptopdaemon.lang
#%find_lang kcmlaptop		--with-kde
#cat kcmlaptop.lang >> klaptopdaemon.lang
#%find_lang kljettool		--with-kde
#%find_lang klpq		--with-kde
#%find_lang klprfax		--with-kde
#%find_lang kpm			--with-kde
%find_lang ktimer		--with-kde
#%find_lang cdbakeoven		--with-kde
%find_lang ksim			--with-kde
# Does not build:
#%find_lang kcardchooser	--with-kde

%clean
rm -rf $RPM_BUILD_ROOT

#%post   ark -p /sbin/ldconfig
#%postun ark -p /sbin/ldconfig

#%post   ksim -p /sbin/ldconfig
#%postun ksim -p /sbin/ldconfig

%files devel
%defattr(644,root,root,755)
%{_includedir}/*
%{_libdir}/libark.so
%{_libdir}/libksimcore.so

%files ark -f ark.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ark
%attr(755,root,root) %{_libdir}/libark.so.*
%attr(755,root,root) %{_libdir}/libark.la
%{_datadir}/apps/ark
%{_datadir}/apps/konqueror/servicemenus/arkservicemenu.desktop
%{_datadir}/services/ark_part.desktop
%{_applnkdir}/Utilities/ark.desktop
%{_pixmapsdir}/*/*/apps/ark.*

#%files cdbakeoven
#-f cdbakeoven.lang
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/cdbakeoven
#%{_libdir}/kde3/libkcm_cdbo*
#%{_datadir}/apps/cdbakeoven
#%{_datadir}/mimelnk/application/cdbo-file-list.desktop
#%{_datadir}/mimelnk/inode/ISO-image.desktop
#%{_pixmapsdir}/*/*/mimetypes/cd*.png
#%{_pixmapsdir}/*/*/apps/cd*.png
#%{_applnkdir}/Utilities/cdbakeoven.desktop
#%{_applnkdir}/Settings/KDE/CDBakeOven

#%files kab -f kab.lang
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/kab3
#%attr(755,root,root) %{_libdir}/kde3/libkab3part*
#%{_applnkdir}/Utilities/kab3.desktop
#%{_datadir}/apps/kab3
#%{_pixmapsdir}/*/*/apps/kab3.*
#%{_datadir}/services/kab3_part.desktop

%files kcalc -f kcalc.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kcalc
%attr(755,root,root) %{_libdir}/kcalc.*
%{_applnkdir}/Utilities/kcalc.desktop
%{_pixmapsdir}/*/*/apps/kcalc.*

%files kcharselect -f kcharselect.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kcharselect
%attr(755,root,root) %{_libdir}/kde3/kcharselect_panelapplet.*
%{_datadir}/apps/kicker/applets/kcharselectapplet.desktop
%{_applnkdir}/Utilities/KCharSelect.desktop
%{_pixmapsdir}/*/*/apps/kcharselect.*

#%files kdepasswd -f kdepasswd.lang
%files kdepasswd
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kdepasswd
%{_applnkdir}/Utilities/kdepasswd.desktop
%{_applnkdir}/Settings/kdepasswd.desktop

#%files kdessh -f kdessh.lang
%files kdessh
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kdessh

%files kdf -f kdf.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kdf
%attr(755,root,root) %{_bindir}/kwikdisk
%attr(755,root,root) %{_libdir}/kde3/kcm_kdf.*
%{_datadir}/apps/kdf
%{_applnkdir}/Settings/KDE/Information/kcmdf.desktop
%{_applnkdir}/System/kdf.desktop
%{_applnkdir}/System/kwikdisk.desktop
%{_pixmapsdir}/*/*/apps/kcmdf.*
%{_pixmapsdir}/*/*/apps/kdf.*
%{_pixmapsdir}/*/*/apps/kwikdisk.*

%files kedit -f kedit.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kedit
%attr(755,root,root) %{_libdir}/kedit.*
%{_datadir}/apps/kedit
%{_applnkdir}/Editors/KEdit.desktop
%{_pixmapsdir}/*/*/apps/kedit.*

%files kfloppy -f kfloppy.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kfloppy
%{_applnkdir}/Utilities/KFloppy.desktop
%{_pixmapsdir}/*/*/apps/kfloppy.*

%files khexedit -f khexedit.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/khexedit
%{_datadir}/apps/khexedit
%{_applnkdir}/Editors/khexedit.desktop
%{_pixmapsdir}/*/*/apps/khexedit.*

%files kjots -f kjots.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kjots
%{_datadir}/apps/kjots
%{_applnkdir}/Utilities/Kjots.desktop
%{_pixmapsdir}/*/*/apps/kjots.*

%files klaptopdaemon -f klaptopdaemon.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/klaptopdaemon
%attr(755,root,root) %{_libdir}/klaptopdaemon.*
%attr(755,root,root) %{_libdir}/kde3/kcm_laptop.*
%{_datadir}/apps/klaptopdaemon
%{_datadir}/services/klaptopdaemon.desktop
%{_applnkdir}/Settings/KDE/Information/pcmcia.desktop
%{_applnkdir}/Settings/KDE/PowerControl/*.desktop
%{_pixmapsdir}/*/*/*/*laptop*

##%files kljettool -f kljettool.lang
#%files kljettool
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/kljettool
#%{_applnkdir}/Utilities/KLJetTool.desktop
#%{_datadir}/apps/kljettool
#%{_pixmapsdir}/*/*/apps/kljettool.*

#%files klpq -f klpq.lang
#%files klpq
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/klpq
#%{_applnkdir}/Utilities/KLpq.desktop
#%{_pixmapsdir}/*/*/apps/klpq.*

#%files klprfax -f klprfax.lang
#%files klprfax
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/*fax*
#%attr(755,root,root) %{_bindir}/efix
#%{_applnkdir}/Utilities/klprfax.desktop
#%{_pixmapsdir}/*/*/apps/klprfax.*
#%{_mandir}/man1/*fax.1
#%{_mandir}/man1/efix.1

#%files knotes
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/knotes
#%{_applnkdir}/Utilities/knotes.desktop
#%{_datadir}/apps/knotes
#%{_datadir}/config/knotesrc
#%{_includedir}/KNotesIface.h
#%{_pixmapsdir}/*/*/apps/knotes.*
#
#%files kpm -l kpm.lang
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/kpm
#%attr(755,root,root) %{_bindir}/kpmdocked
#%{_applnkdir}/System/kpm.desktop
#%{_pixmapsdir}/*/*/apps/kpm.*

%files kregexpeditor -f KRegExpEditor.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/libkregexpeditorgui.*
%{_datadir}/apps/kregexpeditor
%{_datadir}/services/kregexpeditorgui.desktop

%files ksim -f ksim.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ksim
%attr(755,root,root) %{_libdir}/ksim.*
%attr(755,root,root) %{_libdir}/libksimcore.la
%attr(755,root,root) %{_libdir}/libksimcore.so.*
%attr(755,root,root) %{_libdir}/kde3/ksim*
%{_datadir}/apps/ksim
%{_datadir}/config/ksimrc
%{_pixmapsdir}/*/*/apps/ksim*.png
%{_pixmapsdir}/*/*/devices/ksim*.png
%{_applnkdir}/System/ksim.desktop

%files ktimer -f ktimer.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ktimer
%{_applnkdir}/Utilities/ktimer.desktop
