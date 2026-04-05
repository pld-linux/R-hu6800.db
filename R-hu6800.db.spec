%define		packname	hu6800.db

%undefine	_debugsource_packages
Summary:	Affymetrix HuGeneFL Genome Array annotation data (chip hu6800)
Name:		R-%{packname}
Version:	3.13.0
Release:	1
License:	Artistic 2.0
Group:		Applications/Engineering
Source0:	https://bioconductor.org/packages/release/data/annotation/src/contrib/%{packname}_%{version}.tar.gz
# Source0-md5:	aa1cb6c107dee6d2ed1929b48aa831e9
URL:		https://bioconductor.org/packages/release/data/annotation/html/hu6800.db.html
BuildRequires:	R-AnnotationDbi
BuildRequires:	R-org.Hs.eg.db
BuildRequires:	R
BuildRequires:	texlive-latex
Requires:	R-AnnotationDbi
Requires:	R-org.Hs.eg.db
Requires:	R
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Affymetrix HuGeneFL Genome Array annotation data (chip hu6800)
assembled using data from public repositories.

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/R/library

R CMD INSTALL %{packname} -l $RPM_BUILD_ROOT%{_libdir}/R/library

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_libdir}/R/library/%{packname}/
%doc %{_libdir}/R/library/%{packname}/DESCRIPTION
%doc %{_libdir}/R/library/%{packname}/html/
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/Meta/
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/R/
%{_libdir}/R/library/%{packname}/help/
%{_libdir}/R/library/%{packname}/extdata
