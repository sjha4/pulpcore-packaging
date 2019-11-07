# Created by pyp2rpm-3.3.3
%global pypi_name rq

Name:           python-%{pypi_name}
Version:        1.1.0
Release:        1%{?dist}
Summary:        RQ is a simple, lightweight, library for creating background jobs, and processing them

License:        BSD
URL:            https://github.com/nvie/rq/
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
rq is a simple, lightweight, library for creating background jobs, and
processing them.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3-click >= 5.0
Requires:       python3-redis >= 3.0.0
Requires:       python3-setuptools
%description -n python3-%{pypi_name}
rq is a simple, lightweight, library for creating background jobs, and
processing them.

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.md
%{_bindir}/rq
%{_bindir}/rqinfo
%{_bindir}/rqworker
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/tests
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Thu Nov 07 2019 Evgeni Golov - 1.1.0-1
- Initial package.
