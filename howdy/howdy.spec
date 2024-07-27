%global         debug_package %{nil}

Name:           howdy
Version:        2.6.1
Release:        10%{?dist}
Summary:        Windows Hello™ style authentication for Linux


License:        MIT
URL:            https://github.com/boltgolt/%{name}
Source0:        https://github.com/boltgolt/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        com.github.boltgolt.howdy.policy
Source2:        howdy_profile.sh
Source3:        howdy_profile.csh
Source4:        https://github.com/boltgolt/howdy/pull/687.patch
Source10:       https://github.com/davisking/dlib-models/raw/master/dlib_face_recognition_resnet_model_v1.dat.bz2
Source11:       https://github.com/davisking/dlib-models/raw/master/mmod_human_face_detector.dat.bz2
Source12:       https://github.com/davisking/dlib-models/raw/master/shape_predictor_5_face_landmarks.dat.bz2

# Fix for Fedora Polkit https://github.com/boltgolt/howdy/pull/687
Patch0:         687.patch

BuildRequires: polkit-devel
BuildRequires: python3-devel
BuildRequires: bzip2

Requires:      python3dist(dlib) >= 6.0
Requires:      python3-opencv
Requires:      pam_python

%description
Windows Hello™ style authentication for Linux. Use your built-in IR emitters and
camera in combination with face recognition to prove who you are.

%prep
%autosetup -p1

# Set empty to remove `-sP`
%global py3_shebang_flags %{nil}
%py3_shebang_fix .

bzip2 -dc %{S:10} > %(f=%{basename:%{S:10}}; echo ${f%.*})
bzip2 -dc %{S:11} > %(f=%{basename:%{S:11}}; echo ${f%.*})
bzip2 -dc %{S:12} > %(f=%{basename:%{S:12}}; echo ${f%.*})


%build
## nothing to build


%install
mkdir -p %{buildroot}%{_libdir}/security/%{name}
# Remove backup file
rm -fr src/*~
cp -pr src/* %{buildroot}%{_libdir}/security/%{name}

# install dlib-data files
install -Dm 0644 *.dat -t %{buildroot}%{_libdir}/security/%{name}/dlib-data/

# Add polkit rules
mkdir -p %{buildroot}%{_datadir}/polkit-1/actions
install -Dm 0644 %{SOURCE1} %{buildroot}%{_datadir}/polkit-1/actions/

#Add bash completion
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions
install -Dm 644 autocomplete/%{name} %{buildroot}%{_datadir}/bash-completion/completions

# Create an executable
mkdir -p %{buildroot}%{_bindir}
chmod +x %{buildroot}%{_libdir}/security/%{name}/cli.py
ln -s %{_libdir}/security/%{name}/cli.py %{buildroot}%{_bindir}/%{name}

# Add environment variables
install -Dm 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/profile.d/howdy.sh
install -Dm 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/profile.d/howdy.csh



%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/polkit-1/actions/
%{_libdir}/security/%{name}/
%config(noreplace) %{_libdir}/security/%{name}/config.ini
%config(noreplace) %{_sysconfdir}/profile.d/howdy.*


%changelog
* Sat Jul 27 2024 Arthur Bols <arthur@bols.dev> - 2.6.1-10
- Remove -sP flags from shebang fix

* Wed Jul 24 2024 Arthur Bols <arthur@bols.dev> - 2.6.1-9
- Rebuilt for Fedora 40

* Tue Feb 14 2023 Arthur Bols <arthur@bols.dev> - 2.6.1-8
- Fix for Fedora Polkit on some systems

* Tue Nov 29 2022 Arthur Bols <arthur@bols.dev> - 2.6.1-7
- Rebuilt for Fedora 37

* Fri May 20 2022 Arthur Bols <arthur@bols.dev> - 2.6.1-6
- Rebuilt for Fedora 36

* Fri Jan 07 2022 Arthur Bols <arthur@bols.dev> - 2.6.1-5
- Incorrect disable of Intel MFX messages in csh

* Thu Jan 06 2022 Arthur Bols <arthur@bols.dev> - 2.6.1-4
- Add option to fix Intel MFX messages

* Thu Jun 10 2021 Arthur Bols <arthur@bols.dev> - 2.6.1-3
- Set OPENCV_LOG_LEVEL to ERROR to fix notices.

* Wed Sep 02 2020 Arthur Bols <arthur@bols.dev> - 2.6.1-2
- Rebuild for Fedora 32
- Fix spec formatting

* Wed Sep 02 2020 Arthur Bols <arthur@bols.dev> - 2.6.1-1
- Update to 2.6.1

* Sun May 03 2020 Arthur Bols <arthur@bols.dev> - 2.6.0-1
- Update to 2.6.0

* Sun May 03 2020 Arthur Bols <arthur@bols.dev> - 2.5.1-4
- Fixed dependencies

* Sun Apr 07 2019 Luya Tshimbalanga <luya@fedoraproject.org> - 2.5.1-3
- Add polkit policy

* Sun Apr 07 2019 Luya Tshimbalanga <luya@fedoraproject.org> - 2.5.1-2
- Install facial recognition data

* Tue Apr 02 2019 Luya Tshimbalanga <luya@fedoraproject.org> - 2.5.1-1
- Update to 2.5.1

* Sat Mar 16 2019 Luya Tshimbalanga <luya@fedoraproject.org> - 2.5.0-3
- Require python-v4l2

* Wed Jan 23 2019 Luya Tshimbalanga <luya@fedoraproject.org> - 2.5.0-2
- Fix pam configuration

* Sun Jan 06 2019 Luya Tshimbalanga <luya@fedoraproject.org> - 2.5.0-1
- Update to 2.5.0

* Thu Nov 29 2018 Luya Tshimbalanga <luya@fedoraproject.org> - 2.4.0-3
- Add conditional statement for RHEL/Centos 7.x based on williamwlk spec

* Thu Nov 29 2018 Luya Tshimbalanga <luya@fedoraproject.org> - 2.4.0-3
- Include bash completion

* Mon Nov 26 2018 Luya Tshimbalanga <luya@fedoraproject.org> - 2.4.0-2
- Switch to new requirement method from Fedora Python guideline

* Mon Nov 26 2018 Luya Tshimbalanga <luya@fedoraproject.org> - 2.4.0-1
- Update to 2.4.0

* Thu Nov  1 2018 Luya Tshimbalanga <luya@fedoraproject.org> - 2.3.1-1
- Initial package
