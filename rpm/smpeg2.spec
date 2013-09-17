Summary:   SDL MPEG Library
Name:      smpeg
Version:   2.0.0
Release:   1
License:   LGPL
Group:     System Environment/Libraries
Source:    %{name}-%{version}.tar.gz
URL:       http://icculus.org/smpeg/

%description
SMPEG is based on UC Berkeley's mpeg_play software MPEG decoder
and SPLAY, an mpeg audio decoder created by Woo-jae Jung. We have
completed the initial work to wed these two projects in order to
create a general purpose MPEG video/audio player for the Linux OS.

%package plaympeg
Summary: SDL MPEG library - "plaympeg" utility
Group: Development/Libraries
Requires: %{name}

%description plaympeg
SMPEG is based on UC Berkeley's mpeg_play software MPEG decoder
and SPLAY, an mpeg audio decoder created by Woo-jae Jung. We have
completed the initial work to wed these two projects in order to
create a general purpose MPEG video/audio player for the Linux OS.

This package contains the "plaympeg" CLI utility shipped with smpeg.

%package devel
Summary: Libraries, includes and more to develop SMPEG applications.
Group: Development/Libraries
Requires: %{name}

%description devel
SMPEG is based on UC Berkeley's mpeg_play software MPEG decoder
and SPLAY, an mpeg audio decoder created by Woo-jae Jung. We have
completed the initial work to wed these two projects in order to
create a general purpose MPEG video/audio player for the Linux OS.

This is the libraries, include files and other resources you can use
to develop SMPEG applications.

%prep
%setup -q

%build
%configure --enable-static=no
make

%install
%makeinstall

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr(-, root, root)
%doc CHANGES COPYING README
%{_libdir}/lib*.so.*

%files plaympeg
%defattr(-, root, root)
%doc CHANGES COPYING README
%{_bindir}/plaympeg
%{_datadir}/man/man1/plaympeg.1*

%files devel
%defattr(-, root, root)
%doc CHANGES COPYING README
%{_bindir}/smpeg2-config
%{_includedir}/*
%{_libdir}/lib*.la
%{_libdir}/lib*.so
%{_datadir}/aclocal/*.m4
