%include	/usr/lib/rpm/macros.perl
%define	pdir	Math
%define	pnam	Expr
Summary:	Math-Expr perl module
Summary(pl):	Modu³ perla Math-Expr
Name:		perl-Math-Expr
Version:	0.4
Release:	8
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Math-Expr module parses mathematical expressions.

%description -l pl
Math-Expr analizuje wyra¿enia matematyczne.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz db
%{perl_sitelib}/Math/Expr.pm
%{perl_sitelib}/Math/Expr
%{_mandir}/man3/*
