%define upstream_name    Time-ZoneInfo
%define upstream_version 0.3

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    10

Summary:    Perl extension for returning a list of Time Zones
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Time/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires: perl-devel
Patch0:	    Time-ZoneInfo-0.3-geolocalisation.patch

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



%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.300.0-6mdv2012.0
+ Revision: 765792
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.300.0-5
+ Revision: 764297
- rebuilt for perl-5.14.x

* Fri Jan 20 2012 Oden Eriksson <oeriksson@mandriva.com> 0.300.0-4
+ Revision: 763114
- rebuild

* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 0.300.0-3
+ Revision: 654335
- rebuild for updated spec-helper

* Tue Jan 12 2010 Jérôme Quelin <jquelin@mandriva.org> 0.300.0-2mdv2011.0
+ Revision: 490199
- bump mkrel
- do *not* update module version in a patch

* Tue Jul 07 2009 Jérôme Quelin <jquelin@mandriva.org> 0.300.0-1mdv2010.0
+ Revision: 393240
- using %%perl_convert_version
- fixed license field

* Sat Apr 11 2009 Funda Wang <fwang@mandriva.org> 0.3.4-2mdv2009.1
+ Revision: 366060
- fix patch num

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.3.4-2mdv2009.0
+ Revision: 224571
- rebuild

* Sat Feb 23 2008 Pixel <pixel@mandriva.com> 0.3.4-1mdv2008.1
+ Revision: 174090
- 0.3.4: fix getting timezone from /etc/sysconfig/clock

* Thu Feb 21 2008 Pixel <pixel@mandriva.com> 0.3.3-1mdv2008.1
+ Revision: 173505
- 0.3.3: get country code from time zone
  (ie really extract all info from /usr/share/zoneinfo/zone.tab)
- 0.3.2: correctly handle error in ->latitude_longitude_sexagesimal

* Tue Feb 19 2008 Pixel <pixel@mandriva.com> 0.3.1-1mdv2008.1
+ Revision: 172993
- import perl-Time-ZoneInfo


* Tue Feb 19 2008 Pixel <pixel@mandriva.com> 0.3.1-1mdv2008.1
- import
- fork upstream version to add geolocalisation
