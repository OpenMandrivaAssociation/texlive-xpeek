%global tl_name xpeek
%global tl_revision 61719

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2
Release:	%{tl_revision}.1
Summary:	Define commands that peek ahead in the input stream
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/xpeek
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xpeek.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xpeek.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xpeek.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides tools to help define commands that, like \xspace
and the LaTeX command \textit, peek at what follows them in the command
stream and choose appropriate behaviour.

