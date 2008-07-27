Summary:	Cute cat chasing around your mouse cursor
Summary(pl.UTF-8):	Kotek ganiający kursor myszy
Name:		oneko
Version:	1.2
Release:	8
License:	Public Domain (?)
Group:		X11/Amusements
Source0:	http://agtoys.sourceforge.net/oneko/%{name}-%{version}.tar.gz
# Source0-md5:	890a476b54e13bfd4ab21440c6a5a8e2
Source1:	%{name}.desktop
Source2:	%{name}.png
BuildRequires:	xorg-lib-libXext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
oneko changes your mouse cursor into mouse and creates a little cute
cat and the cat start chasing around your mouse cursor. If the cat
catchup the ``mouse'', start sleeping.

%description -l pl.UTF-8
oneko zmienia kursor w mysz i tworzy kotka, który zaczyna ją gonić.
Gdy kotek złapie mysz, idzie spać.

%prep
%setup -q

%build
%{__cc} %{rpmcflags} %{rpmldflags} oneko.c -o oneko -lm -lX11 -lXext -DSHAPE

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man6,%{_pixmapsdir},%{_desktopdir}}

install oneko $RPM_BUILD_ROOT%{_bindir}
install oneko.man $RPM_BUILD_ROOT%{_mandir}/man6/oneko.6

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README README-NEW sample.resource
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man6/*
%{_pixmapsdir}/*
%{_desktopdir}/*.desktop
