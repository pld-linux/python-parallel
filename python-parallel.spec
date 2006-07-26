
%define	module	parallel

Summary:	Parallel port interface module
Summary(pl):	Modu³ interfejsu do portu równoleg³ego
Name:		python-parallel
Version:	0.2
Release:	1
License:	Python
Group:		Development/Languages/Python
Source0:	http://dl.sourceforge.net/pyserial/pyparallel-%{version}.zip
# Source0-md5:	46b65592f0b2fa7094ca87bf053e93a7
Patch0:		%{name}-distutils.patch
URL:		http://pyserial.sourceforge.net/
%pyrequires_eq	python-modules
BuildRequires:	python-devel
BuildRequires:	unzip
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module encapsulates the access for the parallel port. It provides
backends for Python running on Windows and Linux.

%description -l pl
Ten modu³ obudowuje dostêp do portu równoleg³ego. Dostarcza backendy
dla Pythona dzia³aj±cego na Windows i Linuksie.

%prep
%setup  -q -n pyparallel-%{version}
%patch0 -p1

%build
python ./setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python ./setup.py install \
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
