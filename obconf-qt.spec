Summary:	Openbox configuration tool for the LXQt desktop
Name:		obconf-qt
Version:	0.9.0
Release:	3
Source0:	http://lxqt.org/downloads/%{name}/%{version}/%{name}-%{version}.tar.gz
URL:		http://lxqt.org/
License:	GPL
Group:		Graphical desktop/Other
BuildRequires:	cmake
BuildRequires:	qmake5
BuildRequires:	qt5-linguist-tools
BuildRequires:	pkgconfig(lxqt)
BuildRequires:	pkgconfig(Qt5Help)
BuildRequires:	pkgconfig(Qt5X11Extras)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(obrender-3.5)
BuildRequires:	pkgconfig(obt-3.5)

%description
Openbox configuration tool for the LXQt desktop.

%prep
%setup -q
# try to fix "undefined reference to symbol 'XInternAtom' - DSO missing from command line error
%cmake_qt5 -DUSE_QT5=ON -DCMAKE_EXE_LINKER_FLAGS=-lX11

%build
%make -C build

%install
%makeinstall_std -C build

%find_lang %{name} --with-qt

%files -f %{name}.lang
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png
