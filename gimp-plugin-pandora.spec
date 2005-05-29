Summary:	Pandora - a Gimp plugin for making panoramas
Summary(pl):	Pandora - wtyczka Gimpa do tworzenia panoram
Name:		gimp-plugin-pandora
Version:	0.7
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://www.shallowsky.com/software/pandora/pandora-%{version}.tar.gz
# Source0-md5:	e094d3546ca51acb4f3c13ae95acf8c9
URL:		http://www.shallowsky.com/software/pandora/
BuildRequires:	gimp-devel
Requires:	gimp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_plugindir	%(gimptool --gimpplugindir)/plug-ins

%description
Pandora is a Gimp plugin for making quick panoramas.

%description -l pl
Pandora jest wtyczk± Gimpa do szybkiego tworzenia panoram.

%prep
%setup -q -n pandora-%{version}

%build
gimptool --build pandora_gen.c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_plugindir}

install pandora_gen $RPM_BUILD_ROOT%{_plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_plugindir}/*
