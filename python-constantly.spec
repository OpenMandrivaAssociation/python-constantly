Summary:	Python library for symbolic constants
Name:		python-constantly
Version:	23.10.4
Release:	1
License:	MIT
Group:		Development/Python
Url:		https://pypi.org/project/constantly/
Source0:	https://files.pythonhosted.org/packages/source/c/constantly/constantly-%{version}.tar.gz
BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(versioneer)
# Removed after 6.0
Obsoletes:	python2-constantly < %{EVRD}

%description
Python library for symbolic constants

%files
%defattr(0644,root,root,0755)
%{py_sitedir}/constantly
%{py_sitedir}/constantly-%{version}.dist-info
