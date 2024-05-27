Name:           python-yacl
Version:        0.5.0
Release:        1%{?dist}
Summary:        simple to use color logger for Python

License:        MIT
URL:            https://github.com/IngoMeyer441/yacl
Source0:        %{pypi_source yacl}
BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
YACL is a very simple to use color logger for Python intended to be used for
stderr logging. It can be set up with a single function call in existing
projects and enables colored logging output with reasonable defaults.
Colors are disabled automatically if stderr is not connected to a tty
(e.g. on file redirection) or if not supported by the connected terminal.
Currently, Linux and macOS are supported.}

%description %_description

%package -n     python3-yacl
Summary:        %{summary}
Suggests:       python3dist(pygments)

%description -n python3-yacl %_description

%prep
%autosetup -n yacl-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l yacl

%check
%pyproject_check_import

%files -f %{pyproject_files}
%doc README.md

%changelog
* Mon May 27 2024 Arthur Bols <arthur@bols.dev> - 0.5.0-1
- Initial package.
