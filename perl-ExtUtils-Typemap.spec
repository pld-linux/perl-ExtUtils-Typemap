#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	ExtUtils
%define		pnam	Typemap
%include	/usr/lib/rpm/macros.perl
Summary:	ExtUtils::Typemap - Read/Write/Modify Perl/XS typemap files
Name:		perl-ExtUtils-Typemap
Version:	1.00
Release:	0.1
License:	Perl
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/ExtUtils/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a7175a06e27939a83b1b781e91c13ad0
URL:		http://search.cpan.org/dist/ExtUtils-Typemap/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module exists merely as a compatibility wrapper around
ExtUtils::Typemaps. In a nutshell, ExtUtils::Typemap was renamed to
ExtUtils::Typemaps because the Typemap directory in lib/ could collide
with the typemap file on case-insensitive file systems.

The ExtUtils::Typemaps module is part of the ExtUtils::ParseXS
distribution and ships with the standard library of perl starting with
perl version 5.16.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/ExtUtils/*.pm
%{perl_vendorlib}/ExtUtils/Typemap
%{_mandir}/man3/*
