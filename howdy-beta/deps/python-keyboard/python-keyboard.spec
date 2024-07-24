# Tests fail randomly, disable by default
%bcond_with tests

%global srcname     keyboard
%global forgeurl    https://github.com/boppreh/%{srcname}

Version:            0.13.5
%forgemeta

Name:           python-%{srcname}
Release:        3%{?dist}
Summary:        Hook and simulate keyboard events on Windows and Linux

License:        MIT
URL:            %{forgeurl}
Source0:        %{forgesource}
BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
Take full control of your keyboard with this small Python library. Hook global
events, register hotkeys, simulate key presses and much more.}

%description %_description

%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description

%prep
%forgeautosetup -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%if %{with tests}
%{py3_test_envvars} %{python3} -m keyboard._mouse_tests
%{py3_test_envvars} %{python3} -m keyboard._keyboard_tests
%else
%pyproject_check_import
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE.txt
%doc README.md

%changelog
* Wed Jul 24 2024 Arthur Bols <copr@bols.dev> - 0.13.5-3
- Rebuilt for Python 3.13

* Tue Apr 09 2024 Arthur Bols <copr@bols.dev> - 0.13.5-2
- Rebuilt for Fedora 40

* Wed Jan 24 2024 Arthur Bols <copr@bols.dev> - 0.13.5-1
- Initial package.