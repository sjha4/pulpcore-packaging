# Created by pyp2rpm-3.3.3
%global pypi_name pulp-file

Name:           python-%{pypi_name}
Version:        0.1.0b4
Release:        1%{?dist}
Summary:        File plugin for the Pulp Project

License:        GPLv2+
URL:            http://www.pulpproject.org/
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
pulp_file A Pulp plugin to support hosting arbitrary files.For more
information, please see the documentation < or the Pulp project page <>_.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3-pulpcore-plugin = 0.1rc7
Requires:       python3-setuptools
%description -n python3-%{pypi_name}
pulp_file A Pulp plugin to support hosting arbitrary files.For more
information, please see the documentation < or the Pulp project page <>_.

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
%{python3_sitelib}/pulp_file
%{python3_sitelib}/pulp_file-%{version}-py%{python3_version}.egg-info

%changelog
* Fri Nov 08 2019 Evgeni Golov - 0.1.0b4-1
- Initial package.
