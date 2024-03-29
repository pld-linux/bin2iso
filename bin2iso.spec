Summary:	Convert BIN into ISO images
Summary(pl.UTF-8):	Narzędzie do konwersji plików obrazów z formatu BIN do iso
Name:		bin2iso
Version:	1.9b
Release:	8
License:	unknown
Group:		Applications/File
# http://users.andara.com/~doiron/bin2iso/linux/%{name}19b_linux.c
Source0:	%{name}19b_linux.c
Source1:	http://users.andara.com/~doiron/bin2iso/readme.txt
# Source1-md5:	703e50ee80e5c15a742458aab8a93340
Patch0:		%{name}-warnings.patch
URL:		http://users.andara.com/~doiron/bin2iso/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Convert BIN into ISO images.

%description -l pl.UTF-8
Narzędzie do konwersji plików obrazów z formatu BIN do iso.

%prep
%setup -q -c -T
install %{SOURCE0} %{name}.c
install %{SOURCE1} readme.txt
%patch0 -p0

%build
%{__cc} -Wall %{rpmcflags} %{rpmldflags} %{name}.c -o %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install %{name} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%doc readme.txt
