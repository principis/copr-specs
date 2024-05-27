Name:           radiotray-ng-mpris
Version:        0.1.2
Release:        1%{?dist}
Summary:        A wrapper script for Radiotray-NG which provides an MPRIS2 interface

License:        MIT
URL:            https://github.com/IngoMeyer441/radiotray-ng-mpris
Source0:        %{pypi_source radiotray_ng_mpris}
BuildArch:      noarch

Requires:       radiotray-ng

BuildRequires:  python3-devel

%py_provides python3-%{name}

%description
Radiotray-NG MPRIS is a wrapper for Radiotray-NG to add an MPRIS2 interface
which integrates well with desktop environments (like GNOME, KDE or XFCE) or
desktop independent music player control tools like playerctl.

%prep
%autosetup -n radiotray_ng_mpris-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l radiotray_ng_mpris

%check
%pyproject_check_import

%files -f %{pyproject_files}
%doc README.md
%{_bindir}/radiotray-ng-mpris

%changelog
* Mon May 27 2024 Arthur Bols <arthur@bols.dev> - 0.1.2-1
- Initial package.