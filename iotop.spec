%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
Name: iotop
Version: 0.3.2
Release: 3%{?dist}
Summary: Top like utility for I/O

Group: Applications/System
License: GPLv2
URL: http://guichaz.free.fr/iotop/
Source0: http://guichaz.free.fr/iotop/files/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch: noarch
BuildRequires: python-devel
BuildRequires: python-setuptools-devel
Requires: python

Patch0: iotop-0.2-setuptools.patch

#taken from upstream, rhbz#580972 - fix int size on ppc64
Patch1: iotop-0.4-ppctypesize.patch

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__python} setup.py build

%description
Linux has always been able to show how much I/O was going on
(the bi and bo columns of the vmstat 1 command).
iotop is a Python program with a top like UI used to
show of behalf of which process is the I/O going on.


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --root=${RPM_BUILD_ROOT}


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc COPYING NEWS README THANKS
%{_bindir}/iotop
%{_mandir}/man1/iotop.1.*
%{python_sitelib}/*

%changelog
* Tue May 04 2010 Michal Hlavinka <mhlavink@redhat.com> - 0.3.2-3
- fix iotop for ppc64 (#580972)

* Thu Feb 18 2010 Michal Hlavinka <mhlavink@redhat.com> - 0.3.2-2
- README added to doc

* Tue Jan 05 2010 Michal Hlavinka <mhlavink@redhat.com> - 0.3.2-1
- updated to 0.3.2

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.3-2.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue May 19 2009 Adel Gadllah <adel.gadllah@gmail.com> 0.3-1
- New upstream version
- fixes RH #475917

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.2.1-2
- Rebuild for Python 2.6

* Wed Jul 09 2008 Adel Gadllah <adel.gadllah@gmail.com> 0.2.1-1
- Update to 0.2.1

* Mon Jul 07 2008 Adel Gadllah <adel.gadllah@gmail.com> 0.2-2
- New upstream tarball..

* Mon May 26 2008 Adel Gadllah <adel.gadllah@gmail.com> 0.2-1
- Update to new upstream version

* Fri Dec 28 2007 Adel Gadllah <adel.gadllah@gmail.com> 0.1-3
- Fix build issue

* Fri Dec 28 2007 Adel Gadllah <adel.gadllah@gmail.com> 0.1-2
- Fix traceback on xterm-color RH #400071

* Sun Nov 3 2007 Adel Gadllah <adel.gadllah@gmail.com> 0.1-1
- Fix version

* Sun Nov 3 2007 Adel Gadllah <adel.gadllah@gmail.com> 20070930-1
- Initial Build
