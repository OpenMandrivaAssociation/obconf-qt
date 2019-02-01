Summary:	Openbox configuration tool for the LXQt desktop
Name:		obconf-qt
Version:	0.14.0
Release:	1
Source0:	https://downloads.lxqt.org/downloads/obconf-qt/%{version}/obconf-qt-%{version}.tar.xz
URL:		http://lxqt.org/
License:	GPL
Group:		Graphical desktop/Other
BuildRequires:	cmake
BuildRequires:	qmake5
BuildRequires:	ninja
BuildRequires:	cmake(Qt5LinguistTools)
BuildRequires:	cmake(Qt5Help)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5X11Extras)
BuildRequires:	cmake(lxqt-build-tools)
BuildRequires:	pkgconfig(lxqt)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(obrender-3.5)
BuildRequires:	pkgconfig(obt-3.5)

%description
Openbox configuration tool for the LXQt desktop.

%prep
%setup -q
# try to fix "undefined reference to symbol 'XInternAtom' - DSO missing from command line error
%cmake_qt5 -DUSE_QT5=ON -DPULL_TRANSLATIONS=NO -DCMAKE_EXE_LINKER_FLAGS=-lX11 -G Ninja

%build
# Need to be in a UTF-8 locale so grep (used by the desktop file
# translation generator) doesn't scream about translations containing
# "binary" (non-ascii) characters
export LANG=en_US.utf-8
export LC_ALL=en_US.utf-8
%ninja -C build

%install
# Need to be in a UTF-8 locale so grep (used by the desktop file
# translation generator) doesn't scream about translations containing
# "binary" (non-ascii) characters
export LANG=en_US.utf-8
export LC_ALL=en_US.utf-8
%ninja_install -C build
%find_lang %{name} --with-qt --all-name

%files -f %{name}.lang
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png
