%global srcname     pyv4l2
%global forgeurl    https://github.com/duanhongyi/%{srcname}
%global commit      f12f0b3a14e44852f0a0d13ab561cbcae8b5e0c3

Version:            1.0.2
%forgemeta

Name:           python-%{srcname}
Release:        3%{?dist}
Summary:        Python library for v4l2

License:        MIT
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  python3-devel
BuildRequires:  gcc
BuildRequires:  pkgconfig(libv4l2)

%global _description %{expand:
A simple, libv4l2-based frames capture library.}

%description %_description

%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description

%prep
%forgeautosetup -p1

# fix import
sed -i 's/from v4l2 cimport/from pyv4l2.v4l2 cimport/' pyv4l2/control.pyx
sed -i 's/from v4l2 cimport/from pyv4l2.v4l2 cimport/' pyv4l2/frame.pyx

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel -C="--build-option=--use-cython"

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%pyproject_check_import

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
* Wed Jul 24 2024 Arthur Bols <copr@bols.dev> - 1.0.2-3
- Rebuilt for Python 3.13

* Tue Apr 09 2024 Arthur Bols <copr@bols.dev> - 1.0.2-2
- Rebuilt for Fedora 40

* Wed Jan 24 2024 Arthur Bols <copr@bols.dev> - 1.0.2-1
- Initial package.