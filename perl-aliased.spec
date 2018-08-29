#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-aliased
Version  : 0.34
Release  : 1
URL      : https://cpan.metacpan.org/authors/id/E/ET/ETHER/aliased-0.34.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/E/ET/ETHER/aliased-0.34.tar.gz
Summary  : 'Use shorter versions of class names.'
Group    : Development/Tools
License  : Artistic-1.0-Perl
BuildRequires : buildreq-cpan
BuildRequires : perl(Module::Build::Tiny)

%description
This archive contains the distribution aliased,
version 0.34:
Use shorter versions of class names.

%package dev
Summary: dev components for the perl-aliased package.
Group: Development
Provides: perl-aliased-devel

%description dev
dev components for the perl-aliased package.


%prep
%setup -q -n aliased-0.34

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.1/aliased.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/aliased.3
