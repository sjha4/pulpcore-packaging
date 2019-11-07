# Created by pyp2rpm-3.3.3
%global pypi_name djangorestframework-queryfields

Name:           python-%{pypi_name}
Version:        1.0.0
Release:        1%{?dist}
Summary:        Serialize a partial subset of fields in the API

License:        None
URL:            https://github.com/wimglenn/djangorestframework-queryfields
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-mock-django
BuildRequires:  python3-pytest-django
BuildRequires:  python3-django
BuildRequires:  python3-django-rest-framework
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel

%description
Django REST Framework QueryFields Installation .. code-block:: bash pip install
djangorestframework-queryfields Quickstart -Specify your base model serializer
like this:.. code-block:: python from rest_framework.serializers import
ModelSerializer from drf_queryfields import QueryFieldsMixin class
MyModelSerializer(QueryFieldsMixin, ModelSerializer): pass--.. code-block::
bash GET...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Django REST Framework QueryFields Installation .. code-block:: bash pip install
djangorestframework-queryfields Quickstart -Specify your base model serializer
like this:.. code-block:: python from rest_framework.serializers import
ModelSerializer from drf_queryfields import QueryFieldsMixin class
MyModelSerializer(QueryFieldsMixin, ModelSerializer): pass--.. code-block::
bash GET...

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.rst
%{python3_sitelib}/drf_queryfields
%{python3_sitelib}/djangorestframework_queryfields-%{version}-py%{python3_version}.egg-info

%changelog
* Thu Nov 07 2019 Evgeni Golov - 1.0.0-1
- Initial package.
