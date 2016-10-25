Name:           ros-indigo-bondcpp
Version:        1.7.18
Release:        0%{?dist}
Summary:        ROS bondcpp package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/bondcpp
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       libuuid-devel
Requires:       ros-indigo-bond
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-smclib
BuildRequires:  boost-devel
BuildRequires:  libuuid-devel
BuildRequires:  ros-indigo-bond
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-cmake-modules >= 0.3.2
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-smclib

%description
C++ implementation of bond, a mechanism for checking when another process has
terminated.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Mon Oct 24 2016 Mikael Arguedas <mikael@osrfoundation.org> - 1.7.18-0
- Autogenerated by Bloom

* Wed Jun 22 2016 Mikael Arguedas <mikael@osrfoundation.org> - 1.7.17-0
- Autogenerated by Bloom

