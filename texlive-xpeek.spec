Name:		texlive-xpeek
Version:	61719
Release:	2
Summary:	Define commands that peek ahead in the input stream
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/xpeek
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xpeek.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xpeek.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xpeek.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides tools to help define commands that, like
\xspace (from xspace) and the LaTeX command \textit, peek at
what follows them in the command stream and choose appropriate
behaviour.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/xpeek/xpeek.sty
%doc %{_texmfdistdir}/doc/latex/xpeek/README
%doc %{_texmfdistdir}/doc/latex/xpeek/xpeek.pdf
#- source
%doc %{_texmfdistdir}/source/latex/xpeek/xpeek.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
