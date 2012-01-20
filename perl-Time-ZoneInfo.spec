%define upstream_name    Time-ZoneInfo
%define upstream_version 0.3

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 4

Summary:    Perl extension for returning a list of Time Zones
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Time/%{upstream_name}-%{upstream_version}.tar.gz
Patch0:	    Time-ZoneInfo-0.3-geolocalisation.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}
BuildArch: noarch

%description
An OO interface to accessing a list of timezones. This is useful if you
want to provide an interface for your user to choose one of the available
time zones.

Version 0.3.1 also gives the geolocalisation for a time zone.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
%patch0 -p1 -b .geo

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*

