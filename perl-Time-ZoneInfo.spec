%define realname    Time-ZoneInfo
%define realversion 0.3
%define version	    0.3.1
%define release     %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Perl extension for returning a list of Time Zones
Source:     http://www.cpan.org/modules/by-module/Time/%{realname}-%{realversion}.tar.gz
Patch:	    Time-ZoneInfo-0.3-geolocalisation.patch
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildArch: noarch

%description
An OO interface to accessing a list of timezones. This is useful if you
want to provide an interface for your user to choose one of the available
time zones.

Version 0.3.1 also gives the geolocalisation for a time zone.

%prep
%setup -q -n %{realname}-%{realversion}
%patch0 -p1 -b .pix

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*

