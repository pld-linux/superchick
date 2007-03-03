%define		exec_name	superchick
Summary:	Manga comic files viewer
Summary(pl.UTF-8):	Przeglądarka plików z komiksami manga
Name:		superchick
Version:	0.4
Release:	1
License:	GPL v2
Group:		X11/Applications/Graphics
Source0:	http://www.sacredchao.net/~piman/software/%{name}-%{version}.tar.bz2
# Source0-md5:	fdcfd94f49a2be231dea528d4952499e
URL:		http://www.sacredchao.net/~piman/
Requires:	python >= 2.3
Requires:       python-pygame
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Superchick is a program to view manga, that is, Japanese comics. It
can also be easily used to view American comics, or any other
collection of images. However the feature set is slanted towards
viewing images that should be displayed in alphabetical order, 1-2 per
screen, and in right to left order.

%description -l pl.UTF-8
Superchick jest programem do wyświetlania mangi, tj. japońskich
komiksów. Może być także bez przeszkód użyty do wyświetlania komiksów
amerykańskich, lub jakichkolwiek innych kolekcji obrazów, jednakże
jest on tworzony z myślą o wyświetlaniu obrazów, które mają być
ukazywane w kolejności alfabetycznej, 1-2 na ekran i w orientacji
od-prawej-do-lewej.

%prep
%setup -q

%build
find -type f -exec sed -i -e 's|#!.*python.*|#!%{_bindir}/python|g' "{}" ";"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT
install -D %{exec_name}.1 $RPM_BUILD_ROOT%{_mandir}/man1/%{exec_name}.1
chmod a+x %{exec_name}.py
install -D %{exec_name}.py $RPM_BUILD_ROOT%{_bindir}/%{exec_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README
%{_mandir}/man1/*
%attr(755,root,root) %{_bindir}/*
