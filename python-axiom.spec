%define module  axiom
%define name	python-%{module}
%define version 0.6.0
%define release %mkrel 1

Name: 		%{name}
Summary: 	Object database, or alternatively, an object-relational mapper
Version: 	%{version}
Release: 	%{release}
Group: 		Development/Python 
URL: 		http://www.divmod.org/trac/wiki/DivmodAxiom
Source0: 	http://divmod.org/trac/attachment/wiki/SoftwareReleases/Axiom-%{version}.tar.gz
License: 	BSD
Requires: 	python-epsilon 
Provides: 	python-Axiom = %{version}
Provides: 	Axiom = %{version}
BuildRequires: 	python-epsilon, python-twisted, python-devel
BuildArch:	noarch
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Axiom is an object database, or alternatively, an object-relational mapper.

%prep
%setup -q -n Axiom-%version

%build
%__python setup.py build

%install
%__rm -rf %buildroot

PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=INSTALLED_FILES.tmp
%__grep -v %{py_sitedir}/build INSTALLED_FILES.tmp > INSTALLED_FILES
%__rm -rf %{buildroot}%{py_sitedir}/build
# I don't think it would be right to package this - AdamW 2008/12
rm -f %{buildroot}%{py_puresitedir}/twisted/plugins/dropin.cache

%clean
%__rm -rf %buildroot

%files -f INSTALLED_FILES
%defattr(-,root,root)
%doc *.txt LICENSE
