%global tl_name epsf
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.7.4
Release:	%{tl_revision}.1
Summary:	Simple macros for EPS inclusion
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/epsf
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/epsf.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/epsf.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The original (and now obsolescent) graphics inclusion macros for use
with dvips, still widely used by Plain TeX users (in particular). For
LaTeX users, the package is nowadays (rather strongly) deprecated in
favour of the more sophisticated standard LaTeX latex-graphics bundle of
packages. (The latex-graphics bundle is also available to Plain TeX
users, via its Plain TeX version.)

