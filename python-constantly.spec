Summary:	Python library for symbolic constants
Name:		python-constantly
Version:	15.1.0
Release:	6
License:	MIT
Group:		Development/Python
Url:		https://pypi.org/project/constantly/
Source0:	https://files.pythonhosted.org/packages/95/f1/207a0a478c4bb34b1b49d5915e2db574cadc415c9ac3a7ef17e29b2e8951/constantly-%{version}.tar.gz
BuildRequires:	pkgconfig(python3)
BuildRequires:	python-setuptools
BuildRequires:	pkgconfig(python2)
BuildRequires:	python2-setuptools
BuildArch:	noarch

%description
Python library for symbolic constants

%package -n python2-constantly
Summary:	Python 2.x library for symbolic constants
Group:		Development/Python

%description -n python2-constantly
Python 2.x library for symbolic constants

%prep
%setup -qn constantly-%{version}
%autopatch -p1

mkdir python2
mv `ls |grep -v python2` python2
cp -a python2 python3

%build
cd python2
python2 setup.py build

cd ../python3
python setup.py build

%install
cd python2
python2 setup.py install --root=%{buildroot}

cd ../python3
python setup.py install --root=%{buildroot}

%files
%defattr(0644,root,root,0755)
%{py_sitedir}/constantly
%{py_sitedir}/*.egg-info

%files -n python2-constantly
%{py2_puresitedir}/constantly
%{py2_puresitedir}/*.egg-info
