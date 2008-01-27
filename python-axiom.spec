Name: python-axiom
Summary: Axiom is an object database, or alternatively, an object-relational mapper
Version: 0.5.27
Release: %mkrel 1
Group: Development/Python 
URL: http://www.divmod.org/trac/wiki/DivmodEpsilon
Source0: Axiom-%{version}.tar.gz
License: BSD
BuildRequires: python-epsilon
Requires: python-epsilon 
Provides: python-Axiom = %version
Provides: Axiom = %version
%py_requires -d

%description
Axiom is an object database, or alternatively, an object-relational mapper.

%files
%defattr(-,root,root)
%_bindir/*
%py_platsitedir/*

#------------------------------------------------------------

%prep
%setup -q -n Axiom-%version

%build
python setup.py build

%install
rm -rf %buildroot

python setup.py install --root=%buildroot --install-lib=%py_platsitedir

%clean
rm -rf %buildroot

