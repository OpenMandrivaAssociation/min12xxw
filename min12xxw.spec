Summary:	A printer filter for Minolta 1[234]xx W printers
Name:		min12xxw
Version:	0.0.9
Release:	%mkrel 13
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
