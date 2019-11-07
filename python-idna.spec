# Created by pyp2rpm-3.3.3
%global pypi_name idna

Name:           python-%{pypi_name}
Version:        2.8
Release:        1%{?dist}
Summary:        Internationalized Domain Names in Applications (IDNA)

License:        BSD-like
URL:            https://github.com/kjd/idna
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
Internationalized Domain Names in Applications (IDNA) Support for the
Internationalised Domain Names in Applications (IDNA) protocol as specified in
RFC 5891 < This is the latest version of the protocol and is sometimes referred
to as “IDNA 2008”.This library also provides support for Unicode Technical
Standard 46, Unicode IDNA Compatibility Processing < acts as a suitable
replacement for the...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Internationalized Domain Names in Applications (IDNA) Support for the
Internationalised Domain Names in Applications (IDNA) protocol as specified in
RFC 5891 < This is the latest version of the protocol and is sometimes referred
to as “IDNA 2008”.This library also provides support for Unicode Technical
Standard 46, Unicode IDNA Compatibility Processing < acts as a suitable
replacement for the...

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE.rst
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Thu Nov 07 2019 Evgeni Golov - 2.8-1
- Initial package.