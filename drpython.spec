%define name	drpython
%define version	165
%define release %mkrel 1

Name: 	 	%{name}
Summary: 	Python editor and development environment
Version: 	%{version}
Release: 	%{release}

Source:		http://prdownloads.sourceforge.net/drpython/%{name}%{version}.tar.bz2
URL:		http://drpython.sourceforge.net/
License:	GPL
Group:		Development/Python
BuildRoot:	%{_tmppath}/%{name}-buildroot
Requires:	wxPythonGTK
BuildRequires:	ImageMagick
BuildRequires:	python-setuptools
BuildRequires:	python
BuildRequires:	python-devel
BuildArch:	noarch

%description
DrPython is a highly customizable, simple, and clean editing environment for
developing Python programs. It is intended primarily for use in schools, and
is a tribute to DrScheme.

%prep
%setup -q -n %{name}
chmod 644 %name.py

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --root=$RPM_BUILD_ROOT
echo 'python %py_puresitedir/%name/%name.pyw' >> $RPM_BUILD_ROOT/%_bindir/%name
chmod 755 $RPM_BUILD_ROOT/%_bindir/%name
rm -f $RPM_BUILD_ROOT/%_bindir/postinst.py

#menu

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

mkdir -p $RPM_BUILD_ROOT/%_iconsdir/hicolor/{48x48,32x32,16x16}/apps
convert -size 16x16 documentation/%name.png $RPM_BUILD_ROOT/%_iconsdir/hicolor/16x16/apps/%name.png
convert -size 32x32 documentation/%name.png $RPM_BUILD_ROOT/%_iconsdir/hicolor/32x32/apps/%name.png
convert -size 48x48 documentation/%name.png $RPM_BUILD_ROOT/%_iconsdir/hicolor/48x48/apps/%name.png

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
%py_puresitedir/%name
%py_puresitedir/DrPython-165-py2.5.egg-info
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png
%{_iconsdir}/hicolor/16x16/apps/%name.png
%{_iconsdir}/hicolor/32x32/apps/%name.png
%{_iconsdir}/hicolor/48x48/apps/%name.png
%{_datadir}/applications/mandriva-%{name}.desktop
