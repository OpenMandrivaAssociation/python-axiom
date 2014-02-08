%define module  axiom
%define name	python-%{module}
%define version 0.6.0
%define release 5

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


%changelog
* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 0.6.0-2mdv2011.0
+ Revision: 667911
- mass rebuild

* Tue Nov 02 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.6.0-1mdv2011.0
+ Revision: 592473
- rebuild for python 2.7
- drop the obselete %%py_requires macro and use BR python-devel

* Sun Jan 10 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.6.0-1mdv2010.1
+ Revision: 489386
- new version

* Thu Dec 25 2008 Adam Williamson <awilliamson@mandriva.org> 0.5.30-1mdv2009.1
+ Revision: 318783
- make the deletion less general and PLEASE FUCKING WORK THIS TIME
- delete some cache that gets generated during %%install
- rebuild for python 2.6
- new version 0.5.30

* Mon Apr 14 2008 Lev Givon <lev@mandriva.org> 0.5.27-4mdv2009.0
+ Revision: 193407
- Build as noarch package.
  Don't install build files.

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 0.5.27-3mdv2008.1
+ Revision: 171057
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
- fix no-buildroot-tag

* Tue Jan 29 2008 Erwan Velu <erwan@mandriva.org> 0.5.27-2mdv2008.1
+ Revision: 159812
- Adding more buildrequires

  + Helio Chissini de Castro <helio@mandriva.com>
    - import python-axiom


