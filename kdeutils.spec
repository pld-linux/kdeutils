Summary:     K Desktop Environment - utilities
Summary(pl): K Desktop Environment - narzêdzia
Name:        kdeutils
Version:     1.0
Release:     7
Source:      ftp://ftp.kde.org/pub/kde/stable/%{version}/distribution/tar/generic/source/%{name}-%{version}.tar.gz
Group:       X11/KDE/Utils
Copyright:   GPL
Requires:    qt >= 1.40, kdelibs = %{version}
Vendor:      The KDE Team
BuildRoot:   /tmp/%{name}-%{version}-root

%description
KDE utilities.
Package includes:
  KArm - time tracker
  KCalc - calculator
  KEdit - text editor
  KFloppy - floppy formating tool
  KHexEdit - HEX file editor
  KJots - note taker
  KLJetTool - tool for LaserJet priter users
  KNotes - notes
  KZip - compressed archives management program

%description -l pl
Narzêdzia KDE.
Pakiet zawiera:
  KArm
  KCalc - kalkulator
  KEdit - edytor tekstu
  KFloppy - narzêdzie do formatowania dyskietek
  KHexdit - edytor plików
  KJots - notatnik
  KLJetTool - narzêdzie dla u¿ytkowników drukarek LaserJet
  KNotes - inny notatnik
  KZip

%package -n karm
Summary:     KDE Time Tracker
Summary(pl): Time Tracker dla KDE
Group:       X11/KDE/Utils
Requires:    qt >= 1.40, kdelibs = %{version}

%description -n karm
KArm is a time tracker for busy people who need
to keep track of the amount of time they spend
on various tasks.

%description -l pl -n karm
Narzêdzie pozwalaj±ce ustaliæ ile czasu siê spêdzi³o robi±c ró¿ne rzeczy.

%package -n kcalc
Summary:     KDE Calculator	
Summary(pl): Kalkulator KDE
Group:       X11/KDE/Utils
Requires:    qt >= 1.40, kdelibs = %{version}

%description -n kcalc
Calculator for KDE.

%description -l pl -n kcalc
Kalkulator dla KDE.

%package -n kedit
Summary:     KDE Text Editor	
Summary(pl): Edytor tekstu dla KDE
Group:       X11/KDE/Utils
Requires:    qt >= 1.40, kdelibs = %{version}

%description -n kedit
Simple text editor for KDE.

%description -l pl -n kcalc
Prosty edytor tekstu dla KDE.

%package -n kfloppy
Summary:     KDE Floppy Formater	
Summary(pl): Formatowanie dyskietek z KDE
Group:       X11/KDE/Utils
Requires:    qt >= 1.40, kdelibs = %{version}

%description -n kfloppy
KFloppy formats disks and puts a DOS or ext2fs filesystem on them.

%description -l pl -n kfloppy
KFloppy formatuje dyskietki i zak³ada na nich system pliku DOS lub ext2.

%package -n khexdit
Summary:     KDE Hex Editor	
Summary(pl): Edytor szesnastkowy KDE
Group:       X11/KDE/Utils
Requires:    qt >= 1.40, kdelibs = %{version}

%description -n khexdit
Hex Editor is a small and simple viewer for binary files.

%description -l pl -n khexdit
Prosta przegl±darka do plików binarnych.

%package -n kjots
Summary:     KDE Note taker
Summary(pl): Notatnik KDE
Group:       X11/KDE/Utils
Requires:    qt >= 1.40, kdelibs = %{version}

%description -n kjots
kjots is a small note taker program. Name and idea are taken from
the jots program included in the tkgoodstuff package.

%description -l pl -n kjots
KJots to ma³y program do zbierania notatek.

%package -n kljettool
Summary:     KDE LaserJet Tool	
Summary(pl): Konfigurator drukarek LaserJet dla KDE
Group:       X11/KDE/Utils
Requires:    qt >= 1.40, kdelibs = %{version}

%description -n kljettool
KLJetTool is a program that lets you adjust your Hewlett Packard
Laserjet operating parameters. Some of Hewlet Packards printers such
as the 5L or the 6L do no longer have a hardware control panel and the
printer is controlled completely by software. However this software is
often available only for the Windows platform. KLJetTool seeks to fill
the need for such software on the Unix platform. It should work with
any printer that understands Hewlet Packarts PJL ( Printer Job
Language). However some features may have no effect on your particular
model.
			   
%description -l pl -n kljettool
KLJetToll to program umo¿liwiaj±cy konfiguracjê drukarek
Hewlett Packard LaserJet.

%package -n knotes 
Summary:     KDE Notes
Summary(pl): Notes KDE
Group:       X11/KDE/Utils
Requires:    qt >= 1.40, kdelibs = %{version}

%description -n knotes
KNotes is ment to be a really usable and good looking notes
application for the KDE project.

%description -l pl -n knotes
KNotes to program umo¿liwiaj±cy spisywanie sobie notatek i trzymanie ich na
ekranie komputera.

%package -n kzip
Summary:     KDE Archive Handling Tool
Summary(pl): Program obs³ugi archiwów KDE
Group:       X11/KDE/Utils
Requires:    qt >= 1.40, kdelibs = %{version}

%description -n kzip
A tool for managing compressed archives.

%description -l pl -n kzip
Narzêdzi do obs³ugi skompresowanych plików.

%prep
%setup -q

%build
export KDEDIR=/usr/X11R6
CXXFLAGS="$RPM_OPT_FLAGS -Wall" CFLAGS="$RPM_OPT_FLAGS -Wall" \
CCOPTS="$RPM_OPT_FLAGS -Wall" \
./configure %{_target} \
	--prefix=$KDEDIR \
 	--with-install-root=$RPM_BUILD_ROOT \
 	--with-pam="yes"
make KDEDIR=$KDEDIR

%install
rm -rf $RPM_BUILD_ROOT
export KDEDIR=/usr/X11R6
make RUN_KAPPFINDER=no prefix=$RPM_BUILD_ROOT$KDEDIR install

# create wmconfig files
install -d $RPM_BUILD_ROOT/etc/X11/wmconfig
DIR=$PWD
cd $RPM_BUILD_ROOT/etc/X11/kde/applnk
for kdelnk in `find . -name "*.kdelnk"` ; do
  PKG=kde`basename $kdelnk|sed -e "s/\.kdelnk$//"`;
  SECT=`dirname $kdelnk|sed -e "s/^\.\/*//"`;
  kdelnk2wmconfig $PKG $kdelnk $RPM_BUILD_ROOT/etc/X11/wmconfig/$PKG KDE/$SECT pl
done
cd $DIR

%clean
rm -rf $RPM_BUILD_ROOT

#################################################
#             KARM
#################################################

%files -n karm
%defattr(644,root,root,755)
%config(missingok) /etc/X11/kde/applnk/Utilities/KArm.kdelnk
%config(missingok) /etc/X11/wmconfig/kdeKArm
%attr(755,root,root) /usr/X11R6/bin/karm
%lang(en) /usr/X11R6/share/kde/doc/HTML/en/karm
/usr/X11R6/share/kde/icons/karm.xpm
/usr/X11R6/share/kde/icons/mini/karm.xpm
%lang(ca) /usr/X11R6/share/locale/ca/LC_MESSAGES/karm.mo
%lang(cs) /usr/X11R6/share/locale/cs/LC_MESSAGES/karm.mo
%lang(da) /usr/X11R6/share/locale/da/LC_MESSAGES/karm.mo
%lang(de) /usr/X11R6/share/locale/de/LC_MESSAGES/karm.mo
%lang(es) /usr/X11R6/share/locale/es/LC_MESSAGES/karm.mo
%lang(fi) /usr/X11R6/share/locale/fi/LC_MESSAGES/karm.mo
%lang(fr) /usr/X11R6/share/locale/fr/LC_MESSAGES/karm.mo
%lang(hr) /usr/X11R6/share/locale/hr/LC_MESSAGES/karm.mo
%lang(it) /usr/X11R6/share/locale/it/LC_MESSAGES/karm.mo
%lang(nl) /usr/X11R6/share/locale/nl/LC_MESSAGES/karm.mo
%lang(no) /usr/X11R6/share/locale/no/LC_MESSAGES/karm.mo
%lang(pl) /usr/X11R6/share/locale/pl/LC_MESSAGES/karm.mo
%lang(pt) /usr/X11R6/share/locale/pt*/LC_MESSAGES/karm.mo
%lang(ro) /usr/X11R6/share/locale/ro/LC_MESSAGES/karm.mo
%lang(sk) /usr/X11R6/share/locale/sk/LC_MESSAGES/karm.mo
%lang(zh) /usr/X11R6/share/locale/zh*/LC_MESSAGES/karm.mo

#################################################
#             KCALC
#################################################

%files -n kcalc
%defattr(644,root,root,755)
%config(missingok) /etc/X11/kde/applnk/Utilities/kcalc.kdelnk
%config(missingok) /etc/X11/wmconfig/kdekcalc
%attr(755,root,root) /usr/X11R6/bin/kcalc
%lang(en) /usr/X11R6/share/kde/doc/HTML/en/kcalc
%lang(de) /usr/X11R6/share/kde/doc/HTML/de/kcalc
/usr/X11R6/share/kde/icons/mini/kcalc.xpm
/usr/X11R6/share/kde/icons/kcalc.xpm
/usr/X11R6/share/kde/apps/kcalc
%lang(ca) /usr/X11R6/share/locale/ca/LC_MESSAGES/kcalc.mo
%lang(cs) /usr/X11R6/share/locale/cs/LC_MESSAGES/kcalc.mo
%lang(de) /usr/X11R6/share/locale/de/LC_MESSAGES/kcalc.mo
%lang(el) /usr/X11R6/share/locale/el/LC_MESSAGES/kcalc.mo
%lang(es) /usr/X11R6/share/locale/es/LC_MESSAGES/kcalc.mo
%lang(fi) /usr/X11R6/share/locale/fi/LC_MESSAGES/kcalc.mo
%lang(hr) /usr/X11R6/share/locale/hr/LC_MESSAGES/kcalc.mo
%lang(it) /usr/X11R6/share/locale/it/LC_MESSAGES/kcalc.mo
%lang(nl) /usr/X11R6/share/locale/nl/LC_MESSAGES/kcalc.mo
%lang(no) /usr/X11R6/share/locale/no/LC_MESSAGES/kcalc.mo
%lang(pl) /usr/X11R6/share/locale/pl/LC_MESSAGES/kcalc.mo
%lang(pt) /usr/X11R6/share/locale/pt*/LC_MESSAGES/kcalc.mo
%lang(ro) /usr/X11R6/share/locale/ro/LC_MESSAGES/kcalc.mo
%lang(sk) /usr/X11R6/share/locale/sk/LC_MESSAGES/kcalc.mo
%lang(sv) /usr/X11R6/share/locale/sv/LC_MESSAGES/kcalc.mo
%lang(zh) /usr/X11R6/share/locale/zh*/LC_MESSAGES/kcalc.mo

#################################################
#             KEDIT
#################################################

%files -n kedit
%defattr(644,root,root,755)
%config(missingok) /etc/X11/kde/applnk/Applications/KEdit.kdelnk
%config(missingok) /etc/X11/wmconfig/kdeKEdit
%attr(755,root,root) /usr/X11R6/bin/kedit
%lang(en) /usr/X11R6/share/kde/doc/HTML/en/kedit
/usr/X11R6/share/kde/icons/mini/kedit.xpm
/usr/X11R6/share/kde/icons/kedit.xpm
/usr/X11R6/share/kde/apps/kedit/
%lang(ca) /usr/X11R6/share/locale/ca/LC_MESSAGES/kedit.mo
%lang(cs) /usr/X11R6/share/locale/cs/LC_MESSAGES/kedit.mo
%lang(da) /usr/X11R6/share/locale/da/LC_MESSAGES/kedit.mo
%lang(de) /usr/X11R6/share/locale/de/LC_MESSAGES/kedit.mo
%lang(el) /usr/X11R6/share/locale/el/LC_MESSAGES/kedit.mo
%lang(es) /usr/X11R6/share/locale/es/LC_MESSAGES/kedit.mo
%lang(fi) /usr/X11R6/share/locale/fi/LC_MESSAGES/kedit.mo
%lang(fr) /usr/X11R6/share/locale/fr/LC_MESSAGES/kedit.mo
%lang(hr) /usr/X11R6/share/locale/hr/LC_MESSAGES/kedit.mo
%lang(hu) /usr/X11R6/share/locale/hu/LC_MESSAGES/kedit.mo
%lang(it) /usr/X11R6/share/locale/it/LC_MESSAGES/kedit.mo
%lang(mk) /usr/X11R6/share/locale/mk/LC_MESSAGES/kedit.mo
%lang(nl) /usr/X11R6/share/locale/nl/LC_MESSAGES/kedit.mo
%lang(no) /usr/X11R6/share/locale/no/LC_MESSAGES/kedit.mo
%lang(pl) /usr/X11R6/share/locale/pl/LC_MESSAGES/kedit.mo
%lang(pt) /usr/X11R6/share/locale/pt*/LC_MESSAGES/kedit.mo
%lang(sk) /usr/X11R6/share/locale/sk/LC_MESSAGES/kedit.mo
%lang(sv) /usr/X11R6/share/locale/sv/LC_MESSAGES/kedit.mo
%lang(zh) /usr/X11R6/share/locale/zh_*/LC_MESSAGES/kedit.mo

#################################################
#             KFLOPPY
#################################################

%files -n kfloppy
%defattr(644,root,root,755)
%config(missingok) /etc/X11/kde/applnk/Utilities/KFloppy.kdelnk
%config(missingok) /etc/X11/wmconfig/kdeKFloppy
%attr(755,root,root) /usr/X11R6/bin/kfloppy
%attr(755,root,root) /usr/X11R6/bin/kmkdosfs
%attr(755,root,root) /usr/X11R6/bin/kfdformat
%attr(755,root,root) /usr/X11R6/bin/kmke2fs
%lang(en) /usr/X11R6/share/kde/doc/HTML/en/kfloppy
/usr/X11R6/share/kde/icons/mini/kfloppy.xpm
/usr/X11R6/share/kde/icons/kfloppy.xpm
/usr/X11R6/share/kde/apps/kfloppy
%lang(ca) /usr/X11R6/share/locale/ca/LC_MESSAGES/kfloppy.mo
%lang(cs) /usr/X11R6/share/locale/cs/LC_MESSAGES/kfloppy.mo
%lang(de) /usr/X11R6/share/locale/de/LC_MESSAGES/kfloppy.mo
%lang(es) /usr/X11R6/share/locale/es/LC_MESSAGES/kfloppy.mo
%lang(fi) /usr/X11R6/share/locale/fi/LC_MESSAGES/kfloppy.mo
%lang(fr) /usr/X11R6/share/locale/fr/LC_MESSAGES/kfloppy.mo
%lang(hr) /usr/X11R6/share/locale/hr/LC_MESSAGES/kfloppy.mo
%lang(nl) /usr/X11R6/share/locale/nl/LC_MESSAGES/kfloppy.mo
%lang(no) /usr/X11R6/share/locale/no/LC_MESSAGES/kfloppy.mo
%lang(pl) /usr/X11R6/share/locale/pl/LC_MESSAGES/kfloppy.mo
%lang(pt) /usr/X11R6/share/locale/pt*/LC_MESSAGES/kfloppy.mo
%lang(ro) /usr/X11R6/share/locale/ro/LC_MESSAGES/kfloppy.mo
%lang(sk) /usr/X11R6/share/locale/sk/LC_MESSAGES/kfloppy.mo
%lang(sv) /usr/X11R6/share/locale/sv/LC_MESSAGES/kfloppy.mo
%lang(zh) /usr/X11R6/share/locale/zh*/LC_MESSAGES/kfloppy.mo

#################################################
#             KHEXDIT
#################################################

%files -n khexdit
%defattr(644,root,root,755)
%config(missingok) /etc/X11/kde/applnk/Utilities/khexdit.kdelnk
%config(missingok) /etc/X11/wmconfig/kdekhexdit
%attr(755,root,root) /usr/X11R6/bin/khexdit
%lang(en) /usr/X11R6/share/kde/doc/HTML/en/khexdit
%lang(it) /usr/X11R6/share/kde/doc/HTML/it/khexdit
/usr/X11R6/share/kde/icons/mini/khexdit.xpm
/usr/X11R6/share/kde/icons/khexdit.xpm
%lang(ca) /usr/X11R6/share/locale/ca/LC_MESSAGES/khexdit.mo
%lang(cs) /usr/X11R6/share/locale/cs/LC_MESSAGES/khexdit.mo
%lang(da) /usr/X11R6/share/locale/da/LC_MESSAGES/khexdit.mo
%lang(de) /usr/X11R6/share/locale/de/LC_MESSAGES/khexdit.mo
%lang(el) /usr/X11R6/share/locale/el/LC_MESSAGES/khexdit.mo
%lang(es) /usr/X11R6/share/locale/es/LC_MESSAGES/khexdit.mo
%lang(fi) /usr/X11R6/share/locale/fi/LC_MESSAGES/khexdit.mo
%lang(fr) /usr/X11R6/share/locale/fr/LC_MESSAGES/khexdit.mo
%lang(hr) /usr/X11R6/share/locale/hr/LC_MESSAGES/khexdit.mo
%lang(hu) /usr/X11R6/share/locale/hu/LC_MESSAGES/khexdit.mo
%lang(it) /usr/X11R6/share/locale/it/LC_MESSAGES/khexdit.mo
%lang(mk) /usr/X11R6/share/locale/mk/LC_MESSAGES/khexdit.mo
%lang(nl) /usr/X11R6/share/locale/nl/LC_MESSAGES/khexdit.mo
%lang(no) /usr/X11R6/share/locale/no/LC_MESSAGES/khexdit.mo
%lang(pl) /usr/X11R6/share/locale/pl/LC_MESSAGES/khexdit.mo
%lang(pt) /usr/X11R6/share/locale/pt*/LC_MESSAGES/khexdit.mo
%lang(ro) /usr/X11R6/share/locale/ro/LC_MESSAGES/khexdit.mo
%lang(ru) /usr/X11R6/share/locale/ru/LC_MESSAGES/khexdit.mo
%lang(sk) /usr/X11R6/share/locale/sk/LC_MESSAGES/khexdit.mo
%lang(sv) /usr/X11R6/share/locale/sv/LC_MESSAGES/khexdit.mo
%lang(zh) /usr/X11R6/share/locale/zh*/LC_MESSAGES/khexdit.mo

#################################################
#             KJOTS
#################################################

%files -n kjots
%defattr(644,root,root,755)
%config(missingok) /etc/X11/kde/applnk/Utilities/Kjots.kdelnk
%config(missingok) /etc/X11/wmconfig/kdeKjots
%attr(755,root,root) /usr/X11R6/bin/kjots
%lang(en) /usr/X11R6/share/kde/doc/HTML/en/kjots
/usr/X11R6/share/kde/icons/mini/kjots.xpm
/usr/X11R6/share/kde/icons/kjots.xpm
/usr/X11R6/share/kde/apps/kjots

#################################################
#             KLJETTOOL
#################################################

%files -n kljettool
%defattr(644,root,root,755)
%config(missingok) /etc/X11/kde/applnk/Utilities/KLJetTool.kdelnk
%config(missingok) /etc/X11/wmconfig/kdeKLJetTool
%attr(755,root,root) /usr/X11R6/bin/kljettool
%lang(en) /usr/X11R6/share/kde/doc/HTML/en/kljettool
/usr/X11R6/share/kde/icons/mini/kljettool.xpm
/usr/X11R6/share/kde/icons/kljetlogo.xpm
%lang(ca) /usr/X11R6/share/locale/ca/LC_MESSAGES/kljettool.mo
%lang(cs) /usr/X11R6/share/locale/cs/LC_MESSAGES/kljettool.mo
%lang(de) /usr/X11R6/share/locale/de/LC_MESSAGES/kljettool.mo
%lang(fi) /usr/X11R6/share/locale/fi/LC_MESSAGES/kljettool.mo
%lang(hr) /usr/X11R6/share/locale/hr/LC_MESSAGES/kljettool.mo
%lang(nl) /usr/X11R6/share/locale/nl/LC_MESSAGES/kljettool.mo
%lang(no) /usr/X11R6/share/locale/no/LC_MESSAGES/kljettool.mo
%lang(pl) /usr/X11R6/share/locale/pl/LC_MESSAGES/kljettool.mo
%lang(pt) /usr/X11R6/share/locale/pt*/LC_MESSAGES/kljettool.mo
%lang(ro) /usr/X11R6/share/locale/ro/LC_MESSAGES/kljettool.mo
%lang(sk) /usr/X11R6/share/locale/sk/LC_MESSAGES/kljettool.mo
%lang(zh) /usr/X11R6/share/locale/zh*/LC_MESSAGES/kljettool.mo

#################################################
#             KNOTES
#################################################

%files -n knotes
%defattr(644,root,root,755)
%config(missingok) /etc/X11/kde/applnk/Utilities/knotes.kdelnk
%config(missingok) /etc/X11/wmconfig/kdeknotes
%attr(755,root,root) /usr/X11R6/bin/knotes
%lang(en) /usr/X11R6/share/kde/doc/HTML/en/knotes
/usr/X11R6/share/kde/icons/mini/knotes.xpm
/usr/X11R6/share/kde/icons/knotes.xpm
/usr/X11R6/share/kde/apps/knotes/
%lang(ca) /usr/X11R6/share/locale/ca/LC_MESSAGES/knotes.mo
%lang(cs) /usr/X11R6/share/locale/cs/LC_MESSAGES/knotes.mo
%lang(da) /usr/X11R6/share/locale/da/LC_MESSAGES/knotes.mo
%lang(de) /usr/X11R6/share/locale/de/LC_MESSAGES/knotes.mo
%lang(es) /usr/X11R6/share/locale/es/LC_MESSAGES/knotes.mo
%lang(fi) /usr/X11R6/share/locale/fi/LC_MESSAGES/knotes.mo
%lang(fr) /usr/X11R6/share/locale/fr/LC_MESSAGES/knotes.mo
%lang(hr) /usr/X11R6/share/locale/hr/LC_MESSAGES/knotes.mo
%lang(hu) /usr/X11R6/share/locale/hu/LC_MESSAGES/knotes.mo
%lang(it) /usr/X11R6/share/locale/it/LC_MESSAGES/knotes.mo
%lang(nl) /usr/X11R6/share/locale/nl/LC_MESSAGES/knotes.mo
%lang(no) /usr/X11R6/share/locale/no/LC_MESSAGES/knotes.mo
%lang(pl) /usr/X11R6/share/locale/pl/LC_MESSAGES/knotes.mo
%lang(pt) /usr/X11R6/share/locale/pt*/LC_MESSAGES/knotes.mo
%lang(ru) /usr/X11R6/share/locale/ru/LC_MESSAGES/knotes.mo
%lang(sk) /usr/X11R6/share/locale/sk/LC_MESSAGES/knotes.mo
%lang(zh) /usr/X11R6/share/locale/zh*/LC_MESSAGES/knotes.mo

#################################################
#             KZIP
#################################################

%files -n kzip
%defattr(644,root,root,755)
%config(missingok) /etc/X11/kde/applnk/Utilities/kzip.kdelnk
%config(missingok) /etc/X11/wmconfig/kdekzip
%attr(755,root,root) /usr/X11R6/bin/kzip
%lang(en) /usr/X11R6/share/kde/doc/HTML/en/kzip
/usr/X11R6/share/kde/icons/mini/kzip.xpm
/usr/X11R6/share/kde/icons/kzip.xpm
/usr/X11R6/share/kde/toolbar/filedel.xpm
%lang(ca) /usr/X11R6/share/locale/ca/LC_MESSAGES/kzip.mo
%lang(cs) /usr/X11R6/share/locale/cs/LC_MESSAGES/kzip.mo
%lang(da) /usr/X11R6/share/locale/da/LC_MESSAGES/kzip.mo
%lang(de) /usr/X11R6/share/locale/de/LC_MESSAGES/kzip.mo
%lang(es) /usr/X11R6/share/locale/es/LC_MESSAGES/kzip.mo
%lang(fi) /usr/X11R6/share/locale/fi/LC_MESSAGES/kzip.mo
%lang(fr) /usr/X11R6/share/locale/fr/LC_MESSAGES/kzip.mo
%lang(hr) /usr/X11R6/share/locale/hr/LC_MESSAGES/kzip.mo
%lang(hu) /usr/X11R6/share/locale/hu/LC_MESSAGES/kzip.mo
%lang(it) /usr/X11R6/share/locale/it/LC_MESSAGES/kzip.mo
%lang(nl) /usr/X11R6/share/locale/nl/LC_MESSAGES/kzip.mo
%lang(no) /usr/X11R6/share/locale/no/LC_MESSAGES/kzip.mo
%lang(pl) /usr/X11R6/share/locale/pl/LC_MESSAGES/kzip.mo
%lang(pt) /usr/X11R6/share/locale/pt*/LC_MESSAGES/kzip.mo
%lang(ro) /usr/X11R6/share/locale/ro/LC_MESSAGES/kzip.mo
%lang(ru) /usr/X11R6/share/locale/ru/LC_MESSAGES/kzip.mo
%lang(sk) /usr/X11R6/share/locale/sk/LC_MESSAGES/kzip.mo
%lang(zh) /usr/X11R6/share/locale/zh*/LC_MESSAGES/kzip.mo

%changelog
* Wed Dec  8 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.0-7]
- recompiled against libstdc++.so.2.9.

* Sun Oct 18 1998 Jacek Konieczny <jajcus@zeus.polsl.gliwice.pl>
  [1.0-4]
- created new spec based on kdebase.spec
