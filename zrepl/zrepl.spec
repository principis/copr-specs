%bcond_without check

# https://github.com/zrepl/zrepl
%global goipath         github.com/zrepl/zrepl
Version:                0.6.1

%gometa -L -f

%global common_description %{expand:
One-stop ZFS backup & replication solution.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           zrepl
Release:        %autorelease
Summary:        One-stop ZFS backup & replication solution

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}
Source1:        zrepl.bash-completion
Source2:        zrepl.zsh-completion

Patch0:         0001-Fix-incorrect-log-usage.patch
Patch1:         0002-Remove-validator-v9.patch

Requires:       systemd

BuildRequires:  systemd-rpm-macros

%description %{common_description}

%gopkg

%prep
%goprep -A
%autopatch -p1

# fix systemd service path
sed -i 's#ExecStart=/usr/local/bin/zrepl #ExecStart=/usr/bin/zrepl #' dist/systemd/zrepl.service
sed -i 's#ExecStartPre=/usr/local/bin/zrepl #ExecStartPre=/usr/bin/zrepl #' dist/systemd/zrepl.service

sed -i 's#USR_SHARE_ZREPL#/usr/share/doc/zrepl#' packaging/systemd-default-zrepl.yml

%generate_buildrequires
%go_generate_buildrequires

%build
%gobuild -o %{gobuilddir}/bin/zrepl %{goipath}

%install
%gopkginstall
install -m 0755 -vd                                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/*                 %{buildroot}%{_bindir}/
install -m 0644 -Dp dist/systemd/zrepl.service          %{buildroot}%{_unitdir}/zrepl.service
install -m 0644 -Dp packaging/systemd-default-zrepl.yml %{buildroot}%{_sysconfdir}/zrepl/zrepl.yml
install -m 0644 -Dp %{SOURCE1}                          %{buildroot}%{_datadir}/bash-completion/completions/zrepl
install -m 0644 -Dp %{SOURCE2}                          %{buildroot}%{_datadir}/zsh/site-functions/_zrepl

pushd config/samples >/dev/null
find . -type f -exec install -m 0644 -Dp {}             %{buildroot}%{_pkgdocdir}/examples/{} \;
popd >/dev/null
install -m 0644 -vp README.md                           %{buildroot}%{_pkgdocdir}/

%if %{with check}
%check
%gocheck
%endif

%post
%systemd_post zrepl.service

%preun
%systemd_preun zrepl.service

%postun
%systemd_postun_with_restart zrepl.service

%files
%license LICENSE
%doc %{_pkgdocdir}
%{_bindir}/zrepl
%{_unitdir}/zrepl.service
%dir %{_sysconfdir}/zrepl/
%config(noreplace) %{_sysconfdir}/zrepl/zrepl.yml
%dir %{_datadir}/bash-completion/
%dir %{_datadir}/bash-completion/completions/
%{_datadir}/bash-completion/completions/zrepl
%dir %{_datadir}/zsh/
%dir %{_datadir}/zsh/site-functions/
%{_datadir}/zsh/site-functions/_zrepl

%gopkgfiles

%changelog
%autochangelog
