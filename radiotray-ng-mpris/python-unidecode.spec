Name:           python-unidecode
Version:        1.3.8
Release:        1%{?dist}
Summary:        ASCII transliterations of Unicode text

License:        GPL-2.0-or-later
URL:            https://pypi.org/project/Unidecode/
Source:         %{pypi_source Unidecode}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(versioneer)

%global _description %{expand:
Unidecode, lossy ASCII transliterations of Unicode text.}

%description %_description

%package -n python3-unidecode
Summary:        %{summary}

%description -n python3-unidecode %_description

%prep
%autosetup -p1 -n Unidecode-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l unidecode

%check
%pyproject_check_import

%files -n python3-unidecode -f %{pyproject_files}
%doc README.rst
%{_bindir}/unidecode

%changelog
* Mon May 27 2024 Arthur Bols <arthur@bols.dev> - 0.5.0-1
- Initial package.

