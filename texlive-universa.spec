Name:		texlive-universa
Version:	51984
Release:	1
Summary:	Herbert Bayer's 'universal' font
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/universa
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/universa.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/universa.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/universa.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
An implementation of the universal font by Herbert Bayer of the
Bauhaus school. The MetaFont sources of the fonts, and their
LaTeX support, are all supplied in a LaTeX documented source
(.dtx) file.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/universa
%{_texmfdistdir}/fonts/tfm/public/universa
%{_texmfdistdir}/tex/latex/universa
%doc %{_texmfdistdir}/doc/fonts/universa
#- source
%doc %{_texmfdistdir}/source/fonts/universa

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
