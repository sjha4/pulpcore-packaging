# Created by pyp2rpm-3.3.3
%global pypi_name packaging

Name:           python-%{pypi_name}
Version:        19.2
Release:        1%{?dist}
Summary:        Core utilities for Python packages

License:        BSD or Apache License, Version 2.0
URL:            https://github.com/pypa/packaging
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
packaging Core utilities for Python packages.The packaging project includes the
following: version handling, specifiers, markers, requirements, tags,
utilities.Documentation -The documentation_ provides information and the API
for the following:- Version Handling - Specifiers - Markers - Requirements-
UtilitiesInstallation Use pip to install these utilities:: pip install
packagingDiscussion...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3-pyparsing >= 2.0.2
Requires:       python3-six
%description -n python3-%{pypi_name}
packaging Core utilities for Python packages.The packaging project includes the
following: version handling, specifiers, markers, requirements, tags,
utilities.Documentation -The documentation_ provides information and the API
for the following:- Version Handling - Specifiers - Markers - Requirements-
UtilitiesInstallation Use pip to install these utilities:: pip install
packagingDiscussion...

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE LICENSE.APACHE LICENSE.BSD
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Thu Nov 07 2019 Evgeni Golov - 19.2-1
- Initial package.