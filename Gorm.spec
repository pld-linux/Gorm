Summary:	Graphic Object Relationship modeler
Summary(pl.UTF-8):	Graficzny modeler zależności obiektów
Name:		Gorm
Version:	1.2.2
Release:	1
License:	GPL v3+
Group:		X11/Development/Tools
Source0:	ftp://ftp.gnustep.org/pub/gnustep/dev-apps/gorm-%{version}.tar.gz
# Source0-md5:	4ea0658d5fa4fc1e38baa0846d05b1ac
Patch0:		%{name}-link.patch
URL:		http://www.gnustep.org/experience/Gorm.html
BuildRequires:	gnustep-base-devel >= 1.13.0
BuildRequires:	gnustep-gui-devel >= 0.11.0
Requires:	gnustep-base >= 1.13.0
Requires:	gnustep-gui >= 0.11.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gorm is an acronym for Graphic Object Relationship modeler (or perhaps
GNUstep Object Relationship Modeler). It is a clone of the NeXTstep
`Interface Builder' application for GNUstep.

%description -l pl.UTF-8
Gorm to skrót od Graphic Object Relationship modeler (czyli graficzny
modeler zależności obiektów). Jest to klon NeXTstepowej aplikacji
"Interface Builder" dla GNUstepa.

%package devel
Summary:	Header files for Gorm library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Gorma
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gnustep-base-devel >= 1.13.0
Requires:	gnustep-gui-devel >= 0.11.0

%description devel
Header files for Gorm library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Gorma.

%prep
%setup -q -n gorm-%{version}
%patch0 -p1

%build
export GNUSTEP_MAKEFILES=%{_datadir}/GNUstep/Makefiles
export GNUSTEP_FLATTENED=yes
%{__make} \
	OPTFLAG="%{rpmcflags}" \
	messages=yes

%install
rm -rf $RPM_BUILD_ROOT
export GNUSTEP_MAKEFILES=%{_datadir}/GNUstep/Makefiles
export GNUSTEP_FLATTENED=yes

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ANNOUNCE ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/Gorm
%dir %{_libdir}/GNUstep/Applications/Gorm.app
%attr(755,root,root) %{_libdir}/GNUstep/Applications/Gorm.app/Gorm
%dir %{_libdir}/GNUstep/Applications/Gorm.app/Resources
%{_libdir}/GNUstep/Applications/Gorm.app/Resources/*.desktop
%{_libdir}/GNUstep/Applications/Gorm.app/Resources/*.plist
%{_libdir}/GNUstep/Applications/Gorm.app/Resources/*.tiff
%dir %{_libdir}/GNUstep/Applications/Gorm.app/Resources/*.palette
%dir %{_libdir}/GNUstep/Applications/Gorm.app/Resources/English.lproj
%{_libdir}/GNUstep/Applications/Gorm.app/Resources/English.lproj/*.gorm
%{_libdir}/GNUstep/Applications/Gorm.app/Resources/*.palette/Resources
%attr(755,root,root) %{_libdir}/GNUstep/Applications/Gorm.app/Resources/*.palette/[0-4]*
%attr(755,root,root) %{_libdir}/libGorm*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/GormCore
%{_includedir}/GormObjCHeaderParser
%{_includedir}/GormPrefs
%{_includedir}/InterfaceBuilder
%{_libdir}/libGorm*.so
