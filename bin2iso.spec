Summary:	Convert BIN into ISO images
Summary(pl):	Narzêdzie do konwersji plików obrazów z formatu BIN do iso
Name:		bin2iso
Version:	1.9b
Release:	3
License:	Unknown
Group:		Applications/File
Source0:	http://users.andara.com/~doiron/bin2iso/linux/%{name}19b_linux.c
# Source0-md5:	01dab72496175a772bcf6e08c854d440
URL:		http://users.andara.com/~doiron/bin2iso/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Convert BIN into ISO images.

%description -l pl
Narzêdzie do konwersji plików obrazów z formatu BIN do iso.

%prep
%setup -q -c -T

%build
%{__cc} %{rpmcflags} %{SOURCE0} -o %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install %{name} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
