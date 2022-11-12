Name:		texlive-epsf
Version:	21461
Release:	1
Summary:	Simple macros for EPS inclusion
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/generic/epsf
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/epsf.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/epsf.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The original graphics inclusion macros for use with dvips;
still widely used by Plain TeX users (in particular). For LaTeX
users, the package is nowadays deprecated in favour of the more
sophisticated standard LaTeX graphics bundle of packages (which
are also available to Plain TeX users, either via its Plain TeX
version, or through the support offered by etex).

%post
%{_sbindir}/texlive.post
%{_bindir}/texhash

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
	%{_bindir}/texhash
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/epsf/epsf.sty
%{_texmfdistdir}/tex/generic/epsf/epsf.tex
%doc %{_texmfdistdir}/doc/generic/epsf/LICENSE
%doc %{_texmfdistdir}/doc/generic/epsf/Makefile
%doc %{_texmfdistdir}/doc/generic/epsf/README
%doc %{_texmfdistdir}/doc/generic/epsf/bboxgrid.ps
%doc %{_texmfdistdir}/doc/generic/epsf/epsf-doc.pdf
%doc %{_texmfdistdir}/doc/generic/epsf/epsf-doc.tex
%doc %{_texmfdistdir}/doc/generic/epsf/fndbadps
%doc %{_texmfdistdir}/doc/generic/epsf/okay/teps.eps
%doc %{_texmfdistdir}/doc/generic/epsf/okay/tepsf.eps
%doc %{_texmfdistdir}/doc/generic/epsf/okay/tepsf1.dvi
%doc %{_texmfdistdir}/doc/generic/epsf/okay/tepsf2.dvi
%doc %{_texmfdistdir}/doc/generic/epsf/okay/tepsf3.dvi
%doc %{_texmfdistdir}/doc/generic/epsf/teps.eps
%doc %{_texmfdistdir}/doc/generic/epsf/tepsf.eps
%doc %{_texmfdistdir}/doc/generic/epsf/tepsf1.tex
%doc %{_texmfdistdir}/doc/generic/epsf/tepsf2.ltx
%doc %{_texmfdistdir}/doc/generic/epsf/tepsf3.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
