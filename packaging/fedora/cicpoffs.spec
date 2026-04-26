Name:           cicpoffs
Version:        0.3
Release:        1%{?dist}
Summary:        Case-Insensitive Case-Preserving Overlay FUSE File System
License:        GPLv2
URL:            https://github.com/ublue-os/cicpoffs
Source0:        cicpoffs-src.tar.gz

%global debug_package %{nil}

BuildRequires:  gcc-c++
BuildRequires:  fuse3-devel
BuildRequires:  libattr-devel
BuildRequires:  make
Requires:       fuse3-libs

%description
Case-Insensitive Case-Preserving Overlay FUSE File System

%prep
%setup -q -n cicpoffs-src

%build
make cicpoffs

%install
install -Dm755 cicpoffs %{buildroot}%{_bindir}/cicpoffs
ln -s cicpoffs %{buildroot}%{_bindir}/mount.cicpoffs

%files
%{_bindir}/cicpoffs
%{_bindir}/mount.cicpoffs
