%global tl_name universa
%global tl_revision 51984

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.1
Release:	%{tl_revision}.1
Summary:	Herbert Bayers universal font
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/universa
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/universa.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/universa.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/universa.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
An implementation of the "universal" font by Herbert Bayer of the
Bauhaus school. The Metafont sources of the fonts, and their LaTeX
support, are all supplied in a LaTeX documented source (.dtx) file.

