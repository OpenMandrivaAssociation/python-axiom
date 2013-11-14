%define module  axiom

Summary:	Object database, or alternatively, an object-relational mapper
Name:		python-%{module}
Version:	0.6.0
Release:	4
Group:		Development/Python 
License:	BSD
Url:		http://www.divmod.org/trac/wiki/DivmodAxiom
Source0:	http://divmod.org/trac/attachment/wiki/SoftwareReleases/Axiom-%{version}.tar.gz
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
%setup -qn Axiom-%version

%build
%__python setup.py build

%install
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=INSTALLED_FILES.tmp
grep -v %{py_sitedir}/build INSTALLED_FILES.tmp > INSTALLED_FILES
rm -rf %{buildroot}%{py_sitedir}/build
# I don't think it would be right to package this - AdamW 2008/12
rm -f %{buildroot}%{py_puresitedir}/twisted/plugins/dropin.cache

%files -f INSTALLED_FILES
%doc *.txt LICENSE

