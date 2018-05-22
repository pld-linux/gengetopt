Summary:	C code generator that generates command line options parsers
Summary(pl.UTF-8):	Generator kodu C generujący analizatory opcji linii poleceń
Name:		gengetopt
Version:	2.22.6
Release:	1
License:	GPL v3+
Group:		Development/Tools
Source0:	http://ftp.gnu.org/gnu/gengetopt/%{name}-%{version}.tar.gz
# Source0-md5:	29749a48dda69277ab969c510597a14e
Patch0:		%{name}-info.patch
Patch1:		%{name}-am.patch
URL:		http://www.gnu.org/software/gengetopt/
BuildRequires:	autoconf >= 2.58
BuildRequires:	automake
BuildRequires:	help2man
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gengetopt generates a C function that uses getopt_long function to
parse the command line options, to validate them and fills a struct.

%description -l pl.UTF-8
Gengetopt jest to narzędzie generujące kod w języku C, wykorzystujący
funkcję getopt_long do analizy opcji linii poleceń, sprawdzania ich
poprawności i umieszczania ich w strukturze.

%package examples
Summary:	gengetopt examples
Summary(pl.UTF-8):	Przykłady do gengetopt
Group:		Documentation
Requires:	%{name} = %{version}-%{release}

%description examples
Gengetopt examples.

%description examples -l pl.UTF-8
Przykłady do gengetopt.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4 -I gl/m4
%{__autoconf}
%{__autoheader}
%{__automake} --gnu
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -p doc/*.{c,cc,ggo,h} $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -p doc/README.example $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/gengetopt

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog LICENSE NEWS README THANKS TODO doc/{gengetopt,index}.html
%attr(755,root,root) %{_bindir}/gengetopt
%{_mandir}/man1/gengetopt.1*
%{_infodir}/gengetopt.info*
%{_datadir}/%{name}

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
