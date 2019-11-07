# Created by pyp2rpm-3.3.3
%global pypi_name ruamel.yaml.clib

Name:           python-%{pypi_name}
Version:        0.2.0
Release:        1%{?dist}
Summary:        C version of reader, parser and emitter for ruamel

License:        MIT
URL:            https://bitbucket.org/ruamel/yaml.clib
Source0:        %{pypi_source}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
ruamel.yaml.clib ruamel.yaml.clib is the C based reader/scanner and emitter for
ruamel.yaml:version: 0.2.0 :updated: 2019-09-26 :documentation: :repository:
:pypi: package was split of from ruamel.yaml, so that ruamel.yaml can be build
as a universal wheel. Apart from the C code seldom changing, and taking a long
time to compile for all platforms, this allows installation of the .so on
Linux...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
ruamel.yaml.clib ruamel.yaml.clib is the C based reader/scanner and emitter for
ruamel.yaml:version: 0.2.0 :updated: 2019-09-26 :documentation: :repository:
:pypi: package was split of from ruamel.yaml, so that ruamel.yaml can be build
as a universal wheel. Apart from the C code seldom changing, and taking a long
time to compile for all platforms, this allows installation of the .so on
Linux...

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
%{python3_sitearch}/ruamel
%{python3_sitearch}/_ruamel_yaml.cpython-37m-x86_64-linux-gnu.so
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Thu Nov 07 2019 Evgeni Golov - 0.2.0-1
- Initial package.