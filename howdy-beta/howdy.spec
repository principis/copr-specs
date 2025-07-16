%global forgeurl    https://github.com/boltgolt/%{name}
%global commit      d3ab99382f88f043d15f15c1450ab69433892a1c

%forgemeta

Name:           howdy
Version:        3.0.0
Release:        7%{?dist}
Summary:        Windows Hello™ style authentication for Linux

# The entire source code is GPL-3.0-or-later except:
# howdy/src/recorders/v4l2.py which is GPL-2.0-or-later OR BSD-3-Clause.
License:        MIT AND (GPL-2.0-or-later OR BSD-3-Clause)
URL:            %{forgeurl}
Source0:        %{forgesource}
Source1:        howdy_profile.sh
Source2:        howdy_profile.csh
Source10:       https://github.com/davisking/dlib-models/raw/master/dlib_face_recognition_resnet_model_v1.dat.bz2
Source11:       https://github.com/davisking/dlib-models/raw/master/mmod_human_face_detector.dat.bz2
Source12:       https://github.com/davisking/dlib-models/raw/master/shape_predictor_5_face_landmarks.dat.bz2

Patch0:         0001-remove-exists-check.patch

BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  bzip2
BuildRequires:  python3-devel

BuildRequires:  pkgconfig(INIReader)
BuildRequires:  pkgconfig(libevdev)
BuildRequires:  pkgconfig(pam)

Requires:       hicolor-icon-theme
Requires:       python3dist(dlib)
Requires:       python3dist(keyboard)
Requires:       python3dist(numpy)
Requires:       python3dist(opencv)
Requires:       python3dist(pyv4l2)

Requires:       %{name}-data = %{version}-%{release}

%description
Windows Hello™ style authentication for Linux. Use your built-in IR emitters
and camera in combination with face recognition to prove who you are.


%package data
Summary:    Data files for %{name}
BuildArch:  noarch
License:    CC0-1.0

%description data
This package contains data files for %{name}.

%package gtk
Summary:    Howdy GTK+ interface
BuildArch:  noarch
Requires:   %{name}%{?_isa} = %{version}-%{release}
Requires:   hicolor-icon-theme
Requires:   gtk3
Requires:   polkit
Requires:   python3-gobject
Requires:   python3dist(elevate)
Requires:   python3dist(pycairo)

%description gtk
Howdy GTK+ interface.

%prep
%forgeautosetup -p1
bzip2 -dc %{S:10} > howdy/src/dlib-data/%(f=%{basename:%{S:10}}; echo ${f%.*})
bzip2 -dc %{S:11} > howdy/src/dlib-data/%(f=%{basename:%{S:11}}; echo ${f%.*})
bzip2 -dc %{S:12} > howdy/src/dlib-data/%(f=%{basename:%{S:12}}; echo ${f%.*})

# Fix perms
chmod 0755 howdy/src/compare.py

# Disable downloading dlib-data files
sed -i "/install_data('dlib-data\/install.sh',.*/d"  howdy/src/meson.build

%build
%meson \
    -Ddlib_data_dir=%{_datadir}/%{name}/dlib-data/ \
    -Dinstall_in_site_packages=true \
    -D python.bytecompile=-1 \
    -D with_polkit=true \
    -D python_path=%{python3}
%meson_build

%install
%meson_install

# Install environment variables
install -Dm 0644 %{S:1} %{buildroot}%{_sysconfdir}/profile.d/%{name}.sh
install -Dm 0644 %{S:2} %{buildroot}%{_sysconfdir}/profile.d/%{name}.csh

# Install logos
install -Dm 0644 howdy/src/logo.png %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.png
install -Dm 0644 howdy-gtk/src/logo.png %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}-gtk.png
ln -sf %{_datadir}/icons/hicolor/scalable/apps/%{name}.png %{buildroot}%{_datadir}/%{name}/logo.png
ln -sf %{_datadir}/icons/hicolor/scalable/apps/%{name}-gtk.png %{buildroot}%{_datadir}/%{name}-gtk/logo.png

# Fix permissions
chmod 0755 %{buildroot}%{bash_completions_dir}/%{name}
chmod 0644 %{buildroot}%{_sysconfdir}/%{name}/config.ini
mkdir -p   %{buildroot}%{_sysconfdir}/%{name}/models/

# install dlib-data files
install -Dm 0644 howdy/src/dlib-data/*.dat -t %{buildroot}%{_datadir}/%{name}/dlib-data/


%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/logo.png
%{bash_completions_dir}/%{name}
%{_datadir}/icons/hicolor/scalable/apps/%{name}.png
%{_datadir}/polkit-1/actions/com.github.boltgolt.howdy-gtk.policy
%{_libdir}/security/pam_howdy.so
%{_mandir}/man1/%{name}.1*
%{python3_sitelib}/%{name}/
%dir %{_sysconfdir}/%{name}/
%dir %{_sysconfdir}/%{name}/models/
%config(noreplace) %{_sysconfdir}/%{name}/config.ini
%config(noreplace) %{_sysconfdir}/profile.d/%{name}.*

%files gtk
%{_bindir}/%{name}-gtk
%{_datadir}/%{name}-gtk/
%{_datadir}/icons/hicolor/scalable/apps/%{name}-gtk.png
%{python3_sitelib}/%{name}-gtk/

%files data
%dir %{_datadir}/%{name}/
%dir %{_datadir}/%{name}/dlib-data/
%{_datadir}/%{name}/dlib-data/*.dat

%changelog
* Wed Jul 16 2025 Alex Shek <hms.starryfish@gmail.com> - 3.0.0-7
- Small packaging fixes.

* Tue Jun 24 2025 Alex Shek <hms.starryfish@gmail.com> - 3.0.0-6
- Rebase to d3ab99382f88f043d15f15c1450ab69433892a1c

* Thu Feb 20 2025 Alex Shek <hms.starryfish@gmail.com> - 3.0.0-5
- Rebase to aef35b526e4fef082f4bbfd6ffb5cbbc520ff629

* Wed Jul 24 2024 Arthur Bols <copr@bols.dev> - 3.0.0-4
- Rebase to aa75c7666c040c6a7c83cd92b9b81a6fea4ce97c

* Tue Apr 09 2024 Arthur Bols <copr@bols.dev> - 3.0.0-3
- Small packaging fixes.

* Wed Jan 24 2024 Arthur Bols <copr@bols.dev> - 3.0.0-2
- Added polkit patch.

* Wed Jan 24 2024 Arthur Bols <copr@bols.dev> - 3.0.0-1
- Initial package.
