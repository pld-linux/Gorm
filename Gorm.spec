Summary:	Graphic Object Relationship modeler
Summary(pl.UTF-8):   Graficzny modeler zależności obiektów
Name:		Gorm
Version:	1.1.0
Release:	1
License:	GPL
Group:		X11/Development/Tools
Source0:	ftp://ftp.gnustep.org/pub/gnustep/dev-apps/gorm-%{version}.tar.gz
# Source0-md5:	4eef5a043c6c07ca7269add9ee286b38
Patch0:		%{name}-link.patch
URL:		http://www.gnustep.org/experience/Gorm.html
BuildRequires:	gnustep-base-devel >= 1.13.0
BuildRequires:	gnustep-gui-devel >= 0.11.0
Requires:	gnustep-base >= 1.13.0
Requires:	gnustep-gui >= 0.11.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _prefix         /usr/%{_lib}/GNUstep

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
Summary(pl.UTF-8):   Pliki nagłówkowe biblioteki Gorma
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
export GNUSTEP_MAKEFILES=%{_prefix}/System/Library/Makefiles
export GNUSTEP_FLATTENED=yes
%{__make} \
	OPTFLAG="%{rpmcflags}" \
	messages=yes

%install
rm -rf $RPM_BUILD_ROOT
export GNUSTEP_MAKEFILES=%{_prefix}/System/Library/Makefiles
export GNUSTEP_FLATTENED=yes

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
%attr(755,root,root) %{_prefix}/System/Applications/Gorm.app/Resources/*.palette/[0-4]*
%{_prefix}/System/Applications/Gorm.app/library_paths.openapp

%{_prefix}/System/Library/Libraries/libGorm*.so.*

%files devel
%defattr(644,root,root,755)
%{_prefix}/System/Library/Headers/GormCore
%{_prefix}/System/Library/Headers/GormObjCHeaderParser
%{_prefix}/System/Library/Headers/GormPrefs
%{_prefix}/System/Library/Headers/InterfaceBuilder
%{_prefix}/System/Library/Libraries/libGorm*.so
