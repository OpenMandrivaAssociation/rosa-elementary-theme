%define tarname	rosa-elementary-theme
%define name	rosa-elementary-theme
%define version	2.4.1
%define release %mkrel 1

Summary:	ROSA-elementary theme
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{tarname}-%{version}.tar.gz
License:	GPLv2
Group:		Graphical desktop/Other
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires: 	murrine
Requires:	gtk-aurora-engine
Suggests:	rosa-icons

%description
ROSA-elementary theme creates specially for the Mandriva. Based on the original theme
by Daniel Fore (aka Dan Rabbit).

%prep
%setup -q

%install
%__rm -rf %{buildroot}
%__mkdir -p %{buildroot}%{_datadir}/themes
%__mkdir -p %{buildroot}%{_datadir}/themes/rosa-elementary
cp -rf ./* %{buildroot}%{_datadir}/themes/rosa-elementary

%clean
%__rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%{_datadir}/themes/rosa-elementary/*
