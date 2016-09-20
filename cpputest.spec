%global debug_package %{nil}

Name: cpputest
Version: 3.8.0+
Release: 0
Summary: C/C++ based unit test framework
License: BSD-3-Clause
Group: Development/Libraries/C and C++
Url: http://cpputest.github.io/
Source: cpputest-%version.tar.gz
Source1: %{name}-rpmlintrc
#Patch0: commit-bf61b4a
BuildRequires: automake autoconf doxygen fdupes gcc-c++ libtool pkg-config
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}
Requires: %{name}-devel = %{version}-%{release}

%description
CppUTest is a C /C++ based unit xUnit test framework for unit testing and for
test-driving your code. It is written in C++ but is used in C and C++ projects
and frequently used in embedded systems but it works for any C/C++ project.

%package devel
Summary: C/C++ based unit test framework - headers and static libraries
Provides: cpputest-static = %{version}-%{release}

%description devel
CppUTest is a C /C++ based unit xUnit test framework for unit testing and for
test-driving your code. It is written in C++ but is used in C and C++ projects
and frequently used in embedded systems but it works for any C/C++ project.

%prep
%setup -q
#%patch0 -p1

%build
autoreconf --force --install
%configure
make %{?_smp_mflags}
doxygen

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/%{_datadir}/cpputest
cp -rp examples scripts $RPM_BUILD_ROOT/%{_datadir}/cpputest
chmod +x $RPM_BUILD_ROOT/%{_datadir}/cpputest/scripts/NewProject.sh

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING NEWS
%doc README.md README_CppUTest_for_C.txt README_UsersOfPriorVersions.txt
%doc cpputest_doxygen/html
%{_datadir}/cpputest

%files devel
%defattr(-,root,root,-)
%{_includedir}/CppUTestExt
%{_includedir}/CppUTest
%{_libdir}/pkgconfig/cpputest.pc
%{_libdir}/libCppUTestExt.a
%{_libdir}/libCppUTest.a

%changelog

