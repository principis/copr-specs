%global         _name pam-python
%global         debug_package %{nil}

Name:           pam_python
Version:        1.0.8
Release:        4%{?dist}
Group:          System/Libraries
URL:            http://pam-python.sourceforge.net
License:        AGPLv3+
Summary:        Support for writing PAM modules in Python
Source:         https://sourceforge.net/projects/%{_name}/files/%{_name}-%{version}-1/%{_name}-%{version}.tar.gz
BuildRequires:  python2-devel
BuildRequires:  pam-devel
BuildRequires:  python2
BuildRequires:  gcc


%description
pam-python is a PAM Module that runs the Python interpreter, thus allowing PAM
modules to be written in Python.


%prep
%setup -q -n %{_name}-%{version}
sed -i 's|-Werror||' src/Makefile


%build
make -C src


%install
make -C src install LIBDIR=%{buildroot}/%{_lib}/security

%files
%doc *.txt *.html
/%{_lib}/security/pam_python.so


%changelog
* Wed Jul 24 2024 Arthur Bols <arthur@bols.dev> - 1.0.8-4
- Rebuilt for Fedora 40

* Thu Dec 29 2022 Arthur Bols <arthur@bols.dev> - 1.0.8-3
- Rebuilt for Fedora 37

* Fri May 20 2022 Arthur Bols <arthur@bols.dev> - 1.0.8-2
- Rebuilt for Fedora 36

* Thu Jun 10 2021 Arthur Bols <arthur@bols.dev> - 1.0.8-1
- Upstream release 1.0.8

* Tue Oct 20 2020 Arthur Bols <arthur@bols.dev> 1.0.7-2
- Rebuild for Fedora 33
- Fix spec formatting
- Add source hash

* Sat May 2 2020 Arthur Bols <arthur@bols.dev> 1.0.7-1
- Initial package
