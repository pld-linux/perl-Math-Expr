%include	/usr/lib/rpm/macros.perl
%define	pdir	Math
%define	pnam	Expr
Summary:	Math::Expr perl module
Summary(pl):	Modu³ perla Math::Expr
Name:		perl-Math-Expr
Version:	0.4
Release:	9
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2c4f7eb097bca918f4748f7843bca02b
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Math::Expr module parses mathematical expressions.

%description -l pl
Math::Expr analizuje wyra¿enia matematyczne.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO db
%{perl_vendorlib}/Math/Expr.pm
%{perl_vendorlib}/Math/Expr
%{_mandir}/man3/*
