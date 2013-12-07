Summary:	ROSA-elementary theme
Name:		rosa-elementary-theme
Version:	2.6.1
Release:	5
Source0:	%{name}-%{version}.tar.gz
#Theme for openbox
Source1:	%{name}-openbox.tar.gz
# new metacity theme
Source2:	metacity-1.tar.bz2
#Aurorae theme
Source3:	rosa-aurorae-1.0.1.tar.xz
License:	GPLv2
Group:		Graphical desktop/Other
URL:		http://www.rosalinux.com
BuildArch:	noarch
Requires:	murrine
Requires:	gtk-aurora-engine
Suggests:	rosa-icons

%description
ROSA-elementary theme creates specially for the ROSA.
Originally based on Elementary theme by Daniel Fore 
(aka Dan Rabbit).

%prep
%setup -q -a1
rm -fr metacity-1

tar xjf %{SOURCE2}
tar xJf %{SOURCE3}

%install
mkdir -p %{buildroot}%{_datadir}/themes
mkdir -p %{buildroot}%{_datadir}/themes/rosa-elementary
cp -rf ./* %{buildroot}%{_datadir}/themes/rosa-elementary
mkdir -p %{buildroot}%{_datadir}/apps/aurorae/themes/rosa/
cp -rf ./rosa-1.0.1/* %{buildroot}%{_datadir}/apps/aurorae/themes/rosa/

%files
%{_datadir}/themes/*
%dir %{_datadir}/apps/aurorae/themes/rosa
%{_datadir}/apps/aurorae/themes/rosa/*
