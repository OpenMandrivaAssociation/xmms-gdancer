%define name xmms-gdancer
%define oname gdancer
%define version 0.4.6
%define release %mkrel 4

Name:		%{name}
Summary:	GDancer - The Dancing Space Ghost XMMS plugin
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Sound
URL:		http://www.figz.com/gdancer/
Source:		%{oname}-%{version}.tar.bz2
Buildrequires:	xmms1-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
GDancer is a cute little plugin for XMMS that allows for a character to
dance to the music playing.  It also supports themes so you can pick
different characters to dance for you.

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q -n %{oname}-%{version}


%build

#we don't use libtool 1.5 yet
%define __libtoolize /bin/true

%configure

%make


%install
make DESTDIR=$RPM_BUILD_ROOT install


%clean
rm -rf $RPM_BUILD_ROOT


%post
/sbin/ldconfig -n %{_libdir}/xmms/Visualization


%postun
/sbin/ldconfig -n %{_libdir}/xmms/Visualization


%files
%defattr(-,root,root,0755)
%doc AUTHORS COPYING ChangeLog INSTALL 
%doc NEWS README README.themes TODO
%{_libdir}/xmms/Visualization/*


