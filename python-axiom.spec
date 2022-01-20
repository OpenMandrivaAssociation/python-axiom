NOTE: This package cannot now be build because python2 support has been droppeed in
some of the dependent packages. Porting axion to Python3 has been done and awaits 
review and merge so the package should be retained in our repo.

%define module  axiom

Summary:	Object database, or alternatively, an object-relational mapper

Name:		python-%{module}
Version:	0.7.5
Release:	1
Group:		Development/Python 
License:	BSD
Url:		http://www.divmod.org/trac/wiki/DivmodAxiom
Source0:	https://pypi.python.org/packages/source/A/Axiom/Axiom-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	python-epsilon
BuildRequires:	python-twisted
BuildRequires:	pkgconfig(python2)
Requires:	python-epsilon 
Provides:	python-Axiom = %{version}
Provides:	Axiom = %{version}

%description
Axiom is an object database, or alternatively, an object-relational mapper.

%prep
%setup -qn Axiom-%{version}

%build
python2 setup.py build

%install
PYTHONDONTWRITEBYTECODE= python2 setup.py install --root=%{buildroot}
rm -rf %{buildroot}%{py2_puresitedir}/build
rm -f %{buildroot}%{py2_puresitedir}/twisted/plugins/dropin.cache

%files
%doc *.txt LICENSE
%{py2_puresitedir}/*
%{_bindir}/*
