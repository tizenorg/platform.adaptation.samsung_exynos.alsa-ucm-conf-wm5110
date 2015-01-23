Name:       alsa-ucm-data-wm5110
Summary:    ALSA UCM data pkg for WM5110 codec
Version:    0.0.1
Release:    1
License:    LGPL-2.1+
BuildArch:  noarch
Source0:    %{name}-%{version}.tar.gz

%description
ALSA UCM data for wm5110

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/alsa/ucm
cp -a wm5110 %{buildroot}/usr/share/alsa/ucm
mkdir -p %{buildroot}/usr/share/license
cp -a LICENSE.LGPL-2.1+ %{buildroot}/usr/share/license/%{name}

%post

%files
%manifest alsa-ucm-conf-wm5110.manifest
/usr/share/alsa/ucm/wm5110/*
/usr/share/license/alsa-ucm-data-wm5110
