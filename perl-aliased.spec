#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-aliased
Version  : 0.34
Release  : 14
URL      : https://cpan.metacpan.org/authors/id/E/ET/ETHER/aliased-0.34.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/E/ET/ETHER/aliased-0.34.tar.gz
Summary  : 'Use shorter versions of class names.'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-aliased-license = %{version}-%{release}
Requires: perl-aliased-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Module::Build::Tiny)

%description
This archive contains the distribution aliased,
version 0.34:
Use shorter versions of class names.

%package dev
Summary: dev components for the perl-aliased package.
Group: Development
Provides: perl-aliased-devel = %{version}-%{release}
Requires: perl-aliased = %{version}-%{release}

%description dev
dev components for the perl-aliased package.


%package license
Summary: license components for the perl-aliased package.
Group: Default

%description license
license components for the perl-aliased package.


%package perl
Summary: perl components for the perl-aliased package.
Group: Default
Requires: perl-aliased = %{version}-%{release}

%description perl
perl components for the perl-aliased package.


%prep
%setup -q -n aliased-0.34
cd %{_builddir}/aliased-0.34

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-aliased
cp %{_builddir}/aliased-0.34/LICENSE %{buildroot}/usr/share/package-licenses/perl-aliased/66d0d9f0c382d7879a988d88ce2af6edfb186673
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/aliased.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-aliased/66d0d9f0c382d7879a988d88ce2af6edfb186673

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/aliased.pm
