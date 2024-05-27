Name:           python-strenum
Version:        0.4.15
Release:        1%{?dist}
Summary:        Python Enum that inherits from str

License:        MIT
URL:            https://github.com/irgeek/StrEnum
Source:         %{pypi_source StrEnum}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(versioneer)

%global _description %{expand:
StrEnum is a Python enum.Enum that inherits from str to complement enum
IntEnum in the standard library. Supports python 3.7+.}

%description %_description

%package -n python3-strenum
Summary:        %{summary}

%description -n python3-strenum %_description

%prep
%autosetup -p1 -n StrEnum-%{version}

rm versioneer.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l strenum

%check
%pyproject_check_import

%files -n python3-strenum -f %{pyproject_files}
%doc README.md

%changelog
* Mon May 27 2024 Arthur Bols <arthur@bols.dev> - 0.5.0-1
- Initial package.
