#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : ktp-kded-module
Version  : 19.08.1
Release  : 6
URL      : https://download.kde.org/stable/applications/19.08.1/src/ktp-kded-module-19.08.1.tar.xz
Source0  : https://download.kde.org/stable/applications/19.08.1/src/ktp-kded-module-19.08.1.tar.xz
Source1 : https://download.kde.org/stable/applications/19.08.1/src/ktp-kded-module-19.08.1.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause LGPL-2.1
Requires: ktp-kded-module-data = %{version}-%{release}
Requires: ktp-kded-module-lib = %{version}-%{release}
Requires: ktp-kded-module-license = %{version}-%{release}
Requires: ktp-kded-module-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : kactivities-dev
BuildRequires : kidletime-dev
BuildRequires : ktp-common-internals-dev
BuildRequires : telepathy-qt-dev

%description
No detailed description available

%package data
Summary: data components for the ktp-kded-module package.
Group: Data

%description data
data components for the ktp-kded-module package.


%package lib
Summary: lib components for the ktp-kded-module package.
Group: Libraries
Requires: ktp-kded-module-data = %{version}-%{release}
Requires: ktp-kded-module-license = %{version}-%{release}

%description lib
lib components for the ktp-kded-module package.


%package license
Summary: license components for the ktp-kded-module package.
Group: Default

%description license
license components for the ktp-kded-module package.


%package locales
Summary: locales components for the ktp-kded-module package.
Group: Default

%description locales
locales components for the ktp-kded-module package.


%prep
%setup -q -n ktp-kded-module-19.08.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1567712502
mkdir -p clr-build
pushd clr-build
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags} VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1567712502
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ktp-kded-module
cp COPYING %{buildroot}/usr/share/package-licenses/ktp-kded-module/COPYING
cp cmake/modules/COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/package-licenses/ktp-kded-module/cmake_modules_COPYING-CMAKE-SCRIPTS
pushd clr-build
%make_install
popd
%find_lang kded_ktp_integration_module

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/dbus-1/services/org.freedesktop.Telepathy.Client.KTp.KdedIntegrationModule.service
/usr/share/kservices5/kcm_ktp_integration_module.desktop
/usr/share/kservices5/kded/ktp_integration_module.desktop

%files lib
%defattr(-,root,root,-)
/usr/lib64/qt5/plugins/kcm_ktp_integration_module.so
/usr/lib64/qt5/plugins/kded_ktp_integration_module.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ktp-kded-module/COPYING
/usr/share/package-licenses/ktp-kded-module/cmake_modules_COPYING-CMAKE-SCRIPTS

%files locales -f kded_ktp_integration_module.lang
%defattr(-,root,root,-)

