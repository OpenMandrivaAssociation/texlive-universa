# revision 15878
# category Package
# catalog-ctan /fonts/universa
# catalog-date 2008-11-02 01:06:10 +0100
# catalog-license gpl
# catalog-version 2.0
Name:		texlive-universa
Version:	2.0
Release:	11
Summary:	Herbert Bayer's 'universal' font
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/universa
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/universa.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/universa.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/universa.source.tar.xz
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
%{_texmfdistdir}/fonts/source/public/universa/fulbc10.mf
%{_texmfdistdir}/fonts/source/public/universa/fulbc12.mf
%{_texmfdistdir}/fonts/source/public/universa/fulbc17.mf
%{_texmfdistdir}/fonts/source/public/universa/fulbc8.mf
%{_texmfdistdir}/fonts/source/public/universa/fulbc9.mf
%{_texmfdistdir}/fonts/source/public/universa/fulbo10.mf
%{_texmfdistdir}/fonts/source/public/universa/fulbo12.mf
%{_texmfdistdir}/fonts/source/public/universa/fulbo17.mf
%{_texmfdistdir}/fonts/source/public/universa/fulbo8.mf
%{_texmfdistdir}/fonts/source/public/universa/fulbo9.mf
%{_texmfdistdir}/fonts/source/public/universa/fulbr10.mf
%{_texmfdistdir}/fonts/source/public/universa/fulbr12.mf
%{_texmfdistdir}/fonts/source/public/universa/fulbr17.mf
%{_texmfdistdir}/fonts/source/public/universa/fulbr8.mf
%{_texmfdistdir}/fonts/source/public/universa/fulbr9.mf
%{_texmfdistdir}/fonts/source/public/universa/fulbst10.mf
%{_texmfdistdir}/fonts/source/public/universa/fulbst12.mf
%{_texmfdistdir}/fonts/source/public/universa/fulbst17.mf
%{_texmfdistdir}/fonts/source/public/universa/fulbst8.mf
%{_texmfdistdir}/fonts/source/public/universa/fulbst9.mf
%{_texmfdistdir}/fonts/source/public/universa/fulmc10.mf
%{_texmfdistdir}/fonts/source/public/universa/fulmc12.mf
%{_texmfdistdir}/fonts/source/public/universa/fulmc17.mf
%{_texmfdistdir}/fonts/source/public/universa/fulmc8.mf
%{_texmfdistdir}/fonts/source/public/universa/fulmc9.mf
%{_texmfdistdir}/fonts/source/public/universa/fulmo10.mf
%{_texmfdistdir}/fonts/source/public/universa/fulmo12.mf
%{_texmfdistdir}/fonts/source/public/universa/fulmo17.mf
%{_texmfdistdir}/fonts/source/public/universa/fulmo8.mf
%{_texmfdistdir}/fonts/source/public/universa/fulmo9.mf
%{_texmfdistdir}/fonts/source/public/universa/fulmr10.mf
%{_texmfdistdir}/fonts/source/public/universa/fulmr12.mf
%{_texmfdistdir}/fonts/source/public/universa/fulmr17.mf
%{_texmfdistdir}/fonts/source/public/universa/fulmr8.mf
%{_texmfdistdir}/fonts/source/public/universa/fulmr9.mf
%{_texmfdistdir}/fonts/source/public/universa/fulmst10.mf
%{_texmfdistdir}/fonts/source/public/universa/fulmst12.mf
%{_texmfdistdir}/fonts/source/public/universa/fulmst17.mf
%{_texmfdistdir}/fonts/source/public/universa/fulmst8.mf
%{_texmfdistdir}/fonts/source/public/universa/fulmst9.mf
%{_texmfdistdir}/fonts/source/public/universa/uniacc.mf
%{_texmfdistdir}/fonts/source/public/universa/unibase.mf
%{_texmfdistdir}/fonts/source/public/universa/unidig.mf
%{_texmfdistdir}/fonts/source/public/universa/uniext.mf
%{_texmfdistdir}/fonts/source/public/universa/unilig.mf
%{_texmfdistdir}/fonts/source/public/universa/unilow.mf
%{_texmfdistdir}/fonts/source/public/universa/unipun.mf
%{_texmfdistdir}/fonts/source/public/universa/unispe.mf
%{_texmfdistdir}/fonts/source/public/universa/uniupp.mf
%{_texmfdistdir}/fonts/tfm/public/universa/fulbc10.tfm
%{_texmfdistdir}/fonts/tfm/public/universa/fulbc12.tfm
%{_texmfdistdir}/fonts/tfm/public/universa/fulbc17.tfm
%{_texmfdistdir}/fonts/tfm/public/universa/fulbc8.tfm
%{_texmfdistdir}/fonts/tfm/public/universa/fulbc9.tfm
%{_texmfdistdir}/fonts/tfm/public/universa/fulbo10.tfm
%{_texmfdistdir}/fonts/tfm/public/universa/fulbo12.tfm
%{_texmfdistdir}/fonts/tfm/public/universa/fulbo17.tfm
%{_texmfdistdir}/fonts/tfm/public/universa/fulbo8.tfm
%{_texmfdistdir}/fonts/tfm/public/universa/fulbo9.tfm
%{_texmfdistdir}/fonts/tfm/public/universa/fulbr10.tfm
%{_texmfdistdir}/fonts/tfm/public/universa/fulbr12.tfm
%{_texmfdistdir}/fonts/tfm/public/universa/fulbr17.tfm
%{_texmfdistdir}/fonts/tfm/public/universa/fulbr8.tfm
%{_texmfdistdir}/fonts/tfm/public/universa/fulbr9.tfm
%{_texmfdistdir}/fonts/tfm/public/universa/fulbst10.tfm
%{_texmfdistdir}/fonts/tfm/public/universa/fulbst12.tfm
%{_texmfdistdir}/fonts/tfm/public/universa/fulbst17.tfm
%{_texmfdistdir}/fonts/tfm/public/universa/fulbst8.tfm
%{_texmfdistdir}/fonts/tfm/public/universa/fulbst9.tfm
%{_texmfdistdir}/fonts/tfm/public/universa/fulmc10.tfm
%{_texmfdistdir}/fonts/tfm/public/universa/fulmc12.tfm
%{_texmfdistdir}/fonts/tfm/public/universa/fulmc17.tfm
%{_texmfdistdir}/fonts/tfm/public/universa/fulmc8.tfm
%{_texmfdistdir}/fonts/tfm/public/universa/fulmc9.tfm
%{_texmfdistdir}/fonts/tfm/public/universa/fulmo10.tfm
%{_texmfdistdir}/fonts/tfm/public/universa/fulmo12.tfm
%{_texmfdistdir}/fonts/tfm/public/universa/fulmo17.tfm
%{_texmfdistdir}/fonts/tfm/public/universa/fulmo8.tfm
%{_texmfdistdir}/fonts/tfm/public/universa/fulmo9.tfm
%{_texmfdistdir}/fonts/tfm/public/universa/fulmr10.tfm
%{_texmfdistdir}/fonts/tfm/public/universa/fulmr12.tfm
%{_texmfdistdir}/fonts/tfm/public/universa/fulmr17.tfm
%{_texmfdistdir}/fonts/tfm/public/universa/fulmr8.tfm
%{_texmfdistdir}/fonts/tfm/public/universa/fulmr9.tfm
%{_texmfdistdir}/fonts/tfm/public/universa/fulmst10.tfm
%{_texmfdistdir}/fonts/tfm/public/universa/fulmst12.tfm
%{_texmfdistdir}/fonts/tfm/public/universa/fulmst17.tfm
%{_texmfdistdir}/fonts/tfm/public/universa/fulmst8.tfm
%{_texmfdistdir}/fonts/tfm/public/universa/fulmst9.tfm
%{_texmfdistdir}/tex/latex/universa/omluni.fd
%{_texmfdistdir}/tex/latex/universa/omsuni.fd
%{_texmfdistdir}/tex/latex/universa/ot1uni.fd
%{_texmfdistdir}/tex/latex/universa/t1uni.fd
%{_texmfdistdir}/tex/latex/universa/uni.sty
%{_texmfdistdir}/tex/latex/universa/uuni.fd
%doc %{_texmfdistdir}/doc/fonts/universa/README.uni
%doc %{_texmfdistdir}/doc/fonts/universa/copyright.tex
%doc %{_texmfdistdir}/doc/fonts/universa/unidoc.sty
#- source
%doc %{_texmfdistdir}/source/fonts/universa/uni.dtx
%doc %{_texmfdistdir}/source/fonts/universa/uni.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.0-2
+ Revision: 757292
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.0-1
+ Revision: 719853
- texlive-universa
- texlive-universa
- texlive-universa

