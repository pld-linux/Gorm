Summary:	Graphic Object Relationship modeler
Summary(pl):	Graficzny modeler zale¿no¶ci obiektów
Name:		Gorm
Version:	0.6.0
%define snap 20040413
Release:	1.%{snap}.0
License:	GPL
Group:		X11/Development/Tools
#Source0:	ftp://ftp.gnustep.org/pub/gnustep/dev-apps/%{name}-%{version}.tar.gz
Source0:	%{name}-%{snap}.tar.gz
# Source0-md5:	710b464929a8fc5e223ab71e8506ff66
URL:		http://www.gnustep.org/experience/Gorm.html
BuildRequires:	gnustep-gui-devel >= 0.8.9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _prefix         /usr/lib/GNUstep

%define		libcombo	gnu-gnu-gnu
%define		gsos		linux-gnu
%ifarch %{ix86}
%define		gscpu		ix86
%else
# also s/alpha.*/alpha/, but we use only "alpha" arch for now
%define		gscpu		%{_target_cpu}
%endif

%description
Gorm is an acronym for Graphic Object Relationship modeler (or perhaps
GNUstep Object Relationship Modeler). It is a clone of the NeXTstep
`Interface Builder' application for GNUstep.

%description -l pl
Gorm to skrót od Graphic Object Relationship modeler (czyli graficzny
modeler zale¿no¶ci obiektów). Jest to klon NeXTstepowej aplikacji
"Interface Builder" dla GNUstepa.

%package devel
Summary:	Header files for Gorm library
Summary(pl):	Pliki nag³ówkowe biblioteki Gorma
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	gnustep-gui-devel

%description devel
Header files for Gorm library.

%description devel -l pl
Pliki nag³ówkowe biblioteki Gorma.

%prep
%setup -q -n %{name}

%build
. %{_prefix}/System/Library/Makefiles/GNUstep.sh
%{__make} \
	OPTFLAG="%{rpmcflags}" \
	messages=yes

%install
rm -rf $RPM_BUILD_ROOT
. %{_prefix}/System/Library/Makefiles/GNUstep.sh

%{__make} install \
	GNUSTEP_INSTALLATION_DIR=$RPM_BUILD_ROOT%{_prefix}/System

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ANNOUNCE ChangeLog NEWS README TODO

%dir %{_prefix}/System/Applications/Gorm.app
%attr(755,root,root) %{_prefix}/System/Applications/Gorm.app/Gorm
%dir %{_prefix}/System/Applications/Gorm.app/Resources
%{_prefix}/System/Applications/Gorm.app/Resources/*.desktop
%{_prefix}/System/Applications/Gorm.app/Resources/*.gorm
%{_prefix}/System/Applications/Gorm.app/Resources/*.plist
%{_prefix}/System/Applications/Gorm.app/Resources/*.tiff
%dir %{_prefix}/System/Applications/Gorm.app/Resources/*.palette
%{_prefix}/System/Applications/Gorm.app/Resources/*.palette/Resources
%attr(755,root,root) %{_prefix}/System/Applications/Gorm.app/Resources/*.palette/%{gscpu}
%dir %{_prefix}/System/Applications/Gorm.app/%{gscpu}
%dir %{_prefix}/System/Applications/Gorm.app/%{gscpu}/%{gsos}
%dir %{_prefix}/System/Applications/Gorm.app/%{gscpu}/%{gsos}/%{libcombo}
%attr(755,root,root) %{_prefix}/System/Applications/Gorm.app/%{gscpu}/%{gsos}/%{libcombo}/Gorm
%{_prefix}/System/Applications/Gorm.app/%{gscpu}/%{gsos}/%{libcombo}/*.openapp

%dir %{_prefix}/System/Applications/GormTest.app
%attr(755,root,root) %{_prefix}/System/Applications/GormTest.app/GormTest
%{_prefix}/System/Applications/GormTest.app/Resources
%dir %{_prefix}/System/Applications/GormTest.app/%{gscpu}
%dir %{_prefix}/System/Applications/GormTest.app/%{gscpu}/%{gsos}
%dir %{_prefix}/System/Applications/GormTest.app/%{gscpu}/%{gsos}/%{libcombo}
%attr(755,root,root) %{_prefix}/System/Applications/GormTest.app/%{gscpu}/%{gsos}/%{libcombo}/GormTest
%{_prefix}/System/Applications/GormTest.app/%{gscpu}/%{gsos}/%{libcombo}/*.openapp

%{_prefix}/System/Library/Libraries/%{gscpu}/%{gsos}/%{libcombo}/lib*.so.*

%files devel
%defattr(644,root,root,755)
%{_prefix}/System/Library/Headers/%{libcombo}/InterfaceBuilder
%{_prefix}/System/Library/Libraries/%{gscpu}/%{gsos}/%{libcombo}/lib*.so
