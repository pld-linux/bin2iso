Summary:	Convert BIN into ISO images.
Summary(pl):	Konwertuje pliki obrazów z formatu BIN do iso.
Name:		bin2iso
Version:	1.9b
Release:	1
Group:		Utilities/File
Group(pl):	Narzêdzia/Pliki
License:	unknown
Source0:	http://users.andara.com/~doiron/bin2iso/linux/bin2iso19b_linux.c
URL:		http://users.andara.com/~doiron/bin2iso/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Convert BIN into ISO images.

%description -l pl
Konwertuje pliki obrazów z formatu BIN do iso.

%prep
%setup -q -c -T

%build
gcc $RPM_OPT_FLAGS %{SOURCE0} -o %{name}

%install
rm -rf $RPM_BUILD_ROOT

install -d		$RPM_BUILD_ROOT%{_bindir}
install %{name}		$RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
