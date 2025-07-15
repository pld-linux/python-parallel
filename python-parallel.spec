
%define	module	parallel

Summary:	Parallel port interface module
Summary(pl.UTF-8):	Moduł interfejsu do portu równoległego
Name:		python-parallel
Version:	0.2
Release:	1
License:	Python
Group:		Development/Languages/Python
Source0:	http://dl.sourceforge.net/pyserial/pyparallel-%{version}.zip
# Source0-md5:	46b65592f0b2fa7094ca87bf053e93a7
Patch0:		%{name}-distutils.patch
URL:		http://pyserial.sourceforge.net/
BuildRequires:	rpmbuild(macros) >= 1.710
%pyrequires_eq	python-modules
BuildRequires:	python-devel
BuildRequires:	unzip
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module encapsulates the access for the parallel port. It provides
backends for Python running on Windows and Linux.

%description -l pl.UTF-8
Ten moduł obudowuje dostęp do portu równoległego. Dostarcza backendy
dla Pythona działającego na Windows i Linuksie.

%prep
%setup  -q -n pyparallel-%{version}
%patch -P0 -p1

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install \
	--optimize 2 \
	--root=$RPM_BUILD_ROOT

%py_postclean
find $RPM_BUILD_ROOT%{py_sitescriptdir} -name "*parallelwin32*" -exec rm {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.txt README.txt
%{py_sitescriptdir}/%{module}
