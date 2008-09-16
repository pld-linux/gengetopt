#
Summary:	C code generator that generates command line options parsers
Summary(pl.UTF-8):	Generator kodu C generujący paser opcji linii poleceń
Name:		gengetopt
Version:	2.22.1
Release:	0.1
License:	GPL v3+
Group:		Development/Tools
Source0:	http://ftp.gnu.org/gnu/gengetopt/%{name}-%{version}.tar.gz
# Source0-md5:	3877433c69902a26887ad65c1a2d60eb
URL:		http://www.gnu.org/software/gengetopt/
BuildRequires:	autoconf >= 2.58
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gengetopt generates a C function that uses getopt_long function to
parse the command line options, to validate them and fills a struct.

%description -l pl.UTF-8
Gengetopt jest to narzędzie generujące kod w języku C, który służy do
parsowania opcji przekazanych w wierszu poleceń z użyciem biblioteki
getopt. Kod wygenerowany przez gengetopt potrafi obsłużyć zarówno
krótkie opcje, jak i długie - sprawdzić poprawność przekazazych
argumentów i wypełnić odpowiednie struktury.

%package examples
Summary:	gengetopt examples
Summary(pl.UTF-8):	Przykłady gengetopt
Group:		Documentation
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description examples
Gengetopt examples.

%description examples -l pl.UTF-8
Przykładowe pliki dla gengetopt.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I gl/m4
%{__autoconf}
%{__autoheader}
%{__automake} --add-missing --gnu
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_examplesdir}/%{name},%{_datadir}/%{name},%{_infodir},%{_mandir}/man1}

install src/gengetopt $RPM_BUILD_ROOT%{_bindir}/gengetopt
install doc/*.{c,cc,ggo,h} $RPM_BUILD_ROOT%{_examplesdir}/gengetopt
install doc/README.example $RPM_BUILD_ROOT%{_examplesdir}/gengetopt
install src/gnugetopt.h $RPM_BUILD_ROOT%{_datadir}/gengetopt/gnugetopt.h
install src/getopt.c $RPM_BUILD_ROOT%{_datadir}/gengetopt/getopt.c
install src/getopt1.c $RPM_BUILD_ROOT%{_datadir}/gengetopt/getopt1.c
install doc/gengetopt.info $RPM_BUILD_ROOT%{_infodir}/gengetopt.info
install doc/gengetopt.1 $RPM_BUILD_ROOT%{_mandir}/man1/gengetopt.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/gengetopt
%{_mandir}/man1/gengetopt.1*
%{_infodir}/gengetopt.info*
%{_datadir}/%{name}

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}
