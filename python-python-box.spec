# Created by pyp2rpm-3.3.3
%global pypi_name python-box
%global srcname box

Name:           python-%{srcname}
Version:        3.4.5
Release:        1%{?dist}
Summary:        Advanced Python dictionaries with dot notation access

License:        MIT
URL:            https://github.com/cdgriffith/Box
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest-runner
BuildRequires:  python3-setuptools

%description
|BuildStatus| |CoverageStatus| |License| |PyPi| |DocStatus||BoxImage|Python
dictionaries with advanced dot notation access... code:: python from box import
Box movie_data { "movies": { "Spaceballs": { "imdb stars": 7.1, "rating": "PG",
"length": 96, "director": "Mel Brooks", "stars": [{"name": "Mel Brooks",
"imdb": "nm0000316", "role": "President Skroob"}, {"name": "John
Candy","imdb":...

%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

Requires:       python3-coverage >= 3.6
Requires:       python3-pytest
Requires:       python3-pytest-cov
%description -n python3-%{srcname}
|BuildStatus| |CoverageStatus| |License| |PyPi| |DocStatus||BoxImage|Python
dictionaries with advanced dot notation access... code:: python from box import
Box movie_data { "movies": { "Spaceballs": { "imdb stars": 7.1, "rating": "PG",
"length": 96, "director": "Mel Brooks", "stars": [{"name": "Mel Brooks",
"imdb": "nm0000316", "role": "President Skroob"}, {"name": "John
Candy","imdb":...

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{_bindir}/box.py
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/box.py
%{python3_sitelib}/python_box-%{version}-py%{python3_version}.egg-info

%changelog
* Thu Nov 07 2019 Evgeni Golov - 3.4.5-1
- Initial package.
