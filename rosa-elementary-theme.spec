%define tarname	rosa-elementary-theme
%define name	rosa-elementary-theme
%define version	2.5.2
%define release 1

Summary:	ROSA-elementary theme
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{tarname}-%{version}.tar.gz
#Theme for openbox
Source1:	%{tarname}-openbox.tar.gz
# new metacity theme
Source2:	metacity-1.tar.bz2
#Aurorae theme
Source3:	rosa-aurorae-1.0.0.tar.xz
License:	GPLv2
Group:		Graphical desktop/Other
URL:		www.rosalinux.com
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
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
%__rm -rf %{buildroot}
%__mkdir -p %{buildroot}%{_datadir}/themes
%__mkdir -p %{buildroot}%{_datadir}/themes/rosa-elementary
cp -rf ./* %{buildroot}%{_datadir}/themes/rosa-elementary
mkdir -p %{buildroot}%{_datadir}/apps/aurorae/themes/rosa/
cp -rf ./rosa-1.0.0/* %{buildroot}%{_datadir}/apps/aurorae/themes/rosa/

%clean
%__rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%{_datadir}/themes/*
%{_datadir}/apps/aurorae/themes/rosa/*