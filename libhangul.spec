#
# Conditional build:
%bcond_without	static_libs	# don't build static libraries
%bcond_without	tests		# don't perform "make check"
#
Summary:	Hangul input library
Summary(pl.UTF-8):	Biblioteka wprowadzania znaków Hangul
Name:		libhangul
Version:	0.1.0
Release:	1
License:	LGPL v2+
Group:		Libraries
#Source0Download: http://code.google.com/p/libhangul/downloads/list
Source0:	http://libhangul.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	e9cf109772cc5fbc79f5de503ea7550a
URL:		http://kldp.net/projects/hangul/
BuildRequires:	check-devel
BuildRequires:	gettext-devel >= 0.18
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libhangul provides common features for Hangul input method programs.

%description -l pl.UTF-8
libhangul udostępnia ogólne funkcje dla programów wykorzystujących
metodę wprowadzania znaków Hangul

%package devel
Summary:	Header files for libhangul library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libhangul
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libhangul library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libhangul.

%package static
Summary:	Static libhangul library
Summary(pl.UTF-8):	Statyczna biblioteka libhangul
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libhangul library.

%description static -l pl.UTF-8
Statyczna biblioteka libhangul.

%package apidocs
Summary:	libhangul API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki libhangul
Group:		Documentation

%description apidocs
API and internal documentation for libhangul library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki libhangul.

%prep
%setup -q

%build
%configure \
	%{!?with_static_libs:--disable-static}
%{__make}

%if %{with tests}
%{__make} -C test check
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/hangul
%attr(755,root,root) %{_libdir}/libhangul.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libhangul.so.1
%{_datadir}/%{name}

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libhangul.so
%{_includedir}/hangul-1.0
%{_pkgconfigdir}/libhangul.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libhangul.a
%endif
