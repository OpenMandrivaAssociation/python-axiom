%define module  axiom

Summary:	Object database, or alternatively, an object-relational mapper

Name:		python-%{module}
Version:	0.9.0
Release:	2
Group:		Development/Python 
License:	BSD
Url:		https://www.divmod.org/trac/wiki/DivmodAxiom
Source:		https://github.com/twisted/axiom/archive/refs/heads/master.tar.gz
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(epsilon)
BuildRequires:	python%{pyver}dist(twisted)
BuildRequires:	pkgconfig(python3)
Requires:	python%{pyver}dist(epsilon)
BuildSystem:	python

%description
Axiom is an object database, or alternatively, an object-relational mapper.

%files
%doc *.txt LICENSE
%{py_puresitedir}/*
%{_bindir}/*
