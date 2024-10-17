%define oname	libmusicbrainz
%define api	3
%define major	6
%define libname	%mklibname musicbrainz %{api} %{major}
%define devname	%mklibname -d musicbrainz %{api}

Summary:	A software library for accesing MusicBrainz servers
Name:		libmusicbrainz3
Version:	3.0.3
Release:	17
Group:		Sound
License:	LGPLv2+
Url:		https://musicbrainz.org/doc/libmusicbrainz
Source0:	http://ftp.musicbrainz.org/pub/musicbrainz/%{oname}-%{version}.tar.gz
Patch0:		libmusicbrainz-3.0.3-c++11.patch
BuildRequires:	cmake
BuildRequires:	pkgconfig(cppunit)
BuildRequires:	pkgconfig(libdiscid)
BuildRequires:	pkgconfig(neon)

%description
The MusicBrainz client library allows applications to make metadata
lookup to a MusicBrainz server, generate signatures from WAV data and
create CD Index Disk ids from audio CD roms.

%package -n %{libname}
Summary:	A software library for accesing MusicBrainz servers
Group:		System/Libraries

%description -n %{libname}
The MusicBrainz client library allows applications to make metadata
lookup to a MusicBrainz server, generate signatures from WAV data and
create CD Index Disk ids from audio CD roms.

%package -n %{devname}
Summary:	Headers for developing programs that will use libmusicbrainz
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{devname}
This package contains the headers that programmers will need to develop
applications which will use libmusicbrainz.

%prep
%setup -qn %{oname}-%{version}
%autopatch -p1

%build
%cmake \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo

%make

%install
%makeinstall_std -C build

%files -n %{libname}
%{_libdir}/libmusicbrainz%{api}.so.%{major}*

%files -n %{devname}
%doc AUTHORS.txt COPYING.txt NEWS.txt README.txt
%{_includedir}/musicbrainz%{api}
%{_libdir}/*.so
%{_libdir}/pkgconfig/libmusicbrainz%{api}.pc

