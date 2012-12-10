%define     real_name  Feedjack
Name:		feedjack
Version:	0.9.16
Release:	%mkrel 4
Summary:	A web based rss and atom feed aggregator 
License:	BSD
Group:      Networking/News 
URL:		http://www.feedjack.org/
Source:		http://www.feedjack.org/download/%{real_name}-%{version}.tar.bz2
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-root
Buildrequires:	python-devel
BuildArch:      noarch
BuildRequires:  python-django
BuildRequires:  python-setuptools 
Requires:       python-django python-feedparser
%description
Feedjack is a rss and atom feed aggregator.
 
Like the Planet feed aggregator:
  * It downloads feeds and aggregate their contents in a single site
  * The new aggregated site has a feed of its own (atom and rss)
  * It uses Mark Pilgrim?s excelent FeedParser
  *  The subscriber list can be exported as OPML and FOAF

But FeedJack also has some advantages:
  * It handles historical data, you can read old posts
  * It parses a lot more info, including post categories
  * It generates pages/feeds with posts of a certain category 
  * It generates pages/feeds with posts from a certain subscriber 
  * It generates pages/feeds with posts of a certain category from a certain 
    subscriber 
  * A cloud tag/folksonomy (hype 2.0 compliant) for every page and every 
    subscriber
  * It uses Django templates
  * The administration is done via web and can handle multiple planets.
  * Extensive use of djangoi's internal cache engine. Most of the time you 
    will have no database hits when serving pages.

%prep
%setup -q -n %real_name-%version

%build
python setup.py build

%install
python setup.py install --root %buildroot

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc LICENSE AUTHORS  CHANGES README
%doc INSTALL
%{_bindir}/*
%{py_puresitedir}/%{name}
%{py_puresitedir}/*.egg-info


%changelog
* Tue Nov 02 2010 Michael Scherer <misc@mandriva.org> 0.9.16-4mdv2011.0
+ Revision: 592394
- rebuild for python 2.7

* Thu Sep 10 2009 Thierry Vignaud <tv@mandriva.org> 0.9.16-3mdv2010.0
+ Revision: 437530
- rebuild

* Tue Jan 06 2009 Funda Wang <fwang@mandriva.org> 0.9.16-2mdv2009.1
+ Revision: 325237
- rebuild

* Tue Sep 09 2008 Michael Scherer <misc@mandriva.org> 0.9.16-1mdv2009.0
+ Revision: 282932
- update to new version 0.9.16

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.9.10-3mdv2009.0
+ Revision: 245077
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.9.10-1mdv2008.1
+ Revision: 136411
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Jul 02 2007 Michael Scherer <misc@mandriva.org> 0.9.10-1mdv2008.0
+ Revision: 47104
- Import feedjack

