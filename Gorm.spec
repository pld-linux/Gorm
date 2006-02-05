Summary:	Graphic Object Relationship modeler
Summary(pl):	Graficzny modeler zale¿no¶ci obiektów
Name:		Gorm
Version:	1.0.4
Release:	1
License:	GPL
Group:		X11/Development/Tools
Source0:	ftp://ftp.gnustep.org/pub/gnustep/dev-apps/%{name}-%{version}.tar.gz
# Source0-md5:	fcc6c0755c10a3f39b283ae029f2878f
URL:		http://www.gnustep.org/experience/Gorm.html
BuildRequires:	gnustep-base-devel >= 0.11.2
BuildRequires:	gnustep-gui-devel >= 0.10.2
Requires:	gnustep-base >= 0.11.2
Requires:	gnustep-gui >= 0.10.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _prefix         /usr/%{_lib}/GNUstep

%define		libcombo	gnu-gnu-gnu
%define		gsos		linux-gnu
%ifarch %{ix86}
%define		gscpu		ix86
%else
# also s/alpha.*/alpha/, but we use only "alpha" arch for now
%define		gscpu		%(echo %{_target_cpu} | sed -e 's/amd64/x86_64/;s/ppc/powerpc/')
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
Requires:	%{name} = %{version}-%{release}
Requires:	gnustep-base-devel >= 0.11.2
Requires:	gnustep-gui-devel >= 0.10.2

%description devel
Header files for Gorm library.

%description devel -l pl
Pliki nag³ówkowe biblioteki Gorma.

%prep
%setup -q

%build
export GNUSTEP_MAKEFILES=%{_prefix}/System/Library/Makefiles
export GNUSTEP_TARGET_DIR=%{gscpu}/linux-gnu
%{__make} \
	OPTFLAG="%{rpmcflags}" \
	messages=yes

%install
rm -rf $RPM_BUILD_ROOT
export GNUSTEP_MAKEFILES=%{_prefix}/System/Library/Makefiles
export GNUSTEP_TARGET_DIR=%{gscpu}/linux-gnu

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
%{_prefix}/System/Applications/Gorm.app/Resources/*.plist
%{_prefix}/System/Applications/Gorm.app/Resources/*.tiff
%dir %{_prefix}/System/Applications/Gorm.app/Resources/*.palette
%dir %{_prefix}/System/Applications/Gorm.app/Resources/English.lproj
%{_prefix}/System/Applications/Gorm.app/Resources/English.lproj/*.gorm
%{_prefix}/System/Applications/Gorm.app/Resources/*.palette/Resources
%attr(755,root,root) %{_prefix}/System/Applications/Gorm.app/Resources/*.palette/%{gscpu}
%dir %{_prefix}/System/Applications/Gorm.app/%{gscpu}
%dir %{_prefix}/System/Applications/Gorm.app/%{gscpu}/%{gsos}
%dir %{_prefix}/System/Applications/Gorm.app/%{gscpu}/%{gsos}/%{libcombo}
%attr(755,root,root) %{_prefix}/System/Applications/Gorm.app/%{gscpu}/%{gsos}/%{libcombo}/Gorm
%{_prefix}/System/Applications/Gorm.app/%{gscpu}/%{gsos}/%{libcombo}/*.openapp

%{_prefix}/System/Library/Libraries/%{gscpu}/%{gsos}/%{libcombo}/lib*.so.*

%files devel
%defattr(644,root,root,755)
%{_prefix}/System/Library/Headers/%{libcombo}/GormCore
%{_prefix}/System/Library/Headers/%{libcombo}/GormObjCHeaderParser
%{_prefix}/System/Library/Headers/%{libcombo}/GormPrefs
%{_prefix}/System/Library/Headers/%{libcombo}/InterfaceBuilder
%{_prefix}/System/Library/Libraries/%{gscpu}/%{gsos}/%{libcombo}/lib*.so
