Name:           python-mpris-server
Version:        0.9.0
Release:        1%{?dist}
Summary:        Integrate MPRIS Media Player support into your app

License:        LGPL-3.0-only
URL:            https://github.com/alexdelorenzo/mpris_server
Source0:        %{pypi_source mpris_server}
BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
mpris_server provides adapters to integrate MPRIS support in your media player
or device. By supporting MPRIS in your app, you will allow Linux users to
control all aspects of playback from the media controllers they already have
installed.}

%description %_description

%package -n     python3-mpris-server
Summary:        %{summary}

%description -n python3-mpris-server %_description

%prep
%autosetup -n mpris_server-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l mpris_server

%check
%pyproject_check_import

%files -n python3-mpris-server -f %{pyproject_files}
%doc README.md

%changelog
* Mon May 27 2024 Arthur Bols <arthur@bols.dev> - 0.9.0-1
- Initial package.
