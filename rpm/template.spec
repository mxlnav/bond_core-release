Name:           ros-kinetic-bondpy
Version:        1.8.1
Release:        0%{?dist}
Summary:        ROS bondpy package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/bondpy
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       libuuid-devel
Requires:       ros-kinetic-rospy
Requires:       ros-kinetic-smclib
BuildRequires:  ros-kinetic-bond
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-rospy
BuildRequires:  ros-kinetic-smclib

%description
Python implementation of bond, a mechanism for checking when another process has
terminated.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Thu Nov 02 2017 Mikael Arguedas <mikael@osrfoundation.org> - 1.8.1-0
- Autogenerated by Bloom

* Thu Mar 30 2017 Mikael Arguedas <mikael@osrfoundation.org> - 1.7.19-0
- Autogenerated by Bloom

* Mon Oct 24 2016 Mikael Arguedas <mikael@osrfoundation.org> - 1.7.18-0
- Autogenerated by Bloom

* Tue Mar 15 2016 Mikael Arguedas <mikael@osrfoundation.org> - 1.7.17-0
- Autogenerated by Bloom

