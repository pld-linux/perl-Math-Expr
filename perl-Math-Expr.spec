%include	/usr/lib/rpm/macros.perl
Summary:	Math-Expr perl module
Summary(pl):	Modu³ perla Math-Expr
Name:		perl-Math-Expr
Version:	0.4
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Math/Math-Expr-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Math-Expr module parses mathematical expressions.

%description -l pl
Math-Expr analizuje wyra¿enia matematyczne.

%prep
%setup -q -n Math-Expr-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Math/Expr
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,TODO}.gz db

%{perl_sitelib}/Math/Expr.pm
%{perl_sitelib}/Math/Expr
%{perl_sitearch}/auto/Math/Expr

%{_mandir}/man3/*
