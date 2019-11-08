# Created by pyp2rpm-3.3.3
%global pypi_name multidict

Name:           python-%{pypi_name}
Version:        4.5.2
Release:        1%{?dist}
Summary:        multidict implementation

License:        Apache 2
URL:            https://github.com/aio-libs/multidict
Source0:        %{pypi_source}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
 multidict .. image::

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
 multidict .. image::

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
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Fri Nov 08 2019 Evgeni Golov - 4.5.2-1
- Initial package.
