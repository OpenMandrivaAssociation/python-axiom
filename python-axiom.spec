%define module  axiom

Summary:	Object database, or alternatively, an object-relational mapper

Name:		python-%{module}
Version:	0.7.1
Release:	4
Group:		Development/Python 
License:	BSD
Url:		http://www.divmod.org/trac/wiki/DivmodAxiom
Source0:	https://pypi.python.org/packages/source/A/Axiom/Axiom-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	python-epsilon
BuildRequires:	python-twisted
BuildRequires:	pkgconfig(python)
Requires:	python-epsilon 
Provides:	python-Axiom = %{version}
Provides:	Axiom = %{version}

%description
Axiom is an object database, or alternatively, an object-relational mapper.

%prep
%setup -qn Axiom-%{version}

%build
%__python setup.py build

%install
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}
rm -rf %{buildroot}%{py_puresitedir}/build
rm -f %{buildroot}%{py_puresitedir}/twisted/plugins/dropin.cache

%files
%doc *.txt LICENSE
%{py_puresitedir}/*
%{_bindir}/*
