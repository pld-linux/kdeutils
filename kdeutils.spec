
%define         _state          snapshots
%define         _ver		3.2
%define		_snap		030502

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
Release:	0.%{_snap}.1
Epoch:		8
License:	GPL
Group:		X11/Applications
#Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{name}-%{_snap}.tar.bz2
Source0:	http://team.pld.org.pl/~adgor/kde/%{name}-%{_snap}.tar.bz2
Patch0:		%{name}-kdf-label.patch
Patch1:		%{name}-kedit-confirmoverwrite.patch
Patch2:		%{name}-fix-kdf-mem-leak.patch
Patch3:		%{name}-vcategories.patch
Patch4:		%{name}-userinfo.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bzip2
BuildRequires:	fam-devel
BuildRequires:	grep
BuildRequires:	kdebase-devel >= %{version}
BuildRequires:	kdelibs-devel >= %{version}
BuildRequires:	libxml2-progs
BuildRequires:	libtool
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_htmldir	%{_docdir}/kde/HTML

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
 - ksim - monitor systemu

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
Summary(pl):	Pliki nag³ówkowe do kompilacji aplikacji u¿ywaj±cych bibliotek kde
Summary(pt_BR):	Arquivos de inclusão para as bibliotecas do kdeutils
Group:		X11/Development/Libraries
Requires:	kdelibs-devel >= %{version}
Requires:	kdebase-devel >= %{version}
Requires:	%{name}-klaptopdaemon
Requires:	%{name}-kmilo
Requires:	%{name}-ksim
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
Requires:	konqueror >= %{version}
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
Ark jest programem s³u¿±cym do zarz±dzania i szybkiego rozpakowywania
archiwów.

%description ark -l pt_BR
Gerenciador de pacotes TAR/comprimidos do KDE.

%package kcalc
Summary:	KDE Calculator
Summary(pl):	Kalkulator dla KDE
Summary(pt_BR):	Calculadora do KDE
Group:		X11/Applications
Requires:	kdebase-core >= %{version}
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
Summary(pl):	Wybierajka znaków dla KDE
Summary(pt_BR):	Ferramenta de seleção de caracteres
Group:		X11/Applications
Requires:	kdebase-kicker >= %{version}
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
Program do wybierania znaków.

%package kdepasswd
Summary:	KDE Passwd
Summary(pl):	passwd dla KDE
Summary(pt_BR):	Ferramenta de mudança de senha
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
Program do zmiany has³a z poziomu KDE.

%description kdepasswd -l pt_BR
Ferramenta de mudança de senha.

%package kdessh
Summary:	KDE SSH Frontend
Summary(pl):	Frontend SSH dla KDE
Summary(pt_BR):	Ferramenta de execução remota de programas
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
Ferramenta de execução remota de programas.

%package kdf
Summary:	KDE Disk space GUI
Summary(pl):	df dla KDE
Summary(pt_BR):	Mostra o status de espaço em disco
Group:		X11/Applications
Requires:	kdebase-infocenter >= %{version}
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
Ten program pokazuje zajêto¶æ dysku dla zamontowanych urz±dzeñ.

%description kdf -l pt_BR
Mostra o status de espaço em disco.

%package kedit
Summary:	KDE Text Editor
Summary(pl):	Edytor tekstu dla KDE
Summary(pt_BR):	Editor de texto melhorado do KDE
Group:		X11/Applications/Editors
Requires:	kdebase-core >= %{version}
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
Summary(pl):	Program formatuj±cy dyskietki dla KDE
Summary(pt_BR):	Ferramenta de formatação de disquetes
Group:		X11/Applications
Requires:	kdebase-core >= %{version}
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
KFloppy formatuje dyskietki i zak³ada na nich system pliku DOS lub
ext2.

%description kfloppy -l pt_BR
Ferramenta de formatação de disquetes.

%package kgpg
Summary:	A frontend for gpg
Summary(pl):	Nak³adka graficzna na gpg
Group:		X11/Applications
Requires:	konqueror >= %{version}
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

%description kgpg
kgpg is a simple, free, open source KDE frontend for gpg.

%description kgpg -l pl
kgpg jest prost± graficzn± nak³adk± na gpg przeznaczon± dla KDE.

%package khexedit
Summary:	KDE Hex Editor
Summary(pl):	Edytor szesnastkowy dla KDE
Summary(pt_BR):	Editor hexadecimal para arquivos binários
Group:		X11/Applications/Editors
Requires:	kdebase-core >= %{version}
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
Hex Editor jest ma³ym i prostym edytorem plików binarnych.

%description khexedit -l pt_BR
Editor hexadecimal para arquivos binários.

%package kjots
Summary:	KDE Note taker
Summary(pl):	Notatnik dla KDE
Summary(pt_BR):	Ferramenta de armazenamento de livros
Group:		X11/Applications
Requires:	kdebase-core >= %{version}
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
KJots to ma³y program do zapisywania notatek.

%description kjots -l pt_BR
Ferramenta de armazenamento de livros.

%package klaptopdaemon
Summary:	KDE Laptop Daemon
Summary(pl):	Wska¼nik zu¿ycia baterii w laptopie dla KDE
Summary(pt_BR):	Miniaplicativo de status de bateria para laptops
Group:		X11/Applications
Requires:	kdebase-infocenter >= %{version}
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
Wska¼nik zu¿ycia baterii w laptopie dla KDE.

%description klaptopdaemon -l pt_BR
Miniaplicativo de status de bateria para laptops

%package kmilo
Summary:	KDE Special Key Notifier
Summary(pl):	KDE Special Key Notifier
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
Obsoletes:	kregexpeditor-devel 

%description kmilo
KDE Special Key Notifier

%description kmilo -l pl

%package kregexpeditor
Summary:	Graphical regular expression editor
Summary(pl):	Graficzny edytor wyra¿eñ regularnych
Group:		X11/Applications
Requires:	kdebase-core >= %{version}
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
Graficzny edytor wyra¿eñ regularnych.

%package ksim
Summary:	K System Information Monitor
Summary(pl):	K System Information Monitor
Group:		X11/Applications
Requires:	kdebase-kicker >= %{version}
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

%package userinfo
Summary:	User Account
Summary(pl):	Konto u¿ytkownika
Group:		X11/Applications
Requires:	kdebase-core >= %{version}
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

%description userinfo
Changes user account information.

%description userinfo -l pl
Zmienia informacje o koncie u¿ytkownika.

%prep
%setup -q -n %{name}-%{_snap}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir
kde_appsdir="%{_applnkdir}"; export kde_appsdir

for plik in `find ./ -name *.desktop` ; do
	echo $plik
	sed -i -e 's/\[nb\]/\[no\]/g' $plik
done

%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_applnkdir}/{Settings,KDE-Settings}

mv $RPM_BUILD_ROOT%{_applnkdir}/Utilities/kgpg.desktop \
	$RPM_BUILD_ROOT%{_desktopdir}

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
%find_lang khexedit		--with-kde
%find_lang kjots		--with-kde
> klaptopdaemon.lang
%find_lang kcmlowbatcrit	--with-kde
%find_lang kcmlowbatwarn	--with-kde
%find_lang laptop		--with-kde
%find_lang powerctrl		--with-kde
cat {kcmlowbatcrit,kcmlowbatwarn,laptop,powerctrl}.lang >> klaptopdaemon.lang
%find_lang ktimer		--with-kde
%find_lang ksim			--with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%{_includedir}/*
%{_libdir}/libkcmlaptop.so
%{_libdir}/libkmilo.so
%{_libdir}/libksimcore.so

%files ark -f ark.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ark
%{_libdir}/ark.la
%attr(755,root,root) %{_libdir}/ark.so
%{_libdir}/kde3/libarkpart.la
%attr(755,root,root) %{_libdir}/kde3/libarkpart.so
%{_datadir}/apps/ark
%{_datadir}/apps/konqueror/servicemenus/arkservicemenu.desktop
%{_datadir}/services/ark_part.desktop
%{_desktopdir}/ark.desktop
%{_pixmapsdir}/*/*/apps/ark.*

%files kcalc -f kcalc.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kcalc
%{_libdir}/kcalc.la
%attr(755,root,root) %{_libdir}/kcalc.so
%{_desktopdir}/kcalc.desktop
%{_pixmapsdir}/*/*/apps/kcalc.*

%files kcharselect -f kcharselect.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kcharselect
%{_libdir}/kde3/kcharselect_panelapplet.la
%attr(755,root,root) %{_libdir}/kde3/kcharselect_panelapplet.so
%{_datadir}/apps/kicker/applets/kcharselectapplet.desktop
%{_desktopdir}/KCharSelect.desktop
%{_pixmapsdir}/*/*/apps/kcharselect.*

%files kdepasswd
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kdepasswd
%{_desktopdir}/kdepasswd.desktop

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
%{_applnkdir}/KDE-Settings/Information/kcmdf.desktop
%{_desktopdir}/kdf.desktop
%{_desktopdir}/kwikdisk.desktop
%{_pixmapsdir}/*/*/apps/kcmdf.*
%{_pixmapsdir}/*/*/apps/kdf.*
%{_pixmapsdir}/*/*/apps/kwikdisk.*

%files kedit -f kedit.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kedit
%{_libdir}/kedit.la
%attr(755,root,root) %{_libdir}/kedit.so
%{_datadir}/apps/kedit
%{_desktopdir}/KEdit.desktop
%{_pixmapsdir}/*/*/apps/kedit.*

%files kfloppy -f kfloppy.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kfloppy
%{_desktopdir}/KFloppy.desktop
%{_pixmapsdir}/*/*/apps/kfloppy.*

%files kgpg
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kgpg
%{_datadir}/apps/kgpg
%{_datadir}/apps/konqueror/servicemenus/encryptfile.desktop
%{_datadir}/autostart/kgpg.desktop
%{_desktopdir}/kgpg.desktop
%{_pixmapsdir}/*/*/apps/kgpg.png

%files khexedit -f khexedit.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/khexedit
%{_datadir}/apps/khexedit
%{_desktopdir}/khexedit.desktop
%{_pixmapsdir}/*/*/apps/khexedit.*

%files kjots -f kjots.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kjots
%{_datadir}/apps/kjots
%{_desktopdir}/Kjots.desktop
%{_pixmapsdir}/*/*/apps/kjots.*

%files kmilo
%defattr(644,root,root,755)
%{_libdir}/libkmilo.la
%attr(755,root,root) %{_libdir}/libkmilo.so.*
%{_libdir}/kde3/kded_kmilod.la
%attr(755,root,root) %{_libdir}/kde3/kded_kmilod.so
%{_datadir}/services/kded/kmilod.desktop
%{_datadir}/servicetypes/kmilo

%files klaptopdaemon -f klaptopdaemon.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/klaptop*
%{_libdir}/libkcmlaptop.la
%attr(755,root,root) %{_libdir}/libkcmlaptop.so.*
%{_libdir}/kde3/kded_klaptopdaemon.la
%attr(755,root,root) %{_libdir}/kde3/kded_klaptopdaemon.so
%{_libdir}/kde3/kcm_laptop.la
%attr(755,root,root) %{_libdir}/kde3/kcm_laptop.so
%{_datadir}/apps/klaptopdaemon
%{_datadir}/services/kded/klaptopdaemon.desktop
%{_applnkdir}/KDE-Settings/Information/pcmcia.desktop
%{_applnkdir}/KDE-Settings/PowerControl/*.desktop
%{_pixmapsdir}/*/*/*/*laptop*

%files kregexpeditor -f KRegExpEditor.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kregexpeditor
%{_libdir}/kde3/libkregexpeditorgui.la
%attr(755,root,root) %{_libdir}/kde3/libkregexpeditorgui.so
%{_datadir}/apps/kregexpeditor
%{_datadir}/services/kregexpeditorgui.desktop
%{_desktopdir}/kregexpeditor.desktop

%files ksim -f ksim.lang
%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/ksim
#%{_libdir}/ksim.la
#%attr(755,root,root) %{_libdir}/ksim.so
%{_libdir}/libksimcore.la
%attr(755,root,root) %{_libdir}/libksimcore.so.*
%{_libdir}/kde3/ksim*.la
%attr(755,root,root) %{_libdir}/kde3/ksim*.so
%{_datadir}/apps/kicker/extensions/ksim.desktop
%{_datadir}/apps/ksim
%{_datadir}/config/ksim_panelextensionrc
%{_desktopdir}/ksim.desktop
%{_pixmapsdir}/*/*/apps/ksim*.png
%{_pixmapsdir}/*/*/devices/ksim*.png

%files ktimer -f ktimer.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ktimer
%{_desktopdir}/ktimer.desktop

%files userinfo
%defattr(644,root,root,755)
%{_libdir}/kde3/kcm_userinfo.la
%attr(755,root,root) %{_libdir}/kde3/kcm_userinfo.so
%{_datadir}/apps/userinfo
%{_applnkdir}/KDE-Settings/System/userinfo.desktop
