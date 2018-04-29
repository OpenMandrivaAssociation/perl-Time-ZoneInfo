%define modname	Time-ZoneInfo
%define modver	0.3

Summary:	Perl extension for returning a list of Time Zones
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	24
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Time/%{modname}-%{modver}.tar.gz
Patch0:		Time-ZoneInfo-0.3-geolocalisation.patch
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires:	perl(DateTime::TimeZone)
BuildRequires:	perl(namespace::clean)
BuildRequires:	perl(Test)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Package::Stash)
BuildRequires:	timezone
Requires:	timezone

%description
An OO interface to accessing a list of timezones. This is useful if you
want to provide an interface for your user to choose one of the available
time zones.

Version 0.3.1 also gives the geolocalisation for a time zone.

%prep
%setup -qn %{modname}-%{modver}
%apply_patches

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

