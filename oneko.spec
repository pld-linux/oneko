Summary:	Cute cat chasing around your mouse cursor
Summary(pl):	Kotek ganiaj�cy kursor myszy
Name:		oneko
Version:	1.2
Release:	1
License:	GPL
Group:		X11/Amusements
Source0:	%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.png
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
oneko changes your mouse cursor into mouse and creates a little cute
cat and the cat start chasing around your mouse cursor. If the cat
catchup the ``mouse'', start sleeping.

%description -l pl
oneko zmienia kursor w mysz i tworzy kotka, kt�ry zaczyna j� goni�.
Gdy kotek z�apie mysz, idzie spa�.

%prep
%setup -q

%build
%{__cc} %{rpmcflags} %{rpmldflags} oneko.c -o oneko -L%{_libdir} -lm -lX11 -lXext -DSHAPE

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man6,%{_pixmapsdir},%{_applnkdir}/Amusements}
install oneko $RPM_BUILD_ROOT%{_bindir}
install oneko.man $RPM_BUILD_ROOT%{_mandir}/man6/oneko.6

gzip -9nf README README-NEW sample.resource

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Amusements
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man6/*
%{_pixmapsdir}/*
%{_applnkdir}/Amusements/*