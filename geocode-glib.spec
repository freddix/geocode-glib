Summary:	Geocode Helper library
Name:		geocode-glib
Version:	3.12.0
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://download.gnome.org/sources/geocode-glib/3.12/%{name}-%{version}.tar.xz
# Source0-md5:	a14c9802c63c35d9ae9091053e192517
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	glib-devel >= 1:2.40.0
BuildRequires:	gobject-introspection-devel >= 1.40.0
BuildRequires:	json-glib-devel >= 1.0.0
BuildRequires:	libsoup-devel
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Geocode Helper library.

%package devel
Summary:	Development files for %{name} library
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Development files for %{name} library.

%package apidocs
Summary:	%{name} API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
%{name} API documentation.

%prep
%setup -q

# kill gnome common deps
%{__sed} -i -e 's/GNOME_COMPILE_WARNINGS.*//g'	\
    -i -e 's/GNOME_MAINTAINER_MODE_DEFINES//g'	\
    -i -e 's/GNOME_COMMON_INIT//g'		\
    -i -e 's/GNOME_CXX_WARNINGS.*//g'		\
    -i -e 's/GNOME_DEBUG_CHECK//g' configure.ac

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--disable-static	\
	--disable-silent-rules	\
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %ghost %{_libdir}/libgeocode-glib.so.0
%attr(755,root,root) %{_libdir}/libgeocode-glib.so.*.*.*
%{_libdir}/girepository-1.0/GeocodeGlib-1.0.typelib

%files devel
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_libdir}/libgeocode-glib.so
%{_includedir}/geocode-glib-1.0
%{_datadir}/gir-1.0/GeocodeGlib-1.0.gir
%{_pkgconfigdir}/geocode-glib-1.0.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/geocode-glib-1.0

