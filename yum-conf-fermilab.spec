Name:		yum-conf-fermilab
Version:	1.1
Release:	2%{dist}
Summary:	Provide the yum repo files for Fermilab

URL:		https://github.com/fermilab-context-rpms/yum-conf-fermilab
Source0:	%{name}.tar.gz

BuildArch:	noarch
BuildRequires:	coreutils

# packages in the repos might work on fedora
#  but these repo files wont
Requires:	base-module(platform:%{expand:%%(echo %{dist} | tr -d '.')})
Provides:	fermilab-release = %{expand:%%(echo %{dist} | tr -d '.')}

License:	MIT

%description
Deploy the Fermilab yum repo files and GPG key.


%package gpgkey
Summary:	The yum repo GPG key for Fermilab's EL Context

%description gpgkey
Just the yum repo GPG key for Fermilab's EL Context.

%prep
%setup -q -n %{name}


%build


%install
%{__rm} -rf %{buildroot}
%{__install} -D RPM-GPG-KEY-fermilab %{buildroot}%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-fermilab
%{__install} -D fermilab.repo %{buildroot}%{_sysconfdir}/yum.repos.d/fermilab.repo
%{__install} -D fermilab-testing.repo %{buildroot}%{_sysconfdir}/yum.repos.d/fermilab-testing.repo
%{__install} -D fermilab-other.repo %{buildroot}%{_sysconfdir}/yum.repos.d/fermilab-other.repo


%files
%defattr(0644,root,root,0755)
%config(noreplace) %{_sysconfdir}/yum.repos.d/*
%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-fermilab

%files gpgkey
%defattr(0644,root,root,0755)
%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-fermilab


%changelog
* Wed Dec 7 2022 Pat Riehecky <riehecky@fnal.gov> 1.1-2
- Better abstraction

* Tue Nov 29 2022 Pat Riehecky <riehecky@fnal.gov> 1.1-1
- Use new repo paths

* Mon Feb 28 2022 Pat Riehecky <riehecky@fnal.gov> 1.0-2
- Use macros more elegantly
- use repo_gpgcheck=1 by default

* Mon Feb 4 2019 Pat Riehecky <riehecky@fnal.gov> 1.0-1
- Initial Build
