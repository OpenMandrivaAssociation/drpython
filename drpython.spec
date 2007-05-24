%define name	drpython
%define version	161
%define release %mkrel 2

%define pyver	2.4

Name: 	 	%{name}
Summary: 	Python editor and development environment
Version: 	%{version}
Release: 	%{release}

Source:		http://prdownloads.sourceforge.net/drpython/%{name}-%{version}.zip
URL:		http://drpython.sourceforge.net/
License:	GPL
Group:		Development/Python
BuildRoot:	%{_tmppath}/%{name}-buildroot
Requires:	wxPythonGTK
BuildRequires:	ImageMagick
BuildArch:	noarch

%description
DrPython is a highly customizable, simple, and clean editing environment for
developing Python programs. It is intended primarily for use in schools, and
is a tribute to DrScheme.

%prep
%setup -q
chmod 644 %name.py

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%_bindir
mkdir -p $RPM_BUILD_ROOT/%_datadir/%name
mkdir -p $RPM_BUILD_ROOT/%_datadir/%name/documentation
cp *.py* $RPM_BUILD_ROOT/%_datadir/%name
cp -r examples bitmaps $RPM_BUILD_ROOT/%_datadir/%name
cp -r documentation/* $RPM_BUILD_ROOT/%_datadir/%name/documentation/
echo '#!/bin/bash' > $RPM_BUILD_ROOT/%_bindir/%name
echo 'cd %_datadir/%name' >> $RPM_BUILD_ROOT/%_bindir/%name
echo 'python drpython.pyw' >> $RPM_BUILD_ROOT/%_bindir/%name
chmod 755 $RPM_BUILD_ROOT/%_bindir/%name

#menu
mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat << EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}): command="%{_bindir}/%{name}" icon="%{name}.png" needs="x11" title="Dr. Python" longtitle="Python Editor and IDE" section="More Applications/Development/Development Environments" xdg="true"
EOF

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Dr. Python
Comment=Python Editor and IDE
Exec=%{_bindir}/%{name} 
Icon=%{name}
Terminal=false
Type=Application
Categories=X-MandrivaLinux-MoreApplications-Development-DevelopmentEnvironments;Development;IDE;
EOF

#icons
mkdir -p $RPM_BUILD_ROOT/%_liconsdir
convert -size 16x16 documentation/%name.png $RPM_BUILD_ROOT/%_liconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_iconsdir
convert -size 32x32 documentation/%name.png $RPM_BUILD_ROOT/%_iconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_miconsdir
convert -size 48x48 documentation/%name.png $RPM_BUILD_ROOT/%_miconsdir/%name.png

rm -rf $RPM_BUILD_ROOT%_datadir/drpython/bitmaps/24/.xvpics

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_menus
		
%postun
%clean_menus

%files
%defattr(-,root,root)
%doc examples/ *.txt
%{_bindir}/%name
%{_datadir}/%name
%{_menudir}/%name
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png
%{_datadir}/applications/mandriva-%{name}.desktop
