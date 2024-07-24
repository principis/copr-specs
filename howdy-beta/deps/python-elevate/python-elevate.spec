%global srcname     elevate
%global forgeurl    https://github.com/barneygale/%{srcname}
%global commit      78e82a8a75e6c7ffba9cf5df86931770eacb9d13

Version:            0.1.3
%forgemeta

Name:           python-%{srcname}
Release:        3%{?dist}
Summary:        Python library for requesting root privileges

License:        MIT
URL:            %{forgeurl}
Source0:        %{forgesource}
BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
Elevate is a small Python library that re-launches the current process with
root/admin privileges using one of the following mechanisms:
- UAC (Windows)
- AppleScript (macOS)
- pkexec, gksudo or kdesudo (Linux)
- sudo (Linux, macOS)}

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
%pyproject_check_import -e elevate.windows

%files -n python3-%{srcname} -f %{pyproject_files}
%license COPYING.txt
%doc README.rst

%changelog
* Wed Jul 24 2024 Arthur Bols <copr@bols.dev> - 0.1.3-3
- Rebuilt for Python 3.13

* Tue Apr 09 2024 Arthur Bols <copr@bols.dev> - 0.1.3-2
- Rebuilt for Fedora 40

* Wed Jan 24 2024 Arthur Bols <copr@bols.dev> - 0.1.3-1
- Initial package.