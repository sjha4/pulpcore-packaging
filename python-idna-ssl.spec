# Created by pyp2rpm-3.3.3
%global pypi_name idna-ssl

Name:           python-%{pypi_name}
Version:        1.1.0
Release:        1%{?dist}
Summary:        Patch ssl.match_hostname for Unicode(idna) domains support

License:        None
URL:            https://github.com/aio-libs/idna-ssl
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
:info: Patch ssl.match_hostname for Unicode(idna) domains support Installation
.. code-block:: shell pip install idna-sslUsage .. code-block:: python from
idna_ssl import patch_match_hostname noqa isort:skip patch_match_hostname()
noqa isort:skip

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3-idna >= 2.0
%description -n python3-%{pypi_name}
:info: Patch ssl.match_hostname for Unicode(idna) domains support Installation
.. code-block:: shell pip install idna-sslUsage .. code-block:: python from
idna_ssl import patch_match_hostname noqa isort:skip patch_match_hostname()
noqa isort:skip

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/idna_ssl.py
%{python3_sitelib}/idna_ssl-%{version}-py%{python3_version}.egg-info

%changelog
* Fri Nov 08 2019 Evgeni Golov - 1.1.0-1
- Initial package.
