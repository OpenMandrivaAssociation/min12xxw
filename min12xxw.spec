Summary:	A printer filter for Minolta 1[234]xx W printers
Name:		min12xxw
Version:	0.0.9
Release:	%mkrel 15
License:	GPL
Group:		System/Printing
URL:		http://www.hinterbergen.de/mala/min12xxw/
Source0:	http://www.hinterbergen.de/mala/min12xxw/%{name}-%{version}.tar.gz
Patch0:		min12xxw-0.0.9-format_not_a_string_literal_and_no_format_arguments.diff
BuildRequires:	gettext-devel
Conflicts:	printer-utils = 2007
Conflicts:	printer-filters = 2007
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
This is min12xxw, a filter to convert pbmraw data such as produced by
ghostscript to the printer language of Minolta 1[234]xx W printers.

%prep

%setup -q
%patch0 -p0 -b .format_not_a_string_literal_and_no_format_arguments
%build

%configure2_5x

%make

%install
rm -rf %{buildroot}

%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog FAQ NEWS README format.txt
%attr(0755,root,root) %{_bindir}/esc-m
%attr(0755,root,root) %{_bindir}/min12xxw
%attr(0644,root,root) %{_mandir}/man1/*


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.0.9-13mdv2011.0
+ Revision: 666427
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.0.9-12mdv2011.0
+ Revision: 606644
- rebuild

* Mon Mar 15 2010 Oden Eriksson <oeriksson@mandriva.com> 0.0.9-11mdv2010.1
+ Revision: 520170
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.0.9-10mdv2010.0
+ Revision: 426128
- rebuild

* Thu Dec 25 2008 Oden Eriksson <oeriksson@mandriva.com> 0.0.9-9mdv2009.1
+ Revision: 319038
- fix build with -Werror=format-security (P0)

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.0.9-7mdv2009.0
+ Revision: 223261
- rebuild

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 0.0.9-6mdv2008.1
+ Revision: 179021
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Aug 30 2007 Oden Eriksson <oeriksson@mandriva.com> 0.0.9-3mdv2008.0
+ Revision: 75345
- fix deps (pixel)

* Thu Aug 16 2007 Oden Eriksson <oeriksson@mandriva.com> 0.0.9-2mdv2008.0
+ Revision: 64164
- use the new System/Printing RPM GROUP

* Sun Aug 12 2007 Oden Eriksson <oeriksson@mandriva.com> 0.0.9-1mdv2008.0
+ Revision: 62288
- Import min12xxw



* Sun Aug 12 2007 Oden Eriksson <oeriksson@mandriva.com> 0.0.9-1mdv2008.0
- initial Mandriva package
