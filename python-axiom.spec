%define module  axiom
%define name	python-%{module}
%define version 0.5.27
%define release 4

Name: 		%{name}
Summary: 	Object database, or alternatively, an object-relational mapper
Version: 	%{version}
Release: 	%mkrel %{release}
Group: 		Development/Python 
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL: 		http://www.divmod.org/trac/wiki/DivmodAxiom
Source0: 	Axiom-%{version}.tar.gz
License: 	BSD
Requires: 	python-epsilon 
Provides: 	python-Axiom = %{version}
Provides: 	Axiom = %{version}
BuildRequires: 	python-epsilon, python-twisted
BuildArch:	noarch
%py_requires -d

%description
Axiom is an object database, or alternatively, an object-relational mapper.

%prep
%setup -q -n Axiom-%version

%build
%__python setup.py build

%install
%__rm -rf %buildroot

%__python setup.py install --root=%{buildroot} --record=INSTALLED_FILES.tmp
%__grep -v %{py_sitedir}/build INSTALLED_FILES.tmp > INSTALLED_FILES
%__rm -rf %{buildroot}%{py_sitedir}/build

%clean
%__rm -rf %buildroot

%files -f INSTALLED_FILES
%defattr(-,root,root)
%doc *.txt LICENSE
