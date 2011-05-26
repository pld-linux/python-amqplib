%define 	module	amqplib
Summary:	Client library for AMQP (Advanced Message Queuing Protocol)
Name:		python-%{module}
Version:	0.6.1
Release:	0.1
License:	LGPL v2.1
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/a/%{module}/%{module}-%{version}.tgz
# Source0-md5:	b2f6679b27eaae97c50a9c3504154fae
URL:		http://code.google.com/p/py-amqplib/
BuildRequires:	python-distribute
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-modules
Requires:	python-pyparsing
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Client library for AMQP (Advanced Message Queuing Protocol).

%prep
%setup -q -n %{module}-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* TODO
%{py_sitescriptdir}/%{module}
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/%{module}-*.egg-info
%endif
