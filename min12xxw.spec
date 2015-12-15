%define _disable_rebuild_configure 1

Summary:	A printer filter for Minolta 1[234]xx W printers
Name:		min12xxw
Version:	0.0.9
Release:	25
License:	GPLv2
Group:		System/Printing
Url:		http://www.hinterbergen.de/mala/min12xxw/
Source0:	http://www.hinterbergen.de/mala/min12xxw/%{name}-%{version}.tar.gz
Patch0:		min12xxw-0.0.9-format_not_a_string_literal_and_no_format_arguments.diff
BuildRequires:	gettext-devel

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
make install DESTDIR=%{buildroot}

%files
%doc AUTHORS COPYING ChangeLog FAQ NEWS README format.txt
%{_bindir}/esc-m
%{_bindir}/min12xxw
%{_mandir}/man1/*

